from threading import Thread
from time import sleep
from raspi_home_texx.automation import Automation
from raspi_home_texx import get_console_logger
import paho.mqtt.client as mqtt
import src.environment as environment


class StatusPublisher(Thread):

    def __init__(self, automation: Automation):
        Thread.__init__(self)
        self.logger = get_console_logger(__name__, environment.LOGGING_LEVEL)
        self.automation = automation
        self.__create_status_client_publisher()

    def __create_status_client_publisher(self) -> None:
        self.connected_flag = False
        self.client = mqtt.Client(client_id=environment.CLIENT_ID, transport="websockets")
        self.client.on_connect = self.__on_connect
        self.client.on_disconnect = self.__on_disconnect
        # Fix: In case network is not available this will throw exception
        self.client.connect(environment.BROKER_HOST, int(environment.BROKER_PORT), 60)

    def __on_connect(self, client, userdata, flags, rc) -> None:
        self.logger.debug("Status publisher connected with result code: " + str(rc))
        self.connected_flag = True

    def __on_disconnect(self, client, userdata, rc) -> None:
        self.logger.warning("Stataus publisher is going to be discconected")
        self.connected_flag = False

    def run(self):
        self.client.loop_start()
        while True:
            if self.connected_flag:
                automation_info_serialized = self.automation.serialize()
                self.logger.debug(automation_info_serialized)
                if self.automation.is_alarm_ringing():
                    self.logger.info(f'Alarm is ringing!!')

                self.client.publish(environment.STATUS_TOPIC, automation_info_serialized)

            sleep(environment.PUBLISH_TIMEOUT)
