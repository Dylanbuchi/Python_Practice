import json
import urllib.request

url = "http://py4e-data.dr-chuck.net/comments_697177.json"
print('Retrieved', url)

url_handle = urllib.request.urlopen(url)
url_data = url_handle.read()
print('Retrieved', len(url_data))

data = json.loads(url_data)

result = []
for key in data['comments']:
    num = int(key['count'])
    result.append(num)

print('Count:', len(result))
print('Sum:', sum(result))