
from http import client
from time import sleep
from dotenv import dotenv_values
import paho.mqtt.client as mqtt

config = {    
    **dotenv_values(".env.local"),
    **dotenv_values(".env")
}

BROKER_IP = config['BROKER_IP']
BROKER_PORT = config['BROKER_PORT']
TOPIC=config['TOPIC']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER_IP, int(BROKER_PORT), 60)
client.loop_start

counter = 0
while True:
    counter += 1
    client.publish(TOPIC, "test " + str(counter))
    sleep(3)

