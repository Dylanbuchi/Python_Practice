import json

data = """
{   "id" : "456d",
    "number" : "1234567",
    "name" : "Bob"
}
"""

info = json.loads(data)
print(info)