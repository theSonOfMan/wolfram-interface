import json
import requests

from django.shortcuts import render


def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def result_view(request, *args, **kwargs):
    print(request.POST)
    r = requests.post("http://api.wolframalpha.com/v2/query", data={
        'appid':'VU8KTY-XE5EKU7L24',
        'input':request.POST['input'],
        'output':'json'})
    info = []
    query = r.json()['queryresult']
    for pod_number in range(0,query['numpods']):
        info.append({'title':query['pods'][pod_number]['title'],
         'info':[{'src':x['img']['src'], 'alt':x['img']['alt']} for x in query['pods'][pod_number]['subpods']]})
    print(info)
    return render(request, "result.html", {'info':info})
# Create your views here.
