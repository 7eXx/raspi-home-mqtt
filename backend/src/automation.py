from abc import ABC, abstractmethod
from src.system_information import SystemInformation


class Automation:

    def serialize(self) -> str:
        output = f'{{ {self.str_alarm_status()}, '
        output += f'{self.str_ecu_status()}, '
        output += f'{self.str_gate_status()}, '
        output += f'"systemInfo": {self.system_info().serialize()} }}'

        return output

    def str_alarm_status(self) -> str:
        return f'"alarm": {int(self.is_alarm_ringing())}'

    def str_ecu_status(self) -> str:
        return f'"ecu": {int(self.is_alarm_ecu_active())}'

    def str_gate_status(self) -> str:
        return f'"gate": {int(self.is_gate_open())}'

    def system_info(self) -> SystemInformation:
        system_info = SystemInformation()

        return system_info

    @staticmethod
    def is_alarm_ecu_test_mode(prev_state, new_state) -> bool:
        return new_state == prev_state

    @abstractmethod
    def is_alarm_ringing(self) -> bool:
        pass

    @abstractmethod
    def is_alarm_ecu_active(self) -> bool:
        pass

    @abstractmethod
    def is_gate_open(self) -> bool:
        pass

    def set_alarm_ecu(self, value: int) -> bool:
        if self.is_alarm_ecu_active() != bool(value):
            self.toggle_alarm_ecu()
        return self.is_alarm_ecu_active()

    def set_gate_ecu(self, value: int) -> bool:
        if self.is_gate_open() != bool(value):
            self.toggle_gate_ecu()
        return self.is_gate_open()

    @abstractmethod
    def toggle_alarm_ecu(self) -> bool:
        pass

    @abstractmethod
    def antipanic_mode(self) -> None:
        pass

    @abstractmethod
    def toggle_gate_ecu(self) -> bool:
        pass

    @abstractmethod
    def stop_gate(self) -> bool:
        pass
