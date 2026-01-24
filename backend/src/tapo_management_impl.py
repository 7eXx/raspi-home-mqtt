from typing import Optional

from pytapo import Tapo
from raspi_home_texx import get_console_logger

from src import environment as env
from src.tapo_management import TapoManagement


class TapoManagementImpl(TapoManagement):

    __tapo_c200: Optional[Tapo] = None
    __tapo_c500: Optional[Tapo] = None

    def __init__(self):
        super().__init__()
        self.logger = get_console_logger(__name__, env.LOGGING_LEVEL)
        self.__try_initialize_tapo_c200()
        self.__try_initialize_tapo_c500()

    def __try_initialize_tapo_c200(self):
        if self.__tapo_c200 is not None:
            return

        try:
            self.__tapo_c200 = Tapo(env.TAPO_C200_IP, env.TAPO_USERNAME, env.TAPO_PASSWORD)
        except:
            self.logger.warning("Tapo C200 not reachable")
            self.__tapo_c200 = None

    def __try_initialize_tapo_c500(self):
        if self.__tapo_c500 is not None:
            return

        try:
            self.__tapo_c500 = Tapo(env.TAPO_C500_IP, env.TAPO_USERNAME, env.TAPO_PASSWORD)
        except:
            self.logger.warning("Tapo C500 not reachable")
            self.__tapo_c500 = None

    def set_home_mode(self):
        self.set_home_mode_c200()
        self.set_home_mode_c500()

    def set_away_mode(self):
        self.set_away_mode_c200()
        self.set_away_mode_c500()

    def set_home_mode_c200(self) -> bool:
        self.__try_initialize_tapo_c200()
        if self.__tapo_c200 is None:
            return False

        try:
            self.__tapo_c200.setMotionDetection(False)
            self.__tapo_c200.setPersonDetection(False)
            self.__tapo_c200.setTamperDetection(False)
            self.__tapo_c200.setAlarm(False)
            self.__tapo_c200.setNotificationsEnabled(False)
            self.__tapo_c200.setPrivacyMode(True)
            return True
        except:
            self.logger.warning("Tapo C200 unable to set home mode")
            return False

    def set_away_mode_c200(self):
        self.__try_initialize_tapo_c200()
        if self.__tapo_c200 is None:
            return False

        try:
            self.__tapo_c200.setMotionDetection(True)
            self.__tapo_c200.setPersonDetection(True)
            self.__tapo_c200.setTamperDetection(True)
            self.__tapo_c200.setAlarm(True)
            self.__tapo_c200.setNotificationsEnabled(True)
            self.__tapo_c200.setPrivacyMode(False)
            return True
        except:
            self.logger.warning("Tapo C200 unable to set away mode")
            return False

    def set_home_mode_c500(self):
        self.__try_initialize_tapo_c500()
        if self.__tapo_c500 is None:
            return False

        try:
            self.__tapo_c500.setMotionDetection(False)
            self.__tapo_c500.setPersonDetection(True)
            self.__tapo_c500.setTamperDetection(True)
            self.__tapo_c500.setAlarm(False)
            self.__tapo_c500.setNotificationsEnabled(False)
            self.__tapo_c500.setPrivacyMode(False)
            return True
        except:
            self.logger.warning("Tapo C500 unable to set home mode")
            return False

    def set_away_mode_c500(self):
        self.__try_initialize_tapo_c500()
        if self.__tapo_c500 is None:
            return False

        try:
            self.__tapo_c500.setMotionDetection(False)
            self.__tapo_c500.setPersonDetection(True)
            self.__tapo_c500.setTamperDetection(True)
            self.__tapo_c500.setAlarm(False)
            self.__tapo_c500.setNotificationsEnabled(True)
            self.__tapo_c500.setPrivacyMode(False)
            return True
        except:
            self.logger.warning("Tapo C500 unable to set away mode")
            return False
