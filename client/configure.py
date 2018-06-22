import os, uuid, json
import requests

config_file = os.path.expanduser('~/.mrmark_config.json')
server_url = 'https://mrmark.herokuapp.com/'
# server_url = 'http://localhost:5000'

if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
else:
    config = {}

    print("Let's get you started.")
    config['email_id'] = str(input("Please enter the mail address associated with the Google assistant.\n"))

    # the UUID serves as a unique auth token to send requests.

    print("Created a configuration file for you at {}".format(config_file))
    config['auth_key'] = str(uuid.uuid4()).lower()[:4]

    with open(config_file, 'w') as f:
        json.dump(config, f)

    headers = {'content-type': 'application/json'}
    # sends the configuration to the server so that the communication can begin.
    requests.post(url=server_url+'/config', data=json.dumps(config), headers=headers)

print(json.dumps(config))

