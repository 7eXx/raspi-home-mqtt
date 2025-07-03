import json

from raspi_home_texx.environment_info import EnvironmentInfo
from raspi_home_texx.datetime_builder import DatetimeStringBuilder


class TemperatureInfo():
    def __init__(self):
        self.value = "n/a"
        self.unit = "°C"

    def serialize(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def format_pretty(self):
        pass

class HumidityInfo():
    def __init__(self):
        self.value = "n/a"
        self.unit = "%"

    def serialize(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def format_pretty(self):
        pass


class EnvironmentInfoImpl(EnvironmentInfo):
    def __init__(self, status: str = "n/a"):
        super().__init__(status)
        self.timestamp = DatetimeStringBuilder().now()
        self.temperature = TemperatureInfo()
        self.humidity = HumidityInfo()

    def serialize(self) -> str:
        output = f'{{"status": "{self._status}"'
        output += f', "timestamp": "{self.timestamp}"'
        output += f', "temperature": {self.temperature.serialize()}'
        output += f', "humidity": {self.humidity.serialize()}}}'

        return output

    def format_pretty(self) -> str:
        output = "Environment Info: \n"
        output += "--------------------------------------------\n"
        output += f'"timestamp" : "{self.timestamp}"' + "\n"
        output += "--------------------------------------------\n"
        output += f'"status" : "{self._status}"' + "\n"
        output += "--------------------------------------------\n"
        output += self.temperature.format_pretty()
        output += "--------------------------------------------\n"
        output += self.humidity.format_pretty()

        return output

class EnvironmentInfoUnmarshaller:
    def __init__(self, json_string: bytes):
        self.json_string = json_string.decode("utf-8")

    def unmarshall(self) -> EnvironmentInfo:
        env_data = json.loads(self.json_string)
        # check if temperature and humidity fields exist
        if "temperature" not in env_data or "humidity" not in env_data:
            # default env info implementation
            return EnvironmentInfoImpl()

        temperature = self.__extract_temperature(env_data["temperature"])
        hum_data = self.__extract_humidity(env_data["humidity"])

        environment_info = EnvironmentInfoImpl("online")
        environment_info.temperature = temperature
        environment_info.humidity = hum_data

        return environment_info

    def __extract_temperature(self, data: dict) -> TemperatureInfo:
        if "value" not in data or "unit" not in data:
            return TemperatureInfo()

        temperature = TemperatureInfo()
        temperature.value = data["value"]
        temperature.unit = data["unit"]

        return temperature

    def __extract_humidity(self, data: dict) -> HumidityInfo:
        if "value" not in data or "unit" not in data:
            return HumidityInfo()

        humidity = HumidityInfo()
        humidity.value = data["value"]
        humidity.unit = data["unit"]

        return humidity

