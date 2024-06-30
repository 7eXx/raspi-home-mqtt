import subprocess

import emoji
from raspi_home_texx.automation import Automation
from raspi_home_texx.bot.chat_handler import ChatHandler
from raspi_home_texx.bot.commands import Commands
from telegram import Update
from telegram.ext import CallbackContext


class ChatHandlerExtended(ChatHandler):

    def __init__(self, commands: Commands, automation: Automation):
        super().__init__(commands, automation)

    def wake_ryzen(self, update: Update, context: CallbackContext):
        self._logger.info("sveglio il ryzen 7 di Marco")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=emoji.emojize("Sveglio il ryzen di Marco :computer_mouse:", use_aliases=True))
        subprocess.run("wakeonlan -i 192.168.0.255 04:D9:F5:21:8E:57",
                       capture_output=True, text=True)
