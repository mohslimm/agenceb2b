import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace all pitch-boxes
content = re.sub(r'\s*<div class="pitch-box">.*?</div>\s*</div>', '\n', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
