import re

result = re.search(r"l.l", "lol")
result = re.search(r"l..l", "lool")
result = re.search(r"l..l", "yooloololo")
result = re.search(r"l..l", "heLLOOL", re.IGNORECASE)

python = "python"
java = "Java"

result = re.search(r"[pP]ython", python)
result = re.search(r"[jJ]ava", java)

print(result)
