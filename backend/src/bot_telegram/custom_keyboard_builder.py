from telegram import KeyboardButton, ReplyKeyboardMarkup

from src.bot_telegram.chat_handler_extended import ChatHandlerExtended


class CustomKeyboardBuilder:
    home_away_mode_toggle_btn = None
    gate_toggle_btn = None

    ecu_check_btn = None
    gate_check_btn = None

    def __init__(self, chat_handler: ChatHandlerExtended):
        self.home_away_mode_toggle_btn = KeyboardButton('/' + chat_handler.home_away_mode_toggle.__name__)
        self.gate_toggle_btn = KeyboardButton('/' + chat_handler.gate_toggle.__name__)

        self.ecu_check_btn = KeyboardButton('/' + chat_handler.ecu_check.__name__)
        self.gate_check_btn = KeyboardButton('/' + chat_handler.gate_check.__name__)

    def build(self) -> ReplyKeyboardMarkup:
        keyboard = [
            [self.home_away_mode_toggle_btn, self.gate_toggle_btn],
            [self.ecu_check_btn, self.gate_check_btn]
        ]

        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)