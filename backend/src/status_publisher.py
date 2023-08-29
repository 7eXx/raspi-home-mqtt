from threading import Thread
from time import sleep
import logging
import paho.mqtt.client as mqtt
import src.environment as environment


class StatusPublisher(Thread):

    def __init__(self, automation):
        Thread.__init__(self)
        self.automation = automation
        self.__create_status_client_publisher()

    def __create_status_client_publisher(self) -> None:
        self.connected_flag = False
        self.client = mqtt.Client(client_id=environment.CLIENT_ID, transport="websockets")
        self.client.on_connect = self.__on_connect
        self.client.on_disconnect = self.__on_disconnect
        # Fix: In case network is not available this will throw exception
        self.client.connect(environment.BROKER_IP, int(environment.BROKER_PORT), 60)

    def __on_connect(self, client, userdata, flags, rc) -> None:
        logging.debug("Status publisher connected with result code: " + str(rc))
        self.connected_flag = True

    def __on_disconnect(self, client, userdata, rc) -> None:
        logging.warning("Stataus publisher is going to be discconected")
        self.connected_flag = False

    def run(self):
        self.client.loop_start()
        while True:
            if self.connected_flag:
                automation_info_serialized = self.automation.serialize()
                logging.debug(automation_info_serialized)
                self.client.publish(environment.STATUS_TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
