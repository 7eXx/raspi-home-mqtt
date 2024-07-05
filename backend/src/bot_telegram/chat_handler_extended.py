import emoji

from raspi_home_texx.automation import Automation
from raspi_home_texx.bot.chat_handler import ChatHandler
from raspi_home_texx.bot.commands import Commands
from telegram import Update
from telegram.ext import CallbackContext

from src.base_automation import BaseAutomation


class ChatHandlerExtended(ChatHandler):

    def __init__(self, commands: Commands, automation: Automation):
        super().__init__(commands, automation)

    def wake_ryzen(self, update: Update, context: CallbackContext):
        self._logger.info("provo a svegliare il ryzen 7 di Marco")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.wake_ryzen()
        else:
            result = -1

        if result >= 0:
            mess = emoji.emojize("Sveglio il ryzen di Marco :computer_mouse:", use_aliases=True)
        else:
            mess = emoji.emojize("Il pc non viene risvegliato :computer_mouse:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def wake_luigi(self, update: Update, context: CallbackContext):
        self._logger.info("provo a svegliare il lenovo di Luigi")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.wake_luigi()
        else:
            result = -1

        if result >= 0:
            mess = emoji.emojize("Sveglio il lenovo di Luigi :computer_mouse:", use_aliases=True)
        else:
            mess = emoji.emojize("Il pc non viene risvegliato :computer_mouse:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)