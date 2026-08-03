#!/usr/bin/env python3
"""
Open Trades Brain offline app builder.
Scans notes/**/*.md next to this script, builds ONE fully self-contained
offline HTML app (no internet, no CDN, no external files): index.html
Usage:  python3 build_app.py
"""
import os, re, json, html, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(HERE, "notes")
OUT_PATH  = os.path.join(HERE, "index.html")

# ---------------- tiny markdown -> html ----------------
def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out, i, in_code, in_table = [], 0, False, False
    def flush_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            if not in_code:
                flush_table(); out.append("<pre><code>"); in_code = True
            else:
                out.append("</code></pre>"); in_code = False
            i += 1; continue
        if in_code:
            out.append(html.escape(ln) + "\n"); i += 1; continue
        s = ln.strip()
        # tables
        if s.startswith("|") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c or "---") for c in cells):
                i += 1; continue
            if not in_table:
                out.append("<table><tbody>"); in_table = True
            tag = "th" if i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i+1]) else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
            i += 1; continue
        flush_table()
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1)); out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if re.match(r"^[-*]\s+", s):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i])); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        if re.match(r"^\d+\.\s+", s):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i])); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
        if s.startswith(">"):
            out.append(f"<blockquote>{inline(s.lstrip('> '))}</blockquote>"); i += 1; continue
        if s in ("---", "***"):
            out.append("<hr>"); i += 1; continue
        if s == "":
            i += 1; continue
        out.append(f"<p>{inline(s)}</p>"); i += 1
    flush_table()
    if in_code: out.append("</code></pre>")
    return "\n".join(out)

def inline(t: str) -> str:
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t

# ---------------- collect docs ----------------
def collect():
    docs = []
    for root, _, files in os.walk(NOTES_DIR):
        for f in sorted(files):
            if not f.lower().endswith(".md"):
                continue
            path = os.path.join(root, f)
            raw = open(path, encoding="utf-8", errors="replace").read()
            rel = os.path.relpath(path, NOTES_DIR)
            cat = os.path.dirname(rel).replace("\\", "/") or "General"
            title = None
            for ln in raw.split("\n"):
                m = re.match(r"^#\s+(.*)", ln.strip())
                if m:
                    title = m.group(1).strip(); break
            if not title:
                title = re.sub(r"\.md$", "", f).replace("-", " ").replace("_", " ").title()
            # plain text for search
            text = re.sub(r"[#*`>|\-]{1,}", " ", raw)
            text = re.sub(r"\s+", " ", text).strip()
            docs.append({
                "id": hashlib.md5(rel.encode()).hexdigest()[:10],
                "title": title, "cat": cat, "file": rel,
                "html": md_to_html(raw), "text": text[:200000],
            })
    docs.sort(key=lambda d: (d["cat"], d["title"]))
    return docs

