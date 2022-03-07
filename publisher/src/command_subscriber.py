from time import sleep
import paho.mqtt.client as mqtt
import src.environment as environment

class CommandSubscriber: 

    automation = None
    command_subscriber = None

    def __init__(self, automation) -> None:
        self.automation = automation
        self.__create_command_client_subscriber()

    def __create_command_client_subscriber(self) -> None:
        self.command_subscriber = mqtt.Client()
        self.command_subscriber.on_connect = self.__on_connect_command
        self.command_subscriber.on_message = self.__on_message_command
        self.command_subscriber.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.command_subscriber.loop_start()

    def __on_connect_command(self, client, userdata, flags, rc) -> None:
        print("Command subscriber connected with result code: " + str(rc))
        self.command_subscriber.subscribe(environment.COMMAND_TOPIC)

    def __on_message_command(self, client, userdata, msg) -> None:
        print(msg.topic + ": " + str(msg.payload))

    def start_loop(self):
        while True:
            sleep(environment.PUBLISH_TIMEOUT)