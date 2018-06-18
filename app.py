import requests
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

def post_request(json_request):
    data = {}
    # r = requests.post('url, data=data)

@app.route("/", methods=["POST", "GET"])
def process_update():
    if request.method == "POST":
        print('update', request)
        json_request = request.get_json()
        
        if json_request['queryResult']['action'] == 'input.unknown':
            with open("unresponsed_queries.json", 'a') as js:
                js.write(json.dumps(json_request))
        else:
            with open("last_req.json", 'w') as js:
                js.write(json.dumps(json_request))

        print(json_request)
        return "ok got your post!", 200
        
    if request.method == "GET":
        with open("last_req.json") as js:
            last_req = json.load(js)
        with open("unresponsed_queries.json") as js:
            unresponsed_queries = json.load(js)

        if request.args['del']:
            print('deleting unresponsed_queries')
            with open("unresponsed_queries.json", 'w') as js:
                js.write(json.dumps({}))
                
        if request.args['urq']:
            print('returning unresponsed_queries content')
            return jsonify(unresponsed_queries)



        return jsonify(last_req)

if __name__ == '__main__':
   app.run(debug = True)
