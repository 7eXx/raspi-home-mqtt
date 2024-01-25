import time
from abc import ABC, abstractmethod
from system_info_texx.system_info import SystemInfo

from gpiozero import DigitalInputDevice, DigitalOutputDevice


class Automation(ABC):

    _alarm_pin: DigitalInputDevice
    _ecu_status_pin: DigitalInputDevice
    _ecu_toggle_pin: DigitalOutputDevice

    _gate_status_pin: DigitalInputDevice
    _gate_switch_pin: DigitalOutputDevice
    _gate_stop_pin: DigitalOutputDevice

    _alarm_observers: []

    def serialize(self) -> str:
        output = f'{{ {self.__str_alarm_status()}, '
        output += f'{self.__str_ecu_status()}, '
        output += f'{self.__str_gate_status()}, '
        output += f'"systemInfo": {self.system_info().serialize()} }}'

        return output

    def __str_alarm_status(self) -> str:
        return f'"alarm": {int(self.is_alarm_ringing())}'

    def __str_ecu_status(self) -> str:
        return f'"ecu": {int(self.is_alarm_ecu_active())}'

    def __str_gate_status(self) -> str:
        return f'"gate": {int(self.is_gate_open())}'

    @staticmethod
    def is_alarm_ecu_test_mode(prev_state, new_state) -> bool:
        return new_state == prev_state

    @abstractmethod
    def temperature(self) -> (float, str):
        pass

    @abstractmethod
    def system_info(self) -> SystemInfo:
        pass

    def is_alarm_ringing(self) -> bool:
        # check alarm
        if not self._alarm_pin.value:
            return True
        else:
            return False

    def is_alarm_ecu_active(self) -> bool:
        # check ecu state
        if self._ecu_status_pin.value:
            return True
        else:
            return False

    def set_alarm_ecu(self, **kwargs) -> bool:
        if self.is_alarm_ecu_active() != bool(int(kwargs['state'])):
            self.toggle_alarm_ecu()
        return self.is_alarm_ecu_active()

    def toggle_alarm_ecu(self, **kwargs) -> bool:
        # change state ecu toggle pin
        self._ecu_toggle_pin.on()
        time.sleep(0.3)
        self._ecu_toggle_pin.off()
        time.sleep(0.5)

        return self.is_alarm_ecu_active()

    def antipanic_mode(self, **kwargs) -> bool:
        # change state ecu toggle pin
        self._ecu_toggle_pin.on()
        time.sleep(4)
        self._ecu_toggle_pin.off()
        time.sleep(0.5)

        return self.is_alarm_ringing()

    def is_gate_open(self) -> bool:
        if self._gate_status_pin.value:
            return True
        else:
            return False

    def set_gate_ecu(self, **kwargs) -> bool:
        if self.is_gate_open() != bool(int(kwargs['state'])):
            self.toggle_gate_ecu()
        return self.is_gate_open()

    def toggle_gate_ecu(self, **kwargs) -> bool:
        # cambio stato del cancello
        self._gate_switch_pin.on()
        time.sleep(0.5)
        self._gate_switch_pin.off()

        return self.is_gate_open()

    def stop_gate(self, **kwargs) -> bool:
        # cambio pin stop cancello
        self._gate_stop_pin.on()
        time.sleep(0.5)
        self._gate_stop_pin.off()

        return self.is_gate_open()
