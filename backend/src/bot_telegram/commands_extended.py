
from raspi_home_texx.bot.commands import Commands


class CommandsExtended(Commands):
    WAKE_RYZE = "wake_ryzen"

    def __init__(self, name: str):
        super().__init__(name)
        self._add_command(self.WAKE_RYZE, "avvia il ryzen 7 di Marco")

