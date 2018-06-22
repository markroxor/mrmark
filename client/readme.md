## Mr. Mark (ALPHA)
A personal customisable assistant integrated with Google assistant for controlling your machines remotely via voice commands to Google Assistant.

Current functionalities include -
- [x] Invoking any keystroke including hotkeys.
- [x] Launching/closing any app.
- [x] Complete media support.
- [x] Vocal typing.
- [x] Remote sleep.

It can do anything you can do using your keystrokes.
.
├── app.py - The local server where
├── configure.py - Create machine authentication, saves it in `~/.mrmark_config.json` and send a copy to the cloud server.
├── Dockerfile - Configuration for creating docker images. (EXPERIMENTAL)
├── key_mapping.json - Key mapping as per user's preference. User can edit it according to their local configuration.
├── port_forwarding.sh - Script for exposing the localhost to the internet.
├── readme.md - Instructions.
├── requirements.txt - Python dependencies.
└── supervisord.conf - The configuration for servers with supervisord. (EXPERIMENTAL)