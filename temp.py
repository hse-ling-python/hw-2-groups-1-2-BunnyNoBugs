with open('mystem_tags.csv', encoding='utf-8') as f:
    text = f.readlines()

s = {}
for line in text:
    s[line.split(';')[0]] = line.split(';')[1]

print(s)

import json

with open('mystem_tags.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(s, ensure_ascii=False, indent=4))