# ---------------- app template ----------------
APP = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Open Trades Brain — Offline Knowledge Base</title>
<style>
:root{--bg:#0f1419;--panel:#171e26;--panel2:#1e2833;--line:#2a3644;--txt:#dbe4ec;--dim:#8fa1b3;--acc:#3fa7ff;--acc2:#ffb347;--hl:#5a4a00}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--txt);height:100vh;display:flex;flex-direction:column;overflow:hidden}
header{display:flex;align-items:center;gap:10px;padding:10px 14px;background:var(--panel);border-bottom:1px solid var(--line);flex-shrink:0}
header h1{font-size:16px;white-space:nowrap;color:var(--acc)}
#burger{display:none;background:none;border:1px solid var(--line);color:var(--txt);border-radius:6px;padding:6px 10px;font-size:18px;cursor:pointer}
#search{flex:1;padding:9px 12px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--txt);font-size:15px;outline:none}
#search:focus{border-color:var(--acc)}
#wrap{flex:1;display:flex;min-height:0}
#side{width:270px;background:var(--panel);border-right:1px solid var(--line);overflow-y:auto;flex-shrink:0;padding:10px}
#side h3{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);margin:12px 4px 6px}
.catdoc{display:block;width:100%;text-align:left;background:none;border:none;color:var(--txt);padding:7px 10px;border-radius:6px;cursor:pointer;font-size:13.5px;line-height:1.35}
.catdoc:hover{background:var(--panel2)}
.catdoc.active{background:var(--panel2);color:var(--acc)}
#main{flex:1;overflow-y:auto;padding:18px 22px;min-width:0}
#results .hit{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin-bottom:10px;cursor:pointer}
#results .hit:hover{border-color:var(--acc)}
#results .hit b{color:var(--acc);font-size:15px}
#results .hit .c{font-size:11px;color:var(--acc2);margin-left:8px}
#results .hit p{font-size:13px;color:var(--dim);margin-top:5px;line-height:1.45}
mark{background:var(--hl);color:#ffe9a8;border-radius:3px;padding:0 2px}
#docview{max-width:900px}
#docview .meta{font-size:12px;color:var(--dim);margin:4px 0 14px}
#docview .back{display:inline-block;margin-bottom:12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);padding:6px 12px;border-radius:6px;cursor:pointer;font-size:13px}
#docview h1{font-size:24px;margin-bottom:6px;color:var(--acc)}
#docview h2{font-size:19px;margin:22px 0 8px;border-bottom:1px solid var(--line);padding-bottom:4px}
#docview h3{font-size:16px;margin:16px 0 6px;color:var(--acc2)}
#docview h4{font-size:14px;margin:12px 0 4px}
#docview p{margin:8px 0;line-height:1.6;font-size:14.5px}
#docview ul,#docview ol{margin:8px 0 8px 22px;line-height:1.55;font-size:14.5px}
#docview table{border-collapse:collapse;margin:12px 0;width:100%;font-size:13px}
#docview th,#docview td{border:1px solid var(--line);padding:6px 9px;text-align:left}
#docview th{background:var(--panel2)}
#docview code{background:var(--panel2);padding:1px 5px;border-radius:4px;font-size:13px}
#docview pre{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px;overflow-x:auto;margin:10px 0}
#docview blockquote{border-left:3px solid var(--acc2);padding:4px 12px;color:var(--dim);margin:10px 0}
#count{font-size:12px;color:var(--dim);white-space:nowrap}
@media(max-width:760px){
 #burger{display:block}
 #side{position:fixed;left:0;top:0;bottom:0;z-index:20;transform:translateX(-100%);transition:.2s}
 #side.open{transform:none}
 header h1{display:none}
 #main{padding:14px}
}
</style></head><body>
<header>
<button id="burger">☰</button><h1>🧠 Open Trades Brain</h1>
<input id="search" type="search" placeholder="Search error codes, models, symptoms…" autocomplete="off">
<span id="count"></span>
</header>
<div id="wrap"><nav id="side"></nav><main id="main"></main></div>
<script>
const DOCS = __DATA__;
const $=s=>document.querySelector(s);
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const toks=s=>(s.toLowerCase().match(/[a-z0-9]+/g)||[]);
// build inverted index
const IDX={};
DOCS.forEach((d,di)=>{const bag={};toks(d.title+" "+d.text).forEach(t=>bag[t]=(bag[t]||0)+1);
 for(const t in bag){(IDX[t]=IDX[t]||[]).push([di,bag[t]]);}});
function search(q){
 const qs=toks(q);if(!qs.length)return[];
 const score=new Map();
 qs.forEach(t=>{
   const hits=IDX[t]||[];
   hits.forEach(([di,tf])=>score.set(di,(score.get(di)||0)+tf));
   // prefix matches for partial codes like "E1" or "407"
   if(hits.length===0||t.length>=2){
     for(const k in IDX){if(k.startsWith(t)&&k!==t){IDX[k].forEach(([di,tf])=>score.set(di,(score.get(di)||0)+tf*0.6));}}
   }
 });
 // require all query terms present (AND) unless single term
 if(qs.length>1){
   for(const [di]of score){
     const dt=(DOCS[di].title+" "+DOCS[di].text).toLowerCase();
     if(!qs.every(t=>dt.includes(t)))score.delete(di);
   }
 }
 const res=[...score.entries()].map(([di,s])=>{
   const d=DOCS[di];const tl=d.title.toLowerCase();
   qs.forEach(t=>{if(tl.includes(t))s+=25;});
   return[di,s];
 }).sort((a,b)=>b[1]-a[1]).slice(0,60);
 return res.map(([di])=>di);
}
function snippet(d,qs){
 const t=d.text;const lt=t.toLowerCase();let pos=-1;
 for(const q of qs){pos=lt.indexOf(q);if(pos>=0)break;}
 if(pos<0)pos=0;
 const start=Math.max(0,pos-70);let sn=t.slice(start,start+230);
 qs.forEach(q=>{sn=sn.replace(new RegExp("("+q.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+")","ig"),"<mark>$1</mark>")});
 return(start>0?"…":"")+sn+(start+230<t.length?"…":"");
}
function showResults(q){
 const qs=toks(q);const idxs=search(q);
 $("#count").textContent=idxs.length+" result"+(idxs.length===1?"":"s");
 $("#main").innerHTML='<div id="results">'+(idxs.length?idxs.map(di=>{const d=DOCS[di];
   return`<div class="hit" onclick="openDoc('${d.id}')"><b>${esc(d.title)}</b><span class="c">${esc(d.cat)}</span><p>${snippet(d,qs)}</p></div>`}).join("")
  :'<p style="color:var(--dim);padding:20px">No matches. Try an error code (E4, F1), a model number, or a symptom ("short cycling", "frozen coil").</p>')+"</div>";
}
function openDoc(id){
 const d=DOCS.find(x=>x.id===id);if(!d)return;
 $("#count").textContent=d.cat;
 $("#main").innerHTML=`<div id="docview"><button class="back" onclick="goHome()">← Back</button><h1>${esc(d.title)}</h1><div class="meta">${esc(d.cat)} · ${esc(d.file)}</div>${d.html}</div>`;
 $("#main").scrollTop=0;$("#side").classList.remove("open");
 document.querySelectorAll(".catdoc").forEach(b=>b.classList.toggle("active",b.dataset.id===id));
}
function goHome(){renderSide();$("#main").innerHTML=$("#main").dataset.home;$("#count").textContent=DOCS.length+" docs";}
function renderSide(){
 const cats={};DOCS.forEach(d=>{(cats[d.cat]=cats[d.cat]||[]).push(d);});
 $("#side").innerHTML=Object.keys(cats).sort().map(c=>
  `<h3>${esc(c)} (${cats[c].length})</h3>`+cats[c].map(d=>
  `<button class="catdoc" data-id="${d.id}" onclick="openDoc('${d.id}')">${esc(d.title)}</button>`).join("")).join("");
}
window.addEventListener("DOMContentLoaded",()=>{
 renderSide();
 const byCat={};DOCS.forEach(d=>{(byCat[d.cat]=byCat[d.cat]||[]).push(d);});
 const home=`<h2 style="margin-bottom:10px">Offline library ready — ${DOCS.length} documents</h2>
 <p style="color:var(--dim);margin-bottom:16px">Everything is stored inside this one file. No internet needed. Use the search bar for error codes, model numbers, or symptoms, or browse by category on the left.</p>`
 +Object.keys(byCat).sort().map(c=>`<div class="hit" style="cursor:default"><b>${esc(c)}</b><p>${byCat[c].slice(0,8).map(d=>esc(d.title)).join(" · ")}${byCat[c].length>8?" · …":""}</p></div>`).join("");
 $("#main").innerHTML=home;$("#main").dataset.home=home;
 $("#count").textContent=DOCS.length+" docs";
 let tm;$("#search").addEventListener("input",e=>{clearTimeout(tm);const v=e.target.value.trim();
   tm=setTimeout(()=>v?showResults(v):goHome(),160);});
 $("#burger").addEventListener("click",()=>$("#side").classList.toggle("open"));
 document.addEventListener("keydown",e=>{if(e.key==="/"&&document.activeElement!==$("#search")){e.preventDefault();$("#search").focus();}});
});
</script></body></html>"""

def main():
    docs = collect()
    data = json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")
    page = APP.replace("__DATA__", data)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    open(OUT_PATH, "w", encoding="utf-8").write(page)
    print(f"Built {OUT_PATH} — {len(docs)} docs, {os.path.getsize(OUT_PATH)//1024} KB")

if __name__ == "__main__":
    main()
