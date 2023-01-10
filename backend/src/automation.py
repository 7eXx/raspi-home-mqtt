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
        return f'"ecu": {int(self.get_ecu_status())}'

    def str_gate_status(self) -> str:
        return f'"gate": {int(self.get_gate_status())}'

    def system_info(self) -> SystemInformation:
        system_info = SystemInformation()

        return system_info

    @staticmethod
    def is_ecu_state_mode(prev_state, new_state) -> bool:
        return new_state == prev_state

    @abstractmethod
    def is_alarm_ringing(self) -> bool:
        pass

    @abstractmethod
    def get_ecu_status(self) -> bool:
        pass

    @abstractmethod
    def toggle_ecu(self) -> bool:
        pass

    @abstractmethod
    def antipanic_mode(self) -> None:
        pass

    @abstractmethod
    def get_gate_status(self) -> bool:
        pass

    @abstractmethod
    def toggle_gate(self) -> bool:
        pass

    @abstractmethod
    def stop_gate(self) -> bool:
        pass
