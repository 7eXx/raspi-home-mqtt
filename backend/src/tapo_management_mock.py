
from typing_extensions import override

from src.tapo_management import TapoManagement


class TapoManagementMock(TapoManagement):

    def __init__(self):
        super().__init__()

    @override
    def set_home_mode(self):
        pass

    @override
    def set_away_mode(self):
        pass
