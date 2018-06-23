import os, json
import requests
from random import randint

config_file = os.path.expanduser('~/.mrmark_config.json')
server_url = 'https://mrmark.herokuapp.com/'
# server_url = 'http://localhost:5000'

if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
else:
    config = {}

    # the UUID serves as a unique auth token to send requests.
    print("Created a configuration file for you at {}".format(config_file))
    config['auth_tok'] = str(randint(100000, 999999))

    with open(config_file, 'w') as f:
        json.dump(config, f)

    headers = {'content-type': 'application/json'}
    # sends the configuration to the server so that the communication can begin.

    print("sending {} to {}".format(config, server_url))
    requests.post(url=server_url+'/config', data=json.dumps(config), headers=headers)