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
            result = False

        if result:
            mess = emoji.emojize("Sveglio il ryzen di Marco :computer_mouse:", use_aliases=True)
        else:
            mess = emoji.emojize("Il pc non viene risvegliato :cross_mark:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def wake_luigi(self, update: Update, context: CallbackContext):
        self._logger.info("provo a svegliare il lenovo di Luigi")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.wake_luigi()
        else:
            result = False

        if result:
            mess = emoji.emojize("Sveglio il lenovo di Luigi :computer_mouse:", use_aliases=True)
        else:
            mess = emoji.emojize("Il pc non viene risvegliato :cross_mark:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def __build_message_from_ecu_state(self, is_ecu_active: bool) -> str:
        if not is_ecu_active:
            return emoji.emojize("Modalità casa impostata :house:", use_aliases=True)
        else:
            return emoji.emojize("Modalità via impostata :police_car_light:", use_aliases=True)

    def home_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la modalità casa")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.try_set_home_mode()
            mess = self.__build_message_from_ecu_state(result)
        else:
            mess = emoji.emojize("Non riesco ad impostare la modalità casa :cross_mark:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def away_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la modalità via")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.try_set_away_mode()
            mess = self.__build_message_from_ecu_state(result)
        else:
            mess = emoji.emojize("Non riesco ad impostare la modalità via :cross_mark:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def home_away_toggle(self, update: Update, context: CallbackContext):
        self._logger.info("alterno tra modalità casa e via")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.home_away_mode_toggle()
            mess = self.__build_message_from_ecu_state(result)
        else:
            mess = emoji.emojize("Non riesco a cambiare la modalità :cross_mark:", use_aliases=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)