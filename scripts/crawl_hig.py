#!/usr/bin/env python3
"""BFS crawl of Apple HIG DocC JSON pages.

Seeds from the HIG root; follows every doc://com.apple.HIG reference whose url
starts with /design/human-interface-guidelines/. Saves one JSON per page.
"""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
BASE = "https://developer.apple.com/tutorials/data"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/129.0 Safari/537.36")
PREFIX = "/design/human-interface-guidelines"


def fetch(path):
    """path like /design/human-interface-guidelines/color -> json dict or None"""
    url = BASE + path + ".json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa
            if attempt == 2:
                print(f"FAIL {path}: {e}", file=sys.stderr)
                return None
            time.sleep(1.5 * (attempt + 1))


def slug_of(path):
    s = path[len(PREFIX):].strip("/")
    return s.replace("/", "__") or "ROOT"


def extract_links(doc):
    links = set()
    for key, ref in doc.get("references", {}).items():
        url = ref.get("url") or ""
        if key.startswith("doc://com.apple.HIG") and url.startswith(PREFIX):
            # strip fragments
            links.add(url.split("#")[0].rstrip("/"))
    return links


seen = set()
queue = [PREFIX]
seen.add(PREFIX)
done = {}

while queue:
    batch, queue = queue[:8], queue[8:]
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch, p): p for p in batch}
        for f in as_completed(futs):
            p = futs[f]
            doc = f.result()
            if doc is None:
                done[p] = None
                continue
            with open(os.path.join(OUT, slug_of(p) + ".json"), "w") as fh:
                json.dump(doc, fh)
            done[p] = doc.get("metadata", {}).get("title")
            for l in extract_links(doc):
                if l not in seen:
                    seen.add(l)
                    queue.append(l)
    print(f"fetched {len(done)} / discovered {len(seen)}", file=sys.stderr)
    time.sleep(0.3)

with open(os.path.join(OUT, "_pages.json"), "w") as fh:
    json.dump(done, fh, indent=1, sort_keys=True)
print(f"TOTAL pages: {len(done)}; failed: {sum(1 for v in done.values() if v is None)}")
