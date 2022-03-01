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
        self.status_publisher.on_connect = self.__on_connect_status
        self.status_publisher.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.status_publisher.loop_start()

    def __create_mqtt_command_subscriber(self) -> None:
        self.command_subscriber = mqtt.Client()
        self.command_subscriber.on_connect = self.__on_connect_command
        self.command_subscriber.on_message = self.__on_message_command
        self.command_subscriber.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.command_subscriber.loop_start()

    def __on_connect_status(self, client, userdata, flags, rc) -> None:
        print("Status publisher connected with result code: " + str(rc))

    def __on_connect_command(self, client, userdata, flags, rc) -> None:
        print("Command subscriber connected with result code: " + str(rc))
        self.command_subscriber.subscribe(environment.COMMAND_TOPIC)

    def __on_message_command(self, client, userdata, msg) -> None:
        print(msg.topic + ": " + str(msg.payload))

    def start_publishing(self):
        while True:
            automation_info_serialized = self.automation.serialize()

            print(automation_info_serialized)
            self.status_publisher.publish(environment.STATUS_TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
