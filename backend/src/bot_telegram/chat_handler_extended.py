import subprocess

from raspi_home_texx.automation import Automation
from raspi_home_texx.bot.chat_handler import ChatHandler
from raspi_home_texx.bot.commands import Commands


class ChatHandlerExtended(ChatHandler):

    def __init__(self, commands: Commands, automation: Automation):
        super().__init__(commands, automation)
