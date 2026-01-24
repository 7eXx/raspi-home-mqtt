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

    def __build_message_feature_not_available(self) -> str:
        return emoji.emojize("Funzionalità non disponibile :prohibited:", use_aliases=True)

    def __build_message_from_ecu_state(self, is_ecu_active: bool) -> str:
        if not is_ecu_active:
            return emoji.emojize("Modalità casa impostata :house:", use_aliases=True)
        else:
            return emoji.emojize("Modalità via impostata :police_car_light:", use_aliases=True)

    def __build_message_camera_result_state(self, camera: str, result: bool) -> str:
        if result:
            return emoji.emojize(f"Camera {camera} impostata corrattamente :check_mark_button:", use_aliases=True)
        else:
            return emoji.emojize(f"Camera {camera} impostazione fallita :cross_mark:", use_aliases=True)

    def __build_message_wake_pc_result(self, pc_name: str, result: bool) -> str:
        if result:
            return emoji.emojize(f"Sveglio il PC - '{pc_name}' :computer_mouse:", use_aliases=True)
        else:
            return emoji.emojize(f"Il PC - '{pc_name}' non viene risvegliato :cross_mark:", use_aliases=True)

    def wake_ryzen(self, update: Update, context: CallbackContext):
        self._logger.info("provo a svegliare il ryzen 7 di Marco")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.wake_ryzen()
            mess = self.__build_message_wake_pc_result("Ryzen 7 di Marco", result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def wake_luigi(self, update: Update, context: CallbackContext):
        self._logger.info("provo a svegliare il lenovo di Luigi")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.wake_luigi()
            mess = self.__build_message_wake_pc_result("Lenovo di Luigi", result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def c200_home_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la c200 in modalità casa")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.set_home_away_mode_c200(state=0)
            mess = self.__build_message_camera_result_state("c200", result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def c200_away_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la c200 in modalità via")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.set_home_away_mode_c200(state=1)
            mess = self.__build_message_camera_result_state("c200", result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def c500_home_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la c500 in modalità casa")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.set_home_away_mode_c500(state=0)
            mess = self.__build_message_camera_result_state("c500", result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def c500_away_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la c500 in modalità via")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.set_home_away_mode_c500(state=1)
            mess = self.__build_message_camera_result_state("c500", result)

        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def home_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la modalità casa")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.set_home_away_mode(state=0)
            mess = self.__build_message_from_ecu_state(result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def away_mode(self, update: Update, context: CallbackContext):
        self._logger.info("imposto la modalità via")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.set_home_away_mode(state=1)
            mess = self.__build_message_from_ecu_state(result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def home_away_toggle(self, update: Update, context: CallbackContext):
        self._logger.info("alterno tra modalità casa e via")
        if isinstance(self._automation, BaseAutomation):
            result = self._automation.home_away_mode_toggle()
            mess = self.__build_message_from_ecu_state(result)
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def environment_info(self, update: Update, context: CallbackContext):
        self._logger.info("recupero le informazioni sull'ambiente")
        if isinstance(self._automation, BaseAutomation):
            mess = self.__build_env_message()
        else:
            mess = self.__build_message_feature_not_available()

        context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

    def __build_env_message(self) -> str:
        status = self._automation.environment_info().get_status()
        if status == 'n/a':
            return emoji.emojize("Informazioni ambientali non disponibili :cross_mark:", use_aliases=True, )
        elif status == 'offline':
            offline_since = self._automation.environment_info().get_timestamp()

            return emoji.emojize(f"Sensore offline da {offline_since} :cross_mark:", use_aliases=True)
        else:
            return self._automation.environment_info().format_pretty()
