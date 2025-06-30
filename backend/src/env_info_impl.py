import json

from raspi_home_texx.environment_info import EnvironmentInfo
from raspi_home_texx.sys_info.datetime_builder import DatetimeStringBuilder


class TemperatureInfo:

    def __init__(self):
        self.value = -1000
        self.unit = "C"

    def serialize(self):
        return json.dumps(self.__dict__)

class HumidityInfo:

    def __init__(self):
        self.value = -1000
        self.unit = "%"

    def serialize(self):
        return json.dumps(self.__dict__)


class EnvironmentInfoImpl(EnvironmentInfo):

    def __init__(self):
        self.timestamp = DatetimeStringBuilder().now()
        self.temperature = TemperatureInfo()
        self.humidity = HumidityInfo()

    def serialize(self) -> str:
        output = f'{{"timestamp": "{self.timestamp}"'
        output += f', "temperature": {self.temperature.serialize()}'
        output += f', "humidity": {self.humidity.serialize()}}}'

        return output

    def format_pretty(self) -> str:
        pass