import re
import json
import requests

# r = requests.get("http://httpbin.org/json")
# print(r.json())

r = requests.post("http://api.wolframalpha.com/v2/query", data={
    'appid':'VU8KTY-XE5EKU7L24',
    'input':'65 million people',
    'output':'json'})
info = []
query = r.json()['queryresult']
for pod_number in range(0,query['numpods']):
    info.append({'title':query['pods'][pod_number]['title'],
     'info':[{'src':x['img']['src'], 'alt':x['img']['alt']} for x in query['pods'][pod_number]['subpods']]})
print(json.dumps(info))
# print(json.dumps(r.json()))
