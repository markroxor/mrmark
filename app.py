import requests
from flask import Flask, request

app = Flask(__name__)

bot_token = '5'

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

def process_message(update):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = "I can hear you!"
    # r = requests.post(get_url("sendMessage"), data=data)

@app.route("/", methods=["POST"])
def process_update():
    if request.method == "POST":
        print('update', request)
        update = request.get_json()
        print(update)
        if "message" in update:
            process_message(update)
        return "ok!", 200
if __name__ == '__main__':
   app.run(debug = True)
