import re
import json
import requests

# r = requests.get("http://httpbin.org/json")
# print(r.json())

r = requests.post("http://api.wolframalpha.com/v2/query", data={
    'appid':'VU8KTY-XE5EKU7L24',
    'input':'65 million people',
    'output':'json'})
print(json.dumps(r.json()))
