from abc import ABC

from wakeonlan import send_magic_packet

from src import environment
from raspi_home_texx.automation import Automation


class BaseAutomation(Automation, ABC):

    RYZEN_MAC_ADDR = environment.RYZEN_MAC_ADDR
    LUIGI_MAC_ADDR = environment.LUIGI_MAC_ADDR

    def __init__(self):
        super().__init__()

    def wake_ryzen(self, **kwargs) -> int:
        result = -1
        if self.RYZEN_MAC_ADDR != "":
            send_magic_packet(self.RYZEN_MAC_ADDR)
            result = 0

        return result

    def wake_luigi(self, **kwargs) -> int:
        result = -1
        if self.LUIGI_MAC_ADDR != "":
            send_magic_packet(self.LUIGI_MAC_ADDR)
            result = 0

        return result
