#!/usr/bin/env python3
"""URL slug generator."""
import sys, re, unicodedata

def slugify(text, sep='-'):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', sep, text).strip(sep)

if __name__ == '__main__':
    if len(sys.argv) < 2: print("Usage: slug_gen.py <text>"); sys.exit(1)
    print(slugify(' '.join(sys.argv[1:])))
