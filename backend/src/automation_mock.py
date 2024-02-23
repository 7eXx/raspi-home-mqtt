from time import sleep
from raspi_home_texx.automation import Automation
from raspi_home_texx.system_info import SystemInfo, SimpleSystemInfo


class AutomationMock(Automation):

    ALARM_ECU_WAIT_TIME = 0.5
    ALARM_ANTI_PANIC_WAIT_TIME = 2
    GATE_ECU_WAIT_TIME = 0.5
    GATE_STOP_WAIT_TIME = 1

    def __init__(self):
        super().__init__()
        self.__alarm_pin = 1
        self.__ecu_status_pin = 0
        self.__gate_status_pin = 0

        self._alarm_observers = []

    def temperature(self) -> (float, str):
        # retrieve temperature from cpu
        sys_info = SimpleSystemInfo()

        return sys_info.cpu.temperature, sys_info.cpu.unit

    def system_info(self) -> SystemInfo:
        sys_info = SimpleSystemInfo()

        return sys_info

    def is_alarm_ringing(self) -> bool:
        return not self.__alarm_pin

    def is_alarm_ecu_active(self) -> bool:
        return bool(self.__ecu_status_pin)

    def is_gate_open(self) -> bool:
        return bool(self.__gate_status_pin)

    def toggle_alarm_ecu(self, **kwargs) -> bool:
        sleep(AutomationMock.ALARM_ECU_WAIT_TIME)
        self.__ecu_status_pin = int(not self.is_alarm_ecu_active())
        self.__alarm_pin = 1
        return self.is_alarm_ecu_active()

    def anti_panic_mode(self, **kwargs) -> bool:
        sleep(AutomationMock.ALARM_ANTI_PANIC_WAIT_TIME)
        self.__ecu_status_pin = 1
        self.__alarm_pin = 0
        return self.is_alarm_ringing()

    def toggle_gate_ecu(self, **kwargs) -> bool:
        sleep(AutomationMock.GATE_ECU_WAIT_TIME)
        self.__gate_status_pin = int(not self.is_gate_open())
        return self.is_gate_open()

    def stop_gate(self, **kwargs) -> bool:
        sleep(AutomationMock.GATE_STOP_WAIT_TIME)
        return self.is_gate_open()
