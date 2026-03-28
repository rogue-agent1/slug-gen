#!/usr/bin/env python3
"""URL slug generator — clean text into URL-safe slugs."""
import sys, re, unicodedata
def slugify(text, max_len=80):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    text = text.strip("-")[:max_len].rstrip("-")
    return text
def cli():
    if len(sys.argv) < 2: print("Usage: slug_gen <text> [--max N]"); sys.exit(1)
    max_len = 80
    if "--max" in sys.argv: max_len = int(sys.argv[sys.argv.index("--max")+1])
    text = " ".join(a for a in sys.argv[1:] if a != "--max" and not a.isdigit() or a == sys.argv[1])
    print(slugify(text, max_len))
if __name__ == "__main__": cli()
