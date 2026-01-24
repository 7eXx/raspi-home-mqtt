import requests
import json

from src import environment as env
from src.bot_telegram.commands_extended import CommandsExtended


def update_bot_commands(token, commands):
    """
    Update Telegram bot commands with descriptions
    """
    url = f"https://api.telegram.org/bot{token}/setMyCommands"

    payload = {
        "commands": json.dumps(commands)
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
        result = response.json()

        if result.get("ok"):
            print("✅ Comands updated successfully!")
        else:
            print(f"❌ Error during update: {result.get('description')}")

    except Exception as e:
        print(f"⚠️ Connection error: {e}")


# Commands definition (max 100)
# 'command' must be lowercase and without '/' at the beginning
commands_extended = CommandsExtended(env.BOT_NAME)
my_commands = []
for command, description in commands_extended.get_descriptions_dict().items():
    my_commands = my_commands + [{"command": command, "description": description}]

if __name__ == "__main__":
    update_bot_commands(env.BOT_TOKEN, my_commands)
