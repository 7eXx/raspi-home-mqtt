from typing import List, overload

from raspi_home_texx.automation import Automation
from raspi_home_texx.bot.commands import Commands, CommandCallback
from raspi_home_texx.bot_telegram import AbstractBotTelegramBuilder
from telegram import ReplyKeyboardMarkup

from src.bot_telegram.commands_extended import CommandsExtended
from src.bot_telegram.chat_handler_extended import ChatHandlerExtended
from src.bot_telegram.chat_filter_extended import ChatFilterExtended
from src.bot_telegram.custom_keyboard_builder import CustomKeyboardBuilder


class BotTelegramBuilder(AbstractBotTelegramBuilder):

    def __init__(self):
        super().__init__()

    def create_custom_keyboard(self, chat_handler: ChatHandlerExtended) -> ReplyKeyboardMarkup:
        return CustomKeyboardBuilder(chat_handler).build()

    def create_commands(self, name: str) -> CommandsExtended:
        return CommandsExtended(name)

    def create_handler(self, commands: Commands, automation: Automation) -> ChatHandlerExtended:
        return ChatHandlerExtended(commands, automation)

    def create_chat_filter(self, list_id: List[int]) -> ChatFilterExtended:
        return ChatFilterExtended(list_id)

    def create_command_callbacks(self, commands: CommandsExtended, chat_handler: ChatHandlerExtended) -> list[
        CommandCallback]:
        return [
            CommandCallback(commands.HOME_MODE, chat_handler.home_mode),
            CommandCallback(commands.AWAY_MODE, chat_handler.away_mode),
            CommandCallback(commands.HOME_AWAY_TOGGLE, chat_handler.home_away_toggle),
            CommandCallback(commands.ENVIRONMENT_INFO, chat_handler.environment_info),
            CommandCallback(commands.WAKE_RYZE, chat_handler.wake_ryzen),
            CommandCallback(commands.WAKE_LUIGI, chat_handler.wake_luigi),
        ]
