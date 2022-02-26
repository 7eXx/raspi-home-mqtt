from time import sleep
import paho.mqtt.client as mqtt
from src.automation import Automation
import src.environment as environment


class MqttPublisher:

    automation = None
    publisher = None
    subscriber = None

    def __init__(self):
        self.automation = Automation()
        self.__create_mqtt_publisher()
        self.__create_mqtt_subscriber()
        

    def __create_mqtt_publisher(self) -> None:
        self.publisher = mqtt.Client()
        self.publisher.on_connect = MqttPublisher.__on_connect
        self.publisher.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.publisher.loop_start

    @staticmethod
    def __on_connect(client, userdata, flags, rc) -> None:
        print("Connected with result code: " + str(rc))

    def start_publishing(self):
        while True:
            automation_info_serialized = self.automation.serialize()

            print(automation_info_serialized)
            self.publisher.publish(environment.TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
