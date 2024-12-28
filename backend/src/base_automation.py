import urllib

import requests as req

from abc import ABC, abstractmethod

from src import environment as env
from src.tapo_management import TapoManagement
from raspi_home_texx.automation import Automation


class BaseAutomation(Automation, ABC):

    REQ_TIMEOUT = 5

    def __init__(self):
        super().__init__()
        self.__tapo_management = TapoManagement()

    def wake_ryzen(self, **kwargs) -> bool:
        wake_ryzen_url = self.__build_trigger_job_url(env.RYZEN_MAC_ADDR)
        response = req.get(wake_ryzen_url,timeout=self.REQ_TIMEOUT)

        return 200 <= response.status_code < 300

    def wake_luigi(self, **kwargs) -> int:
        wake_luigi_lenovo_url = self.__build_trigger_job_url(env.LUIGI_LENOVO_MAC_ADDR)
        response = req.get(wake_luigi_lenovo_url,timeout=self.REQ_TIMEOUT)

        return 200 <= response.status_code < 300

    def __build_trigger_job_url(self, mac_addr: str):
        params = {
            "token": env.WAKE_LAN_TOKEN,
            "MAC_ADDRESS": mac_addr
        }
        url = f"http://{env.JENKINS_USER}:{env.JENKINS_PASS}@{env.WAKE_LAN_JOB_URL}"
        url += f"?{urllib.parse.urlencode(params)}"

        return url

    def set_home_mode(self):
        self.set_alarm_ecu(state=0)
        self.__tapo_management.set_home_mode()

        return self.is_alarm_ecu_active()

    def set_away_mode(self):
        self.__retry_enable_alarm_ecu()
        self.__tapo_management.set_away_mode()

        return self.is_alarm_ecu_active()

    def __retry_enable_alarm_ecu(self):
        i = 0
        while not self.is_alarm_ecu_active() and i < 3:
            self.set_alarm_ecu(state=1)
            i = i + 1

    def home_away_mode_toggle(self):
        is_enable = self.is_alarm_ecu_active()
        if not is_enable:
            result = self.set_away_mode()
        else:
            result = self.set_home_mode()

        return result