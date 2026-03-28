#!/usr/bin/env python3
"""slug_gen - Generate URL-friendly slugs from text."""
import sys, re, unicodedata

def slugify(text, sep='-', lower=True, max_len=0):
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode()
    if lower: text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', sep, text).strip(sep)
    if max_len: text = text[:max_len].rstrip(sep)
    return text

def main():
    args = sys.argv[1:]
    sep, lower, max_len = '-', True, 0
    texts = []
    i = 0
    while i < len(args):
        if args[i] in ('-h','--help'):
            print("Usage: slug_gen.py TEXT [...] [--sep _] [--no-lower] [--max N]"); return
        elif args[i] == '--sep': i+=1; sep = args[i]
        elif args[i] == '--no-lower': lower = False
        elif args[i] == '--max': i+=1; max_len = int(args[i])
        else: texts.append(args[i])
        i += 1
    if not texts:
        texts = [line.strip() for line in sys.stdin if line.strip()]
    for t in texts:
        print(slugify(t, sep, lower, max_len))

if __name__ == '__main__': main()
