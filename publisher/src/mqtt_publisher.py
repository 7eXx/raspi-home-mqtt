from time import sleep
import paho.mqtt.client as mqtt
from src.automation import Automation
import src.environment as environment


class MqttPublisher:

    automation = None
    status_publisher = None
    command_subscriber = None

    def __init__(self):
        self.automation = Automation()
        self.__create_mqtt_status_publisher()
        self.__create_mqtt_command_subscriber()

    def __create_mqtt_status_publisher(self) -> None:
        self.status_publisher = mqtt.Client()
        self.status_publisher.on_connect = MqttPublisher.__on_connect
        self.status_publisher.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.status_publisher.loop_start

    def __create_mqtt_command_subscriber(self) -> None:
        # TODO: create the command subscriber client to listen in the topic "mqtt/command"
        # define the on message function to parse message and perform proper automation action
        pass

    @staticmethod
    def __on_connect(client, userdata, flags, rc) -> None:
        print("Connected with result code: " + str(rc))

    def start_publishing(self):
        while True:
            automation_info_serialized = self.automation.serialize()

            print(automation_info_serialized)
            self.publisher.publish(environment.TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
