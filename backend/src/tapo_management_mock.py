
from src.tapo_management import TapoManagement


class TapoManagementMock(TapoManagement):

    def __init__(self):
        super().__init__()

    def set_home_mode(self):
        pass

    def set_away_mode(self):
        pass
