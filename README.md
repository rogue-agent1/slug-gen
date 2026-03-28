# slug-gen
Generate URL-friendly slugs from text. Handles Unicode, custom separators. Zero dependencies.
## Usage
```
python3 slug_gen.py "Hello World! Über Cool"
# hello-world-uber-cool
echo "My Blog Post Title" | python3 slug_gen.py --sep _ --max 20
```
