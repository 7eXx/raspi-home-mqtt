import time
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from src.pinout import Pinout
from src.automation import Automation


class AutomationImpl(Automation):
    def __init__(self):
        self.alarm_pin = DigitalInputDevice(Pinout.SWITCH_ALARM_PIN, True, None, 0.300)
        self.ecu_status_pin = DigitalInputDevice(Pinout.STATUS_ECU_PIN)
        self.gate_status_pin = DigitalInputDevice(Pinout.STATUS_GATE_PIN)

        self.ecu_toggle_pin = DigitalOutputDevice(Pinout.TOGGLE_ECU_PIN, True, False)
        self.gate_switch_pin = DigitalOutputDevice(Pinout.SWITCH_GATE_PIN)
        self.gate_stop_pin = DigitalOutputDevice(Pinout.STOP_GATE_PIN)

    def is_alarm_ringing(self) -> bool:
        # check alarm
        if not self.alarm_pin.value:
            return True
        else:
            return False

    # funzione per recuperare lo status della centralina
    def is_alarm_ecu_active(self) -> bool:
        # check ecu state
        if self.ecu_status_pin.value:
            return True
        else:
            return False

    def is_gate_open(self) -> bool:
        if self.gate_status_pin.value:
            return True
        else:
            return False

    # metodo rpc per cambiare lo stato alla centralina
    def toggle_alarm_ecu(self, **kwargs) -> bool:
        # change state ecu toggle pin
        self.ecu_toggle_pin.on()
        time.sleep(0.3)
        self.ecu_toggle_pin.off()
        time.sleep(0.5)

        return self.is_alarm_ecu_active()

    def antipanic_mode(self, **kwargs) -> bool:
        # change state ecu toggle pin
        self.ecu_toggle_pin.on()
        time.sleep(4)
        self.ecu_toggle_pin.off()
        time.sleep(0.5)

        return self.is_alarm_ringing()

    def toggle_gate_ecu(self, **kwargs) -> bool:
        # cambio stato del cancello
        self.gate_switch_pin.on()
        time.sleep(0.5)
        self.gate_switch_pin.off()

        return self.is_gate_open()

    # metodo rpc per bloccare il cancello
    def stop_gate(self, **kwargs) -> bool:
        # cambio pin stop cancello
        self.gate_stop_pin.on()
        time.sleep(0.5)
        self.gate_stop_pin.off()

        return self.is_gate_open()
