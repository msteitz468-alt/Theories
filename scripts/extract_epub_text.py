#!/usr/bin/env python3
"""Extract plain text from an epub file."""
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup


def strip_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    text = soup.get_text("\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def get_spine_order(z: zipfile.ZipFile) -> list[str]:
    opf_path = None
    for name in z.namelist():
        if name.endswith(".opf"):
            opf_path = name
            break
    if not opf_path:
        return []

    root = ET.fromstring(z.read(opf_path))
    ns = {"opf": "http://www.idpf.org/2007/opf"}
    manifest = {
        item.get("id"): item.get("href")
        for item in root.findall(".//opf:manifest/opf:item", ns)
    }
    base = str(Path(opf_path).parent)

    spine = []
    for itemref in root.findall(".//opf:spine/opf:itemref", ns):
        href = manifest.get(itemref.get("idref"))
        if href:
            spine.append(f"{base}/{href}" if base != "." else href)
    return spine


def extract_epub(epub_path: Path) -> str:
    parts = []
    with zipfile.ZipFile(epub_path) as z:
        spine = get_spine_order(z)
        names = set(z.namelist())
        for href in spine:
            # normalize path
            candidate = href.replace("\\", "/")
            if candidate not in names:
                # try basename match
                matches = [n for n in names if n.endswith(Path(candidate).name)]
                if not matches:
                    continue
                candidate = matches[0]
            raw = z.read(candidate).decode("utf-8", errors="replace")
            if candidate.endswith((".html", ".xhtml", ".htm", ".xml")):
                parts.append(strip_html(raw))
    return "\n\n".join(parts)


def main():
    epub = Path(sys.argv[1]).expanduser().resolve()
    out = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) > 2 else None
    text = extract_epub(epub)
    if out:
        out.write_text(text, encoding="utf-8")
        print(f"Wrote {len(text)} chars to {out}")
    else:
        print(text[:5000])


if __name__ == "__main__":
    main()
