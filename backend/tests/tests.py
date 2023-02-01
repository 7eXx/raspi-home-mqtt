
from automation_impl import AutomationImpl
from src.system_information import DiskInfo, MemoryInfo, CpuInfo, SystemInformation

disk = DiskInfo()

print(disk.serialize())

memory = MemoryInfo()

print(memory.serialize())

cpu = CpuInfo()

print(cpu.serialize())

system_info = SystemInformation()

print(system_info.serialize())

automation = AutomationImpl()

print(automation.serialize())