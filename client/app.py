import requests
from flask import Flask, request, jsonify
import json
import pyautogui
import time

app = Flask(__name__)

def take_action(data):
    query = data['queryResult']['queryText']
    parameters = data['queryResult']['parameters']
    action = data['queryResult']['action']
    
    print(query)
    print(parameters)

    with open("key_mapping.json") as km:
        key_map = json.load(km)

    if action == 'open_app':
        print(parameters['app'])
        pyautogui.press('apps')
        time.sleep(1)
        pyautogui.typewrite(parameters['app'])
        pyautogui.press('enter')

    elif action == 'keystroke':
        keystroke = str(parameters['keystroke']).lower()
        print(keystroke)

        if len(keystroke.split(' ')) > 1:
            pyautogui.hotkey(*keystroke.split(' '))
        else:
            if keystroke in key_map:
                keystroke = key_map[keystroke]
            
            print("Pressing {}".format(keystroke))
            pyautogui.press(keystroke)

            # if keystroke == 'play' or keystroke == 'pause':
            #     pyautogui.press('f7')
            # elif keystroke == 'volumeup':
            #     pyautogui.press('f10')
            # elif keystroke == 'volumedown':
            #     pyautogui.press('f9')
            # else:
            #     pyautogui.press(keystroke)

    elif action == 'type':
        text = str(parameters['any']).lower()
        pyautogui.typewrite(text)


@app.route("/", methods=["POST", "GET"])
def process_update():
    if request.method == "POST":
        json_request = request.get_json()
        print(json_request)
        print(json_request['session'])#['userId'])
        if json_request['queryResult']['action'] == 'input.unknown':
            with open("unresponsed_queries.txt", 'a') as js:
                js.write(json.dumps(json_request['queryResult']['queryText']) + '\n')
        else:
            take_action(json_request)
   
        return "ok got your post!", 200
        
    if request.method == "GET":
        return "ok GOT it", 200

if __name__ == '__main__':
    app.run(debug = True, port = 7777)
