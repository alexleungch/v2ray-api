import json

data = {
         "id":'97ecc095-d518-4b15-a4e4-906fa4f49bcb',
         "level": "0",
         "email": "nikhil@geeksforgeeks.org"
        }

temp = json.dumps(data)
print(temp)

x = '''
{
  "clients": [
    {
      "id": "27848739-7e62-4138-9fd3-098a63964b6b",
      "level": 0,
      "alterId": 4,
      "email": "love@v2ray.com"
    }
  ],
  "default": {
    "level": 0,
    "alterId": 4
  },
  "detour": {
    "to": "tag_to_detour"
  },
  "disableInsecureEncryption": false
}
'''

k = json.loads(x)

b = k['clients']
b.append(temp)

print(k)
print(b)
