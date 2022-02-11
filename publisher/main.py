
from src.mqtt_publisher import MqttPublisher


if __name__ == "__main__":

    publisher = MqttPublisher()
    publisher.start_publishing()
