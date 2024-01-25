import time
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from system_info_texx.system_info import SimpleSystemInfo, SystemInfo

from src.pinout import Pinout
from src.automation import Automation


class AutomationImpl(Automation):
    def __init__(self):
        self._alarm_pin = DigitalInputDevice(Pinout.SWITCH_ALARM_PIN, True, None, 0.300)
        self._ecu_status_pin = DigitalInputDevice(Pinout.STATUS_ECU_PIN)
        self._gate_status_pin = DigitalInputDevice(Pinout.STATUS_GATE_PIN)

        self._ecu_toggle_pin = DigitalOutputDevice(Pinout.TOGGLE_ECU_PIN, True, False)
        self._gate_switch_pin = DigitalOutputDevice(Pinout.SWITCH_GATE_PIN)
        self._gate_stop_pin = DigitalOutputDevice(Pinout.STOP_GATE_PIN)

    def temperature(self) -> (float, str):
        # retrieve temperature from cpu
        sys_info = SimpleSystemInfo()

        return sys_info.cpu.temperature, sys_info.cpu.unit

    def system_info(self) -> SystemInfo:
        sys_info = SimpleSystemInfo()

        return sys_info
