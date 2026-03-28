#!/usr/bin/env python3
"""slug_gen - Generate URL-friendly slugs from text."""
import sys, re, unicodedata

def slugify(text, sep="-", max_len=80):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", sep, text).strip(sep)
    return text[:max_len].rstrip(sep)

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: slug_gen <text>"); sys.exit(1)
    print(slugify(" ".join(sys.argv[1:])))
