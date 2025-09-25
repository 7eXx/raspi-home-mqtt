import emoji
from raspi_home_texx.bot.commands import Commands


class CommandsExtended(Commands):
    HOME_MODE = "home_mode"
    AWAY_MODE = "away_mode"
    HOME_AWAY_TOGGLE = "home_away_toggle"
    ENVIRONMENT_INFO = "environment_info"
    WAKE_RYZE = "wake_ryzen"
    WAKE_LUIGI = "wake_luigi_lenovo"

    ## emojized commands
    HOME_AWAY_TOGGLE_EMOJI = emoji.emojize("Home/Away toggle :house:", use_aliases=True)
    ECU_CHECK_EMOJI = emoji.emojize("Home check :house::red_question_mark:", use_aliases=True)
    GATE_TOGGLE_EMOJI = emoji.emojize("Gate toggle :door:", use_aliases=True)
    GATE_CHECK_EMOJI = emoji.emojize("Gate check :door::red_question_mark:", use_aliases=True)

    def __init__(self, name: str):
        super().__init__(name)
        self._add_command(self.HOME_MODE, "imposta la modalità casa")
        self._add_command(self.AWAY_MODE, "imposta la modalità via")
        self._add_command(self.HOME_AWAY_TOGGLE, "alterna tra modalità casa e via")
        self._add_command(self.ENVIRONMENT_INFO, "informazioni sull'ambiente")
        self._add_command(self.WAKE_RYZE, "avvia il ryzen 7 di Marco")
        self._add_command(self.WAKE_LUIGI, "avvia il lenovo di Luigi")
