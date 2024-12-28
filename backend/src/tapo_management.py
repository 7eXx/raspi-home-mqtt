
from pytapo import Tapo

from src import environment as env

class TapoManagement:

    def __init__(self):
        self.__tapo_c200 = Tapo(env.TAPO_C200_IP, env.TAPO_USERNAME, env.TAPO_PASSWORD)
        self.__tapo_c500 = Tapo(env.TAPO_C500_IP, env.TAPO_USERNAME, env.TAPO_PASSWORD)

    def set_home_mode(self):
        pass

    def set_away_mode(self):
        pass

    def __set_home_mode_c200(self):
        self.__tapo_c200.setMotionDetection(False)
        self.__tapo_c200.setPersonDetection(False)
        self.__tapo_c200.setTamperDetection(False)
        self.__tapo_c200.setAlarm(False)
        self.__tapo_c200.setNotificationsEnabled(False)
        self.__tapo_c200.setPrivacyMode(True)

    def __set_home_mode_c500(self):
        self.__tapo_c500.setMotionDetection(False)
        self.__tapo_c500.setPersonDetection(False)
        self.__tapo_c500.setTamperDetection(False)
        self.__tapo_c500.setAlarm(False)
        self.__tapo_c500.setNotificationsEnabled(False)
        self.__tapo_c500.setPrivacyMode(False)

    def __set_away_mode_c200(self):
        self.__tapo_c200.setMotionDetection(True)
        self.__tapo_c200.setPersonDetection(True)
        self.__tapo_c200.setTamperDetection(True)
        self.__tapo_c200.setAlarm(True)
        self.__tapo_c200.setNotificationsEnabled(True)
        self.__tapo_c200.setPrivacyMode(False)

    def __set_away_mode_c500(self):
        self.__tapo_c500.setMotionDetection(True)
        self.__tapo_c500.setPersonDetection(True)
        self.__tapo_c500.setTamperDetection(True)
        self.__tapo_c500.setAlarm(False)
        self.__tapo_c500.setNotificationsEnabled(True)
        self.__tapo_c500.setPrivacyMode(False)
