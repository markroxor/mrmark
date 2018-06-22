## Mr. Mark (ALPHA)
A personal customisable assistant integrated with Google assistant for controlling your machines remotely via voice commands, making it compatible with _Google Home devices_.

<div style="width:100%;text-align:center;">
<a href="https://youtu.be/fpcKOGSSiQc" target="_blank"><img src="https://raw.githubusercontent.com/markroxor/mrmark/master/client/thumbnail.png" width="450" alt="alt text"/></a>
</div>

Current functionalities include -
- [x] Invoking any keystroke including hotkeys.
- [x] Launching/closing any app.
- [x] Complete media support.
- [x] Vocal typing.
- [ ] Remote sleep.

It can do anything you can do using your keystrokes.


### Usage - 
1. Sign up as a alpha tester - using this [link.](https://assistant.google.com/services/a/uid/000000eac507a9f1)   
While in the `client/` directory execute.
2. Install client side dependencies using -
`pip install requirements.txt`
3. Run the app using -  
`python app.py`
4. To expose the server to the internet - open a new terminal give the executable permissions -  
 `chmod +x port_forwarding.sh`
5. Run the port forwarding shell script   
 `./port_forwarding.sh`.
This will return a authentication token - `auth_tok`.   
6. Open _Google Assistant_ and invoke _Mr. Mark_ as `talk to Mr. Mark`.    
7. Say - `Authenticate me` to Mr. Mark and share this authentication token.   
8. Have fun.



### Directory structure.
.
├── `app.py` - Heroku app for db handling and scaling GET POST request.  
├── `client` - client side code.  
│   ├── `app.py` - The local server where  
│   ├── `configure.py` - Create machine authentication, saves it in `~/.mrmark_config.json` and send a copy to the cloud server.  
│   ├── `Dockerfile` - Configuration for creating docker images. (EXPERIMENTAL)  
│   ├── `key_mapping.json` - Key mapping as per user's preference. User can edit it according to their local configuration.  
│   ├── `port_forwarding.sh` - Script for exposing the localhost to the internet.  
│   ├── `readme.md` - Usage instructions.  
│   ├── `requirements.txt` - Python dependencies.  
│   └── `supervisord.conf` - The configuration for servers with supervisord. (EXPERIMENTAL)  
  
├── `Procfile` - Heroku configuration.  
├── `readme.md` - Usage instructions.  
└── `requirements.txt` - Server side dependencies.  
