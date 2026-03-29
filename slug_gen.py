#!/usr/bin/env python3
"""URL slug generator."""
import re, unicodedata

TRANS = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "ñ": "n", "ø": "o",
         "å": "a", "æ": "ae", "þ": "th", "ð": "d", "ł": "l", "đ": "d"}

def slugify(text: str, max_length: int = 80, separator: str = "-") -> str:
    text = text.lower()
    for k, v in TRANS.items():
        text = text.replace(k, v)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", separator, text).strip(separator)
    if max_length:
        text = text[:max_length].rstrip(separator)
    return text

def unique_slug(text: str, existing: set, max_length: int = 80) -> str:
    base = slugify(text, max_length)
    if base not in existing:
        return base
    for i in range(2, 1000):
        candidate = f"{base}-{i}"
        if candidate not in existing:
            return candidate
    return f"{base}-{id(text)}"

if __name__ == "__main__":
    import sys
    text = " ".join(sys.argv[1:]) or "Hello World! This is a Test"
    print(slugify(text))

def test():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("  Lots   of   spaces  ") == "lots-of-spaces"
    assert slugify("Special $#@! chars") == "special-chars"
    assert slugify("über cool") == "ueber-cool"
    assert slugify("café latte") == "cafe-latte"
    assert slugify("A" * 100, max_length=10) == "a" * 10
    assert slugify("test", separator="_") == "test"
    # Unique
    existing = {"hello-world"}
    assert unique_slug("Hello World", existing) == "hello-world-2"
    assert unique_slug("New Post", existing) == "new-post"
    print("  slug_gen: ALL TESTS PASSED")
