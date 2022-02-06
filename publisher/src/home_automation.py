from gpiozero import DigitalInputDevice, DigitalOutputDevice
import time
import emoji
from src.home_pinout import HomePinout
from src.logger import LoggerSingleton
from src.system_information import SystemInformation
from src.log_memory_card import LogMemoryCard
from src.home_bot_singleton import HomeBotSingleton

class HomeAutomation:

    def __init__(self):
        self.alarm_pin = DigitalInputDevice(HomePinout.SWITCH_ALARM_PIN, None, True, 0.300)

        self.ecu_status_pin = DigitalInputDevice(HomePinout.STATUS_ECU_PIN)
        self.ecu_toggle_pin = DigitalOutputDevice(HomePinout.TOGGLE_ECU_PIN, True, False)

        self.gate_status_pin = DigitalInputDevice(HomePinout.STATUS_GATE_PIN)
        self.gate_switch_pin = DigitalOutputDevice(HomePinout.SWITCH_GATE_PIN)
        self.gate_stop_pin = DigitalOutputDevice(HomePinout.STOP_GATE_PIN)

    def temperature(self) -> float:
        # recupero della temperatura della cpu
        system_info = SystemInformation()

        return system_info.cpu_temp

    def system_info(self):
        system_info = SystemInformation()

        LoggerSingleton.info(f"system info: {system_info}")

        return system_info

    def is_alarm_ringing(self) -> bool:
        # logging alarm status
        LoggerSingleton.info(f"Stato Alarm: {self.alarm_pin.value}")
        # check alarm
        if not self.alarm_pin.value:
            return True
        else:
            return False

    # funzione per recuperare lo status della centralina
    def ecu_status(self) -> bool:
        # logging ecu state
        LoggerSingleton.info(f"Stato ECU: {self.ecu_status_pin.value}")
        # check ecu state
        if self.ecu_status_pin.value:
            return True
        else:
            return False

    # metodo rpc per cambiare lo stato alla centralina
    def ecu_toggle(self) -> bool:
        # change state ecu toggle pin
        self.ecu_toggle_pin.on()
        time.sleep(0.3)
        self.ecu_toggle_pin.off()
        time.sleep(0.5)

        return self.ecu_status()

    @staticmethod
    def is_ecu_state_mode( prev_state, new_state):
        return new_state == prev_state

    def anti_panic_mode(self):
        # change state ecu toggle pin
        self.ecu_toggle_pin.on()
        time.sleep(4)
        self.ecu_toggle_pin.off()
        time.sleep(0.5)

        return self.ecu_status()

    # metodo rpc per recuperare lo stato del cancello (TRUE=aperto, FALSE=chiuso)
    def gate_status(self) -> bool:
        LoggerSingleton.info(f'Gate status: {self.gate_status_pin.value}')

        if self.gate_status_pin.value:
            return True
        else:
            return False

    # metodo rpc per aprire-chiudere il cancello
    def gate_toggle(self) -> bool:
        LoggerSingleton.debug("Switch Gate")
        # cambio stato del cancello
        self.gate_switch_pin.on()
        time.sleep(0.5)
        self.gate_switch_pin.off()

        return self.gate_status()

    # metodo rpc per bloccare il cancello
    def gate_stop(self) -> bool:
        LoggerSingleton.debug("Stop Gate")
        # cambio pin stop cancello
        self.gate_stop_pin.on()
        time.sleep(0.5)
        self.gate_stop_pin.off()

        return self.gate_status()
