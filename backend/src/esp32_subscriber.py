from threading import Thread
from time import sleep

import paho.mqtt.client as mqtt
from raspi_home_texx import get_console_logger
from raspi_home_texx.automation import Automation
from src import environment
from src.env_info_impl import EnvironmentInfoUnmarshaller


class Esp32Subscriber(Thread):

    def __init__(self, automation: Automation):
        Thread.__init__(self)
        self.logger = get_console_logger(__name__, environment.LOGGING_LEVEL)
        self.automation = automation
        self.__create_temperature_subscriber()

    def __create_temperature_subscriber(self):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.__on_connect
        self.mqtt_client.on_message = self.__on_message
        self.mqtt_client.connect(environment.BROKER_HOST, int(environment.MQTT_PORT), 60)

    def __on_connect(self, client, userdata, flags, rc):
        self.logger.debug("Esp32 subscriber connected with result code "+str(rc))
        self.mqtt_client.subscribe(environment.SENSORS_TOPIC)

    def __on_message(self, client, userdata, msg):
        unmarshaller = EnvironmentInfoUnmarshaller(msg.payload)
        env_info = unmarshaller.unmarshall()
        self.automation.set_environment_info(env_info)

    def run(self):
        self.mqtt_client.loop_start()
        while True:
            sleep(environment.PUBLISH_TIMEOUT)