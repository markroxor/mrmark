import requests
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

bot_token = '5'

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

def process_message(update):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = "I can hear you!"
    # r = requests.post(get_url("sendMessage"), data=data)

@app.route("/", methods=["POST", "GET"])
def process_update():
    if request.method == "POST":
        print('update', request)
        json_request = request.get_json()

        with open("last_req.json", 'w') as js:
            js.write(json.dumps(json_request))

        print(json_request)
        return "ok got your post!", 200
        
    if request.method == "GET":
        # return "ok got it!", 200
        with open("last_req.json") as js:
            a = json.load(js)
        return jsonify(a)

if __name__ == '__main__':
   app.run(debug = True)
