import requests
import json
import time

from src import environment as env
from src.bot_telegram.commands_extended import CommandsExtended

def __update_commands_with_scope(url, commands, scope_type):
    scope = {
        "type": scope_type
    }
    payload = {
        "commands": json.dumps(commands),
        "scope": json.dumps(scope)
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
        result = response.json()

        if result.get("ok"):
            print(f"✅ Commands updated successfully with scope {scope}!")
        else:
            print(f"❌ Error during update: {result.get('description')}")

    except Exception as e:
        print(f"⚠️ Connection error: {e}")

def update_bot_commands(token, commands, scopes):
    """
    Update Telegram bot commands with descriptions
    """
    url = f"https://api.telegram.org/bot{token}/setMyCommands"

    for scope_type in scopes:
        __update_commands_with_scope(url, commands, scope_type)
        time.sleep(0.5)


# Commands definition (max 100)
# 'command' must be lowercase and without '/' at the beginning
commands_extended = CommandsExtended(env.BOT_NAME)

target_scopes = [
    "default",
    "all_private_chats",
    "all_group_chats",
    "all_chat_administrators"
]
my_commands = []

for command, description in commands_extended.get_descriptions_dict().items():
    my_commands = my_commands + [{"command": command, "description": description}]

if __name__ == "__main__":
    update_bot_commands(env.BOT_TOKEN, my_commands, target_scopes)
