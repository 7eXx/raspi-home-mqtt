from telegram import KeyboardButton, ReplyKeyboardMarkup

from src.bot_telegram.chat_handler_extended import ChatHandlerExtended
from src.bot_telegram.commands_extended import CommandsExtended


class CustomKeyboardBuilder:
    home_away_toggle_btn = None
    gate_toggle_btn = None

    ecu_check_btn = None
    gate_check_btn = None

    def __init__(self, chat_handler: ChatHandlerExtended):
        self.home_away_toggle_btn = KeyboardButton(CommandsExtended.HOME_AWAY_TOGGLE_EMOJI)
        self.gate_toggle_btn = KeyboardButton(CommandsExtended.GATE_TOGGLE_EMOJI)

        self.ecu_check_btn = KeyboardButton(CommandsExtended.ECU_CHECK_EMOJI)
        self.gate_check_btn = KeyboardButton(CommandsExtended.GATE_CHECK_EMOJI)

    def build(self) -> ReplyKeyboardMarkup:
        keyboard = [
            [self.home_away_toggle_btn, self.gate_toggle_btn],
            [self.ecu_check_btn, self.gate_check_btn]
        ]

        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)