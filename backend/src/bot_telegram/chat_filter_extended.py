from typing import List

from raspi_home_texx.bot.chat_filter import ChatFilter


class ChatFilterExtended(ChatFilter):

    def __init__(self, list_id: List[int]):
        super().__init__(list_id)