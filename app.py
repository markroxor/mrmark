import requests
from flask import Flask, request, jsonify
import json
import time

username = 'mrmohitrathoremr'
config_file = 'conf.json'

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def process_df_api():

    # get dialog-flow's POST request and send a POST request to the client side.
    if request.method == "POST":
        r = "GOT a DF API POST request."
        json_request = request.get_json()
        print(json_request)

        with open(config_file) as f:
            confs = json.load(f)

        auth_token = confs[username]['auth_token']

        if json_request['queryResult']['action'] == 'input.unknown':
            with open("unresponsed_queries.txt", 'a') as js:
                js.write(json.dumps(json_request['queryResult']['queryText']) + '\n')
        else:
            url = 'https://'+auth_token+'.serveo.net'
            headers = {'content-type': 'application/json'}

            resp = requests.post(url=url, data=json.dumps(json_request), headers=headers)
            print("response", resp.text)
            r = resp.text

        return r, 200
        
    if request.method == "GET":
        return "Heroku GOT a request", 200

@app.route("/config", methods=["POST"])
def process_config():

    # saves the POSTED user configuration in conf folder
    if request.method == "POST":
        print(request, "request")
        conf = request.get_json()
        print(conf)

        with open(config_file) as f:
            confs = json.load(f)

        username = conf['email_id'].split('@gmail.com')[0] 
        confs[username] = conf

        with open(config_file, 'w') as f:
            json.dump(confs, f)
        
        return "saved the new configuration", 200

if __name__ == '__main__':
    app.run(debug = True)