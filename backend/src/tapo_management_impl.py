import logging
from pytapo import Tapo

from src import environment as env
from src.tapo_management import TapoManagement


class TapoManagementImpl(TapoManagement):

    __tapo_c200: Tapo | None = None
    __tapo_c500: Tapo | None = None

    def __init__(self):
        super().__init__()
        try:
            self.__tapo_c200 = Tapo(env.TAPO_C200_IP, env.TAPO_USERNAME, env.TAPO_PASSWORD)
        except:
            logging.warning("Tapo C200 not reachable")
            self.__tapo_c200 = None

        try:
            self.__tapo_c500 = Tapo(env.TAPO_C500_IP, env.TAPO_USERNAME, env.TAPO_PASSWORD)
        except:
            logging.warning("Tapo C500 not reachable")
            self.__tapo_c500 = None

    def set_home_mode(self):
        if self.__tapo_c200 is not None:
            self.__set_home_mode_c200()
        if self.__tapo_c500 is not None:
            self.__set_home_mode_c500()

    def set_away_mode(self):
        if self.__tapo_c200 is not None:
            self.__set_away_mode_c200()
        if self.__tapo_c500 is not None:
            self.__set_away_mode_c500()

    def __set_home_mode_c200(self):
        if self.__tapo_c200 is None:
            logging.warning("Tapo C200 not reachable")
            return

        self.__tapo_c200.setMotionDetection(False)
        self.__tapo_c200.setPersonDetection(False)
        self.__tapo_c200.setTamperDetection(False)
        self.__tapo_c200.setAlarm(False)
        self.__tapo_c200.setNotificationsEnabled(False)
        self.__tapo_c200.setPrivacyMode(True)

    def __set_home_mode_c500(self):
        if self.__tapo_c500 is None:
            logging.warning("Tapo C500 not reachable")
            return

        self.__tapo_c500.setMotionDetection(False)
        self.__tapo_c500.setPersonDetection(True)
        self.__tapo_c500.setTamperDetection(True)
        self.__tapo_c500.setAlarm(False)
        self.__tapo_c500.setNotificationsEnabled(False)
        self.__tapo_c500.setPrivacyMode(False)

    def __set_away_mode_c200(self):
        if self.__tapo_c200 is None:
            logging.warning("Tapo C200 not reachable")
            return

        self.__tapo_c200.setMotionDetection(True)
        self.__tapo_c200.setPersonDetection(True)
        self.__tapo_c200.setTamperDetection(True)
        self.__tapo_c200.setAlarm(True)
        self.__tapo_c200.setNotificationsEnabled(True)
        self.__tapo_c200.setPrivacyMode(False)

    def __set_away_mode_c500(self):
        if self.__tapo_c500 is None:
            logging.warning("Tapo C500 not reachable")
            return

        self.__tapo_c500.setMotionDetection(False)
        self.__tapo_c500.setPersonDetection(True)
        self.__tapo_c500.setTamperDetection(True)
        self.__tapo_c500.setAlarm(False)
        self.__tapo_c500.setNotificationsEnabled(True)
        self.__tapo_c500.setPrivacyMode(False)
