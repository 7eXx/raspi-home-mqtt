from time import sleep
from src.automation import Automation


class AutomationMock(Automation):
    def __init__(self):
        self.alarm_pin = 1
        self.ecu_status_pin = 0
        self.gate_status_pin = 0

    def is_alarm_ringing(self) -> bool:
        if not self.alarm_pin:
            return True
        else:
            return False

    def get_ecu_status(self) -> bool:
        if self.ecu_status_pin:
            return True
        else:
            return False

    def toggle_ecu(self) -> bool:
        sleep(0.5)
        self.ecu_status_pin = int(not self.get_ecu_status())
        self.alarm_pin = 1
        return self.get_ecu_status()

    def antipanic_mode(self) -> bool:
        sleep(2)
        self.ecu_status_pin = 1
        self.alarm_pin = 0
        return self.is_alarm_ringing()

    def get_gate_status(self) -> bool:
        if self.gate_status_pin:
            return True
        else:
            return False

    def toggle_gate(self) -> bool:
        sleep(0.5)
        self.gate_status_pin = int(not self.get_gate_status())
        return self.get_gate_status()

    def stop_gate(self) -> bool:
        sleep(1)
        return self.get_gate_status()
