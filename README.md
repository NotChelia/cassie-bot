<p align="center">
  <img src="https://i.imgur.com/UPfOqLm.jpeg" width="20%" alt="CASSIE-BOT-logo">
</p>
<p align="center">
    <h1 align="center">CASSIE-BOT</h1>
</p>
<p align="center">
    Uses <a href="https://github.com/NotChelia/cassie-bot-scraper-lambda">cassie-bot-scraper-lambda</a>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
</p>

<br>

#####  Table of Contents

- [ Overview](#-overview)
- [ Architecture](#-architecture)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)

---

##  Overview

<code>❯ Cassie bot is a general purpose bot that uses cassie-bot-service and cassie-bot-service-lambda for use as a Discord Bot</code>

---
##  Architecture
<img src="https://i.imgur.com/di6l63h.png" width="80%" alt="CASSIE-BOT-ARCH">

##  Discord Bot Commands

This bot includes a set of commands for administrators to manage update notifications for the server

toggle_updates
Command: <code>!toggle_updates</code>
Description: Toggles the update checking for the server.

Command: <code>!subscribe_role <role></code>
Description: Subscribes a role to update notifications.

unsubscribe_role
Command: <code>!unsubscribe_role <role></code>
Description: Unsubscribes a role from update notifications.

set_channel
Command: <code>!set_channel <channel></code>
Description: Sets the channel where update notifications will be posted.

---

##  Repository Structure

```sh
└── cassie-bot/
    ├── blueprint.md
    ├── bot.py
    ├── cogs
    │   ├── __pycache__
    │   ├── update_commands.py
    │   └── update_notifier.py
    ├── Dockerfile
    ├── entrypoint.sh
    ├── README.md
    ├── requirements.txt
    ├── server_config_manager.py
    └── utils
        ├── __pycache__
        ├── log_decorator.py
        ├── secret_manager.py
        └── sqs_handler.py
```

