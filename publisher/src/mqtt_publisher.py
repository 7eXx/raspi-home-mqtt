from time import sleep
from typing import Counter
import paho.mqtt.client as mqtt
import json
from src.system_information import SystemInformation
import src.environment as environment


class MqttPublisher:

    client = None

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = MqttPublisher.__on_connect
        self.client.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.client.loop_start

    @staticmethod
    def __on_connect(client, userdata, flags, rc):
        print("Connected with result code: " + str(rc))

    def start_publishing(self):
        while True:
            system_info = SystemInformation()
            system_info_serialized = system_info.serialize()

            print(system_info_serialized)
            self.client.publish(environment.TOPIC, system_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
