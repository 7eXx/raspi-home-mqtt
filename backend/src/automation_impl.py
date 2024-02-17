
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from raspi_home_texx.system_info import SimpleSystemInfo, SystemInfo
from raspi_home_texx.automation import Automation

from src.pinout import Pinout


class AutomationImpl(Automation):
    def __init__(self):
        self._alarm_pin = DigitalInputDevice(Pinout.SWITCH_ALARM_PIN, True, None, 0.300)
        self._ecu_status_pin = DigitalInputDevice(Pinout.STATUS_ECU_PIN)
        self._gate_status_pin = DigitalInputDevice(Pinout.STATUS_GATE_PIN)

        self._ecu_toggle_pin = DigitalOutputDevice(Pinout.TOGGLE_ECU_PIN, True, False)
        self._gate_switch_pin = DigitalOutputDevice(Pinout.SWITCH_GATE_PIN)
        self._gate_stop_pin = DigitalOutputDevice(Pinout.STOP_GATE_PIN)

        self._alarm_observers = []

    def temperature(self) -> (float, str):
        # retrieve temperature from cpu
        sys_info = SimpleSystemInfo()

        return sys_info.cpu.temperature, sys_info.cpu.unit

    def system_info(self) -> SystemInfo:
        sys_info = SimpleSystemInfo()

        return sys_info
