import logging
from time import sleep
import paho.mqtt.client as mqtt
from src.command import Command
import src.environment as environment

class CommandSubscriber: 

    automation = None
    command_subscriber = None

    def __init__(self, automation) -> None:
        self.automation = automation
        self.__create_command_client_subscriber()

    def __create_command_client_subscriber(self) -> None:
        self.command_subscriber = mqtt.Client(transport="websockets")
        self.command_subscriber.on_connect = self.__on_connect_command
        self.command_subscriber.on_message = self.__on_message_command
        self.command_subscriber.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)
        self.command_subscriber.loop_start()
    
    def start_infinite_loop(self) -> None:
        while True:
            sleep(environment.PUBLISH_TIMEOUT)

    def __on_connect_command(self, client, userdata, flags, rc) -> None:
        logging.debug("Command subscriber connected with result code: " + str(rc))
        self.command_subscriber.subscribe(environment.COMMAND_TOPIC)

    def __on_message_command(self, client, userdata, msg) -> None:        
        command = Command()
        command.parse_payload(msg.payload)

        logging.debug("command: " + command.command)
        logging.debug("value: " + str(command.value))

