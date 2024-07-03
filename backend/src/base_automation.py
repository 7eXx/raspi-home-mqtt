import subprocess
from abc import ABC
from src import environment
from raspi_home_texx.automation import Automation


class BaseAutomation(Automation, ABC):

    RYZEN_MAC_ADDR = environment.RYZEN_MAC_ADDR

    def __init__(self):
        super().__init__()

    def wake_ryzen(self, **kwargs) -> int:
        if self.RYZEN_MAC_ADDR != "":
            result = subprocess.call(f"wakeonlan {self.RYZEN_MAC_ADDR}", shell=True)
        else:
            result = -1

        return result
