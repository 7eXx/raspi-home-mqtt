import unittest

from raspi_home_texx.automation import Automation
from src.automation_mock import AutomationMock


class AutomationTest(unittest.TestCase):
    automation: Automation

    def setUp(self) -> None:
        self.automation = AutomationMock()

    def test_initial_status(self):
        self.assertFalse(self.automation.is_alarm_ringing())
        self.assertFalse(self.automation.is_gate_open())
        self.assertFalse(self.automation.is_gate_open())

    def test_toggle_alarm_ecu(self):
        self.automation.toggle_alarm_ecu()
        self.assertTrue(self.automation.is_alarm_ecu_active())
        self.automation.toggle_alarm_ecu()
        self.assertFalse(self.automation.is_alarm_ecu_active())

    def test_set_alarm_ecu(self):
        self.automation.set_alarm_ecu(state=1)
        self.assertTrue(self.automation.is_alarm_ecu_active())
        self.automation.set_alarm_ecu(state=0)
        self.assertFalse(self.automation.is_alarm_ecu_active())

    def test_anti_panic_mode(self):
        self.automation.anti_panic_mode()
        self.assertTrue(self.automation.is_alarm_ringing())

    def test_toggle_gate_ecu(self):
        self.automation.toggle_gate_ecu()
        self.assertTrue(self.automation.is_gate_open())
        self.automation.toggle_gate_ecu()
        self.assertFalse(self.automation.is_gate_open())

    def test_set_gate_ecu(self):
        self.automation.set_gate_ecu(state=1)
        self.assertTrue(self.automation.is_gate_open())
        self.automation.set_gate_ecu(state=0)
        self.assertFalse(self.automation.is_gate_open())


if __name__ == "__main__":
    unittest.main()
