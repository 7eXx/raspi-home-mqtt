import psutil
from gpiozero import CPUTemperature


class SystemInformation:

    def __init__(self):
        # recupero percentuale cpu
        cpu_per = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        self.cpu_temp = self.__get_cpu_temperature()

        self.cpu_perc = cpu_per

        self.tot_mem = SystemInformation.__convert_byte_to_megabyte(memory[0])
        self.ava_mem = SystemInformation.__convert_byte_to_megabyte(memory[1])
        self.per_mem = memory[2]
        self.use_mem = SystemInformation.__convert_byte_to_megabyte(memory[3])
        self.fre_mem = SystemInformation.__convert_byte_to_megabyte(memory[4])

        self.tot_disk = SystemInformation.__convert_byte_to_megabyte(disk_usage[0])
        self.use_disk = SystemInformation.__convert_byte_to_megabyte(disk_usage[1])
        self.fre_disk = SystemInformation.__convert_byte_to_megabyte(disk_usage[2])
        self.per_disk = disk_usage[3]

    def __get_cpu_temperature(self) -> str:
        # recupero della temperatura della cpu
        try:
            cpu = CPUTemperature()
            temp = cpu.temperature
        except FileNotFoundError as err:
            temp = 0

        return temp

    @staticmethod
    def __convert_byte_to_megabyte(bytes_val) -> float:
        return bytes_val / (2.0 ** 20)
