from time import sleep
import paho.mqtt.client as mqtt
from src.automation import Automation
import src.environment as environment


class MqttPublisher:

    automation = None
    client = None

    def __init__(self):
        self.automation = Automation()
        self.__create_mqtt_client()
        

    def __create_mqtt_client(self) -> None:
        self.client = mqtt.Client()
        self.client.on_connect = MqttPublisher.__on_connect
        self.client.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.client.loop_start

    @staticmethod
    def __on_connect(client, userdata, flags, rc) -> None:
        print("Connected with result code: " + str(rc))

    def start_publishing(self):
        while True:
            automation_info_serialized = self.automation.serialize()

            print(automation_info_serialized)
            self.client.publish(environment.TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
