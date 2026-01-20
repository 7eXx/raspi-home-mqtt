from abc import ABC, abstractmethod


class TapoManagement(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def set_home_mode_c200(self):
        pass

    @abstractmethod
    def set_away_mode_c200(self):
        pass

    @abstractmethod
    def set_home_mode_c500(self):
        pass

    @abstractmethod
    def set_away_mode_c500(self):
        pass

    @abstractmethod
    def set_home_mode(self):
        pass

    @abstractmethod
    def set_away_mode(self):
        pass