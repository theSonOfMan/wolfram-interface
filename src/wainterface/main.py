import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index_view():
	return render_template('index.html')
    # return render(request, "index.html", {})

@app.route('/result/', methods = ['POST'])
def result_view():
    params = request.form
    info = []
    # print(request.POST)
    r = requests.post("http://api.wolframalpha.com/v2/query", data={
        'appid':'VU8KTY-XE5EKU7L24',
        'input': params['input'],
        'units': params['metricRadio'],
        'podstate':'Step-by-step solution',
        'format':'image',
        'output':'json'})
    # print(r.json())x
    if  params['rawRadio'] == 'true':
        info.append({'title':"Raw output", 'output':json.dumps(r.json(), sort_keys=True, indent=4)})
    else:
        # print(r.json())
        query = r.json()['queryresult']
        for pod_number in range(0,query['numpods']):
            info.append({'title':query['pods'][pod_number]['title'],
             'info':[{'title':x['title'],'src':x['img']['src'], 'alt':x['img']['alt']} for x in query['pods'][pod_number]['subpods']]})
        # print(info)
    return render_template("result.html", info = info)