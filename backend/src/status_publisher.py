from threading import Thread
from time import sleep
import logging
import paho.mqtt.client as mqtt
import src.environment as environment


class StatusPublisher(Thread):
    automation = None
    status_publisher = None
    command_subscriber = None

    def __init__(self, automation):
        Thread.__init__(self)
        self.automation = automation
        self.__create_status_client_publisher()

    def __create_status_client_publisher(self) -> None:
        self.status_publisher = mqtt.Client(client_id=environment.CLIENT_ID, transport="websockets")
        self.status_publisher.on_connect = self.__on_connect_status
        self.status_publisher.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)

    def __on_connect_status(self, client, userdata, flags, rc) -> None:
        logging.debug("Status publisher connected with result code: " + str(rc))

    def run(self):
        while True:
            automation_info_serialized = self.automation.serialize()

            logging.debug(automation_info_serialized)
            self.status_publisher.publish(environment.STATUS_TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
