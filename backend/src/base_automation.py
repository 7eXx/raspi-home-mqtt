import requests as req

from abc import ABC

from src import environment as env
from raspi_home_texx.automation import Automation


class BaseAutomation(Automation, ABC):

    REQ_TIMEOUT = 5

    def __init__(self):
        super().__init__()

    def wake_ryzen(self, **kwargs) -> bool:
        wake_ryzen_url = self.__build_jenkins_trigger_job_url(env.WAKE_RYZEN_JOB_URL, env.WAKE_RYZEN_TOKEN)
        response = req.get(wake_ryzen_url,timeout=self.REQ_TIMEOUT)

        return 200 <= response.status_code < 300

    def wake_luigi(self, **kwargs) -> int:
        wake_luigi_lenovo_url = self.__build_jenkins_trigger_job_url(env.WAKE_LUIGI_LENOVO_JOB_URL, env.WAKE_LUIGI_LENOVO_TOKEN)
        response = req.get(wake_luigi_lenovo_url,timeout=self.REQ_TIMEOUT)

        return 200 <= response.status_code < 300

    def __build_jenkins_trigger_job_url(self, url: str, token: str):
        return f"http://{env.JENKINS_USER}:{env.JENKINS_PASS}@{url}?token={token}"
