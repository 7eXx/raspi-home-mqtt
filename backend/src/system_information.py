import psutil
import json
from gpiozero import CPUTemperature


class DiskInfo:
    def __init__(self) -> None:
        disk_usage = psutil.disk_usage("/")
        self.unit = "GB"
        self.total = self.__convert_byte_to_unit(disk_usage[0])
        self.used = self.__convert_byte_to_unit(disk_usage[1])
        self.free = self.__convert_byte_to_unit(disk_usage[2])
        self.percentage = disk_usage[3]

    def __convert_byte_to_unit(self, bytes_val) -> float:
        unit_power = 20
        if self.unit == "GB":
            unit_power = 30

        return self.__convert_byte_with_power(bytes_val, unit_power)

    def __convert_byte_with_power(self, bytes_val, power: int) -> float:
        return round(bytes_val / (2.0 ** power), 2)

    def serialize(self) -> str:
        return json.dumps(self.__dict__)


class MemoryInfo:
    def __init__(self) -> None:
        memory = psutil.virtual_memory()
        self.total = self.__convert_byte_to_megabyte(memory[0])
        self.available = self.__convert_byte_to_megabyte(memory[1])
        self.percentage = memory[2]
        self.used = self.__convert_byte_to_megabyte(memory[3])
        self.free = self.__convert_byte_to_megabyte(memory[4])
        self.unit = "MB"

    def __convert_byte_to_megabyte(self, bytes_val) -> float:
        return round(bytes_val / (2.0 ** 20), 2)

    def serialize(self) -> str:
        return json.dumps(self.__dict__)


class CpuInfo:
    def __init__(self) -> None:
        self.percentage = psutil.cpu_percent()
        self.__retrieve_cpu_temperature()
        self.unit = "°C"

    def __retrieve_cpu_temperature(self) -> None:
        # recupero della temperatura della cpu
        try:
            cpu = CPUTemperature()
            self.min_temp = cpu.min_temp
            self.max_temp = cpu.max_temp
            self.temperature = cpu.temperature
        except FileNotFoundError as err:
            self.min_temp = 0
            self.max_temp = 0
            self.temperature = 0

    def serialize(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)

class SystemInformation:
    def __init__(self):
        self.cpu = CpuInfo()
        self.memory = MemoryInfo()
        self.disk = DiskInfo()

    def serialize(self):
        return f'{{"cpu": {self.cpu.serialize()}, "memory": {self.memory.serialize()}, "disk": {self.disk.serialize()}}}'
