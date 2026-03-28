#!/usr/bin/env python3
"""slug_gen - Generate URL-safe slugs from text."""
import sys, re, unicodedata
def slugify(text, sep="-", max_len=200):
    text = unicodedata.normalize("NFKD", text).encode("ascii","ignore").decode()
    text = text.lower(); text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", sep, text).strip(sep)
    return text[:max_len]
if __name__ == "__main__":
    if len(sys.argv) < 2: text = sys.stdin.read().strip()
    else: text = " ".join(sys.argv[1:])
    print(slugify(text))
