from gpiozero import DigitalInputDevice, DigitalOutputDevice
from raspi_home_texx import file_logger
from raspi_home_texx.system_info import SimpleSystemInfo, SystemInfo
from raspi_home_texx.automation import Automation

from src.pinout import Pinout


class AutomationImpl(Automation):
    def __init__(self):
        super().__init__()
        self._alarm_pin = DigitalInputDevice(Pinout.SWITCH_ALARM_PIN, None, True, 0.300)
        self._alarm_pin.when_activated = self.__alarm_callback
        self._alarm_pin.when_deactivated = self.__alarm_callback

        self._ecu_status_pin = DigitalInputDevice(Pinout.STATUS_ECU_PIN)
        self._gate_status_pin = DigitalInputDevice(Pinout.STATUS_GATE_PIN)

        self._ecu_toggle_pin = DigitalOutputDevice(Pinout.TOGGLE_ECU_PIN, True, False)
        self._gate_switch_pin = DigitalOutputDevice(Pinout.SWITCH_GATE_PIN)
        self._gate_stop_pin = DigitalOutputDevice(Pinout.STOP_GATE_PIN)

        self._alarm_observers = []

    # Handle the alarm trigger event
    def __alarm_callback(self) -> None:
        is_alarm_ringing = self.is_alarm_ringing()
        if is_alarm_ringing:
            msg = "L'allarme sta suonando"
        else:
            msg = "L'allarme è rientrato"

        file_logger.write(msg)
        for callback in self._alarm_observers:
            callback(is_alarm_ringing)

    def temperature(self) -> (float, str):
        # retrieve temperature from cpu
        sys_info = SimpleSystemInfo()

        return sys_info.cpu.temperature, sys_info.cpu.unit

    def system_info(self) -> SystemInfo:
        sys_info = SimpleSystemInfo()

        return sys_info

    def toggle_alarm_ecu(self, **kwargs) -> bool:
        return super().toggle_alarm_ecu()

    def anti_panic_mode(self, **kwargs) -> bool:
        return super().anti_panic_mode()

    def toggle_gate_ecu(self, **kwargs) -> bool:
        return super().toggle_gate_ecu()

    def stop_gate(self, **kwargs) -> bool:
        return super().stop_gate()
