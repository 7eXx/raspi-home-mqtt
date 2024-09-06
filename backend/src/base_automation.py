import requests as req

from abc import ABC

from src import environment as env
from raspi_home_texx.automation import Automation


class BaseAutomation(Automation, ABC):

    def __init__(self):
        super().__init__()

    def wake_ryzen(self, **kwargs) -> bool:
        wake_ryzen_url = self.__build_wake_ryzen()
        response = req.get(wake_ryzen_url,timeout=5)

        return response.status_code == 200

    def wake_luigi(self, **kwargs) -> int:
        # TODO: To be implemented
        return False

    def __build_wake_ryzen(self):
        return f"{env.JENKINS_USER}:{env.JENKINS_PASS}@{env.WAKE_RYZEN_JOB_URL}?token={env.WAKE_RYZEN_TOKEN}"
