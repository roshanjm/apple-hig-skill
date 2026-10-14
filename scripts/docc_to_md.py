#!/usr/bin/env python3
"""Render Apple HIG DocC JSON pages to Markdown.

usage: docc_to_md.py <json_dir> <out_dir>
Writes one .md per page plus _index.json with title/section/platforms/abstract.
"""
import json
import os
import re
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
SITE = "https://developer.apple.com"


class Page:
    def __init__(self, doc):
        self.doc = doc
        self.refs = doc.get("references", {})

    # ---------- inline ----------
    def inline(self, nodes):
        out = []
        for n in nodes or []:
            t = n.get("type")
            if t == "text":
                out.append(n.get("text", ""))
            elif t == "strong":
                out.append("**" + self.inline(n.get("inlineContent")) + "**")
            elif t == "emphasis":
                out.append("*" + self.inline(n.get("inlineContent")) + "*")
            elif t == "codeVoice":
                out.append("`" + n.get("code", "") + "`")
            elif t == "small":
                out.append("_" + self.inline(n.get("inlineContent")) + "_")
            elif t == "reference":
                out.append(self.ref_link(n))
            elif t == "image":
                cap = self.inline((n.get("metadata") or {}).get("abstract"))
                if cap:
                    out.append(f"*[Image: {cap}]*")
            elif t == "newTerm":
                out.append("*" + self.inline(n.get("inlineContent")) + "*")
            elif t in ("superscript", "subscript", "strikethrough"):
                out.append(self.inline(n.get("inlineContent")))
            elif t == "inlineHead":
                out.append(self.inline(n.get("inlineContent")))
            elif "inlineContent" in n:
                out.append(self.inline(n["inlineContent"]))
            elif "text" in n:
                out.append(n["text"])
        return "".join(out)

    def ref_link(self, n):
        ident = n.get("identifier", "")
        r = self.refs.get(ident, {})
        title = None
        if n.get("overridingTitleInlineContent"):
            title = self.inline(n["overridingTitleInlineContent"])
        elif n.get("overridingTitle"):
            title = n["overridingTitle"]
        elif r.get("titleInlineContent"):
            title = self.inline(r["titleInlineContent"])
        else:
            title = r.get("title") or ident.rsplit("/", 1)[-1]
        url = r.get("url") or (ident if ident.startswith("http") else "")
        if url.startswith("/"):
            url = SITE + url
        return f"[{title}]({url})" if url else title

    # ---------- blocks ----------
    def blocks(self, nodes, depth=0):
        out = []
        for b in nodes or []:
            t = b.get("type")
            if t == "heading":
                lvl = min(max(int(b.get("level", 2)), 2), 6)
                out.append("\n" + "#" * lvl + " " + b.get("text", "") + "\n")
            elif t == "paragraph":
                s = self.inline(b.get("inlineContent"))
                if s.strip():
                    out.append(s + "\n")
            elif t == "unorderedList":
                for it in b.get("items", []):
                    body = self.blocks(it.get("content"), depth + 1).strip()
                    body = body.replace("\n", "\n  ")
                    out.append("- " + body)
                out.append("")
            elif t == "orderedList":
                for i, it in enumerate(b.get("items", []), 1):
                    body = self.blocks(it.get("content"), depth + 1).strip()
                    body = body.replace("\n", "\n   ")
                    out.append(f"{i}. " + body)
                out.append("")
            elif t == "table":
                out.append(self.table(b))
            elif t == "row":
                for col in b.get("columns", []):
                    s = self.blocks(col.get("content"), depth).strip()
                    if s:
                        out.append(s)
                out.append("")
            elif t == "links":
                for ident in b.get("items", []):
                    r = self.refs.get(ident, {})
                    title = r.get("title", ident)
                    url = r.get("url", "")
                    if url.startswith("/"):
                        url = SITE + url
                    ab = self.inline(r.get("abstract"))
                    out.append(f"- [{title}]({url})" + (f" — {ab}" if ab else ""))
                out.append("")
            elif t == "aside":
                name = b.get("name") or b.get("style", "Note").title()
                body = self.blocks(b.get("content"), depth).strip().replace("\n", "\n> ")
                out.append(f"> **{name}:** {body}\n")
            elif t == "tabNavigator":
                for tab in b.get("tabs", []):
                    body = self.blocks(tab.get("content"), depth).strip()
                    out.append(f"**{tab.get('title','')}**" + (f": {body}" if body else ""))
                out.append("")
            elif t == "video":
                pass  # purely illustrative
            elif t == "codeListing":
                code = "\n".join(b.get("code", []))
                out.append(f"```{b.get('syntax','')}\n{code}\n```\n")
            elif t == "small":
                out.append("_" + self.inline(b.get("inlineContent")) + "_\n")
            elif t == "termList":
                for it in b.get("items", []):
                    term = self.inline(it.get("term", {}).get("inlineContent"))
                    d = self.blocks(it.get("definition", {}).get("content"), depth + 1).strip()
                    out.append(f"- **{term}**: {d}")
                out.append("")
            elif "content" in b:
                out.append(self.blocks(b["content"], depth))
            elif "inlineContent" in b:
                out.append(self.inline(b["inlineContent"]) + "\n")
        return "\n".join(out)

    def table(self, b):
        rows = []
        for row in b.get("rows", []):
            cells = []
            for cell in row:
                s = self.blocks(cell).strip().replace("\n", " ").replace("|", "\\|")
                cells.append(s)
            rows.append(cells)
        if not rows:
            return ""
        ncol = max(len(r) for r in rows)
        rows = [r + [""] * (ncol - len(r)) for r in rows]
        has_header = b.get("header") == "row"
        lines = []
        if has_header:
            lines.append("| " + " | ".join(rows[0]) + " |")
            lines.append("|" + "---|" * ncol)
            body = rows[1:]
        else:
            lines.append("| " + " | ".join([""] * ncol) + " |")
            lines.append("|" + "---|" * ncol)
            body = rows
        for r in body:
            lines.append("| " + " | ".join(r) + " |")
        return "\n".join(lines) + "\n"

    # ---------- page ----------
    def render(self):
        d = self.doc
        md = d.get("metadata", {})
        cm = md.get("customMetadata", {}) or {}
        title = md.get("title", "")
        url = SITE + d.get("identifier", {}).get("url", "").replace("doc://com.apple.HIG", "")
        url = (SITE + d["identifier"]["url"].split("com.apple.HIG")[-1]).lower() if "identifier" in d else url
        paths = (d.get("hierarchy") or {}).get("paths") or [[]]
        section = ""
        if paths and paths[0]:
            parent = paths[0][-1]
            section = self.refs.get(parent, {}).get("title", "") or parent.rsplit("/", 1)[-1]
        platforms = cm.get("supported-platforms", "")
        alert = cm.get("alert-text", "")
        alert_date = cm.get("alert-date", "")
        abstract = self.inline(d.get("abstract"))

        head = [f"# {title}", ""]
        head.append(f"Source: {url}")
        if section:
            head.append(f"Section: {section}")
        if platforms:
            head.append(f"Platforms: {platforms}")
        if alert:
            head.append(f"Latest change ({alert_date}): {alert}")
        head.append("")
        if abstract:
            head.append(f"> {abstract}")
            head.append("")

        body = []
        for sec in d.get("primaryContentSections", []):
            if sec.get("kind") == "content":
                body.append(self.blocks(sec.get("content")))
        # collection groups list their children in topicSections
        for ts in d.get("topicSections") or []:
            if ts.get("title"):
                body.append(f"\n## {ts['title']}\n")
            for ident in ts.get("identifiers", []):
                r = self.refs.get(ident, {})
                u = r.get("url", "")
                if u.startswith("/"):
                    u = SITE + u
                ab = self.inline(r.get("abstract"))
                body.append(f"- [{r.get('title', ident)}]({u})" + (f" — {ab}" if ab else ""))
            body.append("")

        text = "\n".join(head) + "\n" + "\n".join(body)
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        return {
            "title": title, "url": url, "section": section, "platforms": platforms,
            "alert": alert, "alert_date": alert_date, "abstract": abstract,
            "role": md.get("role"), "words": len(text.split()),
        }, text


index = []
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".json") or fn.startswith("_"):
        continue
    with open(os.path.join(SRC, fn)) as fh:
        doc = json.load(fh)
    meta, text = Page(doc).render()
    slug = fn[:-5]
    meta["slug"] = slug
    with open(os.path.join(OUT, slug + ".md"), "w") as fh:
        fh.write(text)
    index.append(meta)

with open(os.path.join(OUT, "_index.json"), "w") as fh:
    json.dump(index, fh, indent=1)
print(f"rendered {len(index)} pages, total words {sum(m['words'] for m in index)}")
