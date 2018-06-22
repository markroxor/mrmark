## Mr. Mark (ALPHA)
A personal customisable assistant integrated with Google assistant for controlling your machines remotely via voice commands to Google Assistant.

<div style="width:100%;text-align:center;">
<a href="https://youtu.be/fpcKOGSSiQc" target="_blank"><img src="https://raw.githubusercontent.com/markroxor/mrmark/master/client/thumb.png" width="450" alt="alt text"/></a>
</div>

Current functionalities include -
- [x] Invoking any keystroke including hotkeys.
- [x] Launching/closing any app.
- [x] Complete media support.
- [x] Vocal typing.
- [x] Remote sleep.

It can do anything you can do using your keystrokes.


### Usage - 
While in `client/` directory execute.
1. `pip install requirements.txt`
2. `python app.py`
3. In a new terminal give the executable permissions by `chmod +x port_forwarding.sh`
4. Run the port forwarding shell script `./port_forwarding.sh`.


Directory structure.
.
├── app.py - Heroku app for db handling and scaling GET POST request.
├── client - client side code.
│   ├── app.py - The local server where
│   ├── configure.py - Create machine authentication, saves it in `~/.mrmark_config.json` and send a copy to the cloud server.
│   ├── Dockerfile - Configuration for creating docker images. (EXPERIMENTAL)
│   ├── key_mapping.json - Key mapping as per user's preference. User can edit it according to their local configuration.
│   ├── port_forwarding.sh - Script for exposing the localhost to the internet.
│   ├── readme.md - Usage instructions.
│   ├── requirements.txt - Python dependencies.
│   └── supervisord.conf - The configuration for servers with supervisord. (EXPERIMENTAL)

├── Procfile - Heroku configuration.
├── readme.md - Usage instructions.
└── requirements.txt - Server side dependencies.
