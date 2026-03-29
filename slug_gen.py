import sys, re, argparse, unicodedata

def slugify(text, sep="-", lower=True, max_len=0):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    if lower: text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", sep, text).strip(sep)
    if max_len > 0: text = text[:max_len].rstrip(sep)
    return text

def main():
    p = argparse.ArgumentParser(description="URL slug generator")
    p.add_argument("text", nargs="*")
    p.add_argument("-s", "--separator", default="-")
    p.add_argument("-m", "--max-length", type=int, default=0)
    p.add_argument("--no-lower", action="store_true")
    args = p.parse_args()
    text = " ".join(args.text) if args.text else sys.stdin.read().strip()
    print(slugify(text, args.separator, not args.no_lower, args.max_length))

if __name__ == "__main__":
    main()
