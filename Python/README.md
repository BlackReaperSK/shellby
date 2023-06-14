<div align="center">

#  Pegasus Discord C2 🦄

</div>

<div align="center">

[![Discord](https://img.shields.io/badge/discord-bot-blue.svg)](https://discord.com/)
[![Python](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

</div>

## ✨ Introduction

This project is a fork/modification of original project [Pegasus C2](https://github.com/LonelyIDA/Pegasus-C2). Pegasus is a versatile Discord C2 that allows you to perform various commands and actions right from your Discord server. With Pegasus, you can execute commands, manage files, and interact with your system using simple Discord messages.

## 🚀 Features

- Execute command prompt commands directly from Discord
- Navigate and explore directories on your system
- Download files from the internet or upload files to Discord
- Run local files or scripts 

## 📝 Prerequisites

- Python 3.8 or higher
- Discord.py library
- Requests library
- dotenv library
- An active Discord bot token

## ⚙️ Configuration

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies.
3. Change var `guid_id` with your guild_id
4. Insert your Bot Token in last line

## 🏃‍♀️ Usage

1. Invite the Pegasus bot to your Discord server.
2. Run the script using `python pegasus.py` or your preferred method.
3. The bot will automatically create a text channel for each session and provide a unique session ID.
4. Use the commands available to interact with the bot and perform various actions.

## 📚 Available Commands

- `help` - Get a list of available commands and their usage.
- `ping` - Check the bot's latency.
- `cd <directory>` - Change the current working directory.
- `ls` - List files and directories in the current directory.
- `download <file>` - Download a file from the internet.
- `upload <link>` - Upload a file to Discord from a given link.
- `cmd <command>` - Execute a command prompt command.
- `run <file>` - Execute a local file or script.
- `startup` - (Linux Only) Add the bot to startup on system boot.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/BlackReaperSK/shellby/issues).
---

<div align="center">
Made with ❤️ by BlackReaperSK
</div>

