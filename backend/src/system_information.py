import psutil
import json
from gpiozero import CPUTemperature

class DiskInfo:

    total = None
    used = None
    free = None
    percentage = None
    unit = None

    def __init__(self) -> None:
        disk_usage = psutil.disk_usage('/')
        self.total = self.__convert_byte_to_megabyte(disk_usage[0])
        self.used = self.__convert_byte_to_megabyte(disk_usage[1])
        self.free = self.__convert_byte_to_megabyte(disk_usage[2])
        self.percentage = disk_usage[3]
        self.unit = 'MB'

    def __convert_byte_to_megabyte(self, bytes_val) -> float:
        return bytes_val / (2.0 ** 20)

    def serialize(self) -> str:
        return json.dumps(self.__dict__)

class MemoryInfo:
    
    total = None
    available = None
    percentage = None
    used = None
    free = None
    unit = None

    def __init__(self) -> None: 
        memory = psutil.virtual_memory()
        self.total = self.__convert_byte_to_megabyte(memory[0])
        self.available = self.__convert_byte_to_megabyte(memory[1])
        self.percentage = memory[2]
        self.used = self.__convert_byte_to_megabyte(memory[3])
        self.free = self.__convert_byte_to_megabyte(memory[4])
        self.unit = 'MB'

    def __convert_byte_to_megabyte(self, bytes_val) -> float:
        return bytes_val / (2.0 ** 20)

    def serialize(self) -> str:
        return json.dumps(self.__dict__)


class CpuInfo:

    percentage = None
    temperature = None
    unit = None

    def __init__(self) -> None:
        self.percentage = psutil.cpu_percent()
        self.temperature = self.__get_cpu_temperature()
        self.unit = 'C'

    def __get_cpu_temperature(self) -> str:
        # recupero della temperatura della cpu
        try:
            cpu = CPUTemperature()
            temp = cpu.temperature
        except FileNotFoundError as err:
            temp = 0

        return temp
    
    def serialize(self) -> str:
        return json.dumps(self.__dict__)
         

class SystemInformation:

    cpu = None
    memory = None
    disk = None

    def __init__(self):
        self.cpu = CpuInfo()
        self.memory = MemoryInfo()
        self.disk = DiskInfo()

    def serialize(self):
        return f'{{"cpu": {self.cpu.serialize()}, "memory": {self.memory.serialize()}, "disk": {self.disk.serialize()} }}'
