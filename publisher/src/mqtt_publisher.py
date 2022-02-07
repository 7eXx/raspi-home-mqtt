from time import sleep
from typing import Counter
import paho.mqtt.client as mqtt
import src.environment as environment


class MqttPublisher:

    client = None
    counter = 0

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
            self.counter += 1
            print('publish: ' + str(self.counter))
            self.client.publish(environment.TOPIC, str(self.counter))
            sleep(environment.PUBLISH_TIMEOUT)
