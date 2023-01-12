import unittest

from src.system_information import SystemInformation


class SystemInformationTest(unittest.TestCase):
    system_information: SystemInformation

    def setUp(self):
        self.system_information = SystemInformation()
        print(self.system_information.serialize())

    def test_disk_info_serialize(self):
        output = self.system_information.disk.serialize()
        print("Disk: " + output)
        self.assertTrue("unit" in output)
        self.assertTrue("total" in output)
        self.assertTrue("used" in output)
        self.assertTrue("free" in output)
        self.assertTrue("percentage" in output)

    def test_memory_info_serialize(self):
        output = self.system_information.memory.serialize()
        print("Memory: " + output)
        self.assertTrue("total" in output)
        self.assertTrue("available" in output)
        self.assertTrue("percentage" in output)
        self.assertTrue("used" in output)
        self.assertTrue("free" in output)
        self.assertTrue("unit" in output)

    def test_cpu_info(self):
        output = self.system_information.cpu.serialize()
        print("CPU: " + output)
        self.assertTrue("percentage" in output)
        self.assertTrue("minTemp" in output)
        self.assertTrue("maxTemp" in output)
        self.assertTrue("temperature" in output)
        self.assertTrue("unit" in output)


if __name__ == '__main__':
    unittest.main()
