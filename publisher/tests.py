
from src.automation import Automation
from src.system_information import DiskInfo, MemoryInfo, CpuInfo, SystemInformation

disk = DiskInfo()

print(disk.serialize())

memory = MemoryInfo()

print(memory.serialize())

cpu = CpuInfo()

print(cpu.serialize())

system_info = SystemInformation()

print(system_info.serialize())

automation = Automation()

print(automation.serialize())