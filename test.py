from slug_gen import slugify, deslugify
assert slugify("Hello World!") == "hello-world"
assert slugify("Über cool stuff") == "ueber-cool-stuff"
assert slugify("  Multiple   Spaces  ") == "multiple-spaces"
assert slugify("Hello", max_length=3) == "hel"
assert deslugify("hello-world") == "Hello World"
print("Slug tests passed")