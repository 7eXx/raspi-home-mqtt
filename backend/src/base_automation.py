import urllib

import requests as req

from abc import ABC, abstractmethod

from src import environment as env
from src.tapo_management import TapoManagement
from raspi_home_texx.automation import Automation


class BaseAutomation(Automation, ABC):

    REQ_TIMEOUT = 5

    def __init__(self, tapo_management: TapoManagement):
        super().__init__()
        self.__tapo_management = tapo_management

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

    def __try_set_home_mode(self) -> bool:
        is_active = self.set_alarm_ecu(state=0)
        if not is_active:
            self.__tapo_management.set_home_mode()

        return is_active

    def __try_set_away_mode(self) -> bool:
        is_active = self.set_alarm_ecu(state=1)
        if is_active:
            self.__tapo_management.set_away_mode()

        return is_active

    def __retry_enable_alarm_ecu(self):
        i = 0
        prev_state = self.is_alarm_ecu_active()
        new_state = self.set_alarm_ecu(state=1)
        while self.is_alarm_ecu_test_mode(prev_state, new_state) and i < 1:
            prev_state = new_state
            new_state = self.set_alarm_ecu(state=1)
            i = i + 1

        return new_state

    def set_home_away_mode(self, **kwargs) -> bool:
        return self.__try_set_away_mode() if bool(int(kwargs['state'])) else self.__try_set_home_mode()

    def home_away_mode_toggle(self, **kwargs) -> bool:
        if not self.is_alarm_ecu_active():
            result = self.set_home_away_mode(state=1)
        else:
            result = self.set_home_away_mode(state=0)

        return result
