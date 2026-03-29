#!/usr/bin/env python3
"""URL slug generator. Zero dependencies."""
import re, sys, unicodedata

TRANSLITERATIONS = {
    "ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "à": "a", "á": "a",
    "â": "a", "ã": "a", "è": "e", "é": "e", "ê": "e", "ë": "e",
    "ì": "i", "í": "i", "î": "i", "ï": "i", "ò": "o", "ó": "o",
    "ô": "o", "õ": "o", "ù": "u", "ú": "u", "û": "u", "ñ": "n",
    "ç": "c", "ð": "d", "ø": "o", "å": "a", "æ": "ae", "þ": "th",
}

def slugify(text, separator="-", max_length=0, lowercase=True):
    if lowercase: text = text.lower()
    for k, v in TRANSLITERATIONS.items():
        text = text.replace(k, v)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", separator, text)
    text = text.strip(separator)
    text = re.sub(f"{re.escape(separator)}+", separator, text)
    if max_length and len(text) > max_length:
        text = text[:max_length].rstrip(separator)
    return text

def deslugify(slug, separator="-"):
    return slug.replace(separator, " ").title()

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Slug generator")
    p.add_argument("text", nargs="+")
    p.add_argument("-s", "--separator", default="-")
    p.add_argument("-m", "--max-length", type=int, default=0)
    p.add_argument("--no-lower", action="store_true")
    args = p.parse_args()
    text = " ".join(args.text)
    print(slugify(text, args.separator, args.max_length, not args.no_lower))
