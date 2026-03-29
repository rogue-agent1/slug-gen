#!/usr/bin/env python3
"""slug_gen - Generate URL-safe slugs."""
import sys, argparse, json, re, unicodedata

def slugify(text, separator="-", max_length=0):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", separator, text)
    text = text.strip(separator)
    if max_length > 0: text = text[:max_length].rstrip(separator)
    return text

def main():
    p = argparse.ArgumentParser(description="Slug generator")
    p.add_argument("text", nargs="+")
    p.add_argument("--sep", default="-")
    p.add_argument("--max-length", type=int, default=0)
    args = p.parse_args()
    results = []
    for t in args.text:
        slug = slugify(t, args.sep, args.max_length)
        results.append({"input": t, "slug": slug, "length": len(slug)})
    print(json.dumps({"slugs": results}, indent=2))

if __name__ == "__main__": main()
