from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

BROKER_HOST = config['BROKER_HOST']
WEBSOCKET_PORT = config['WEBSOCKET_PORT']
MQTT_PORT = config['MQTT_PORT']
CLIENT_ID = config['CLIENT_ID']
PUBLISH_TIMEOUT = int(config['PUBLISH_TIMEOUT'])
STATUS_TOPIC=config['STATUS_TOPIC']
COMMAND_TOPIC=config['COMMAND_TOPIC']
SENSORS_TOPIC=config['SENSORS_TOPIC']
LOGGING_LEVEL=config['LOGGING_LEVEL']

BOT_TOKEN = config['BOT_TOKEN']
BOT_NAME = config['BOT_NAME']

LOG_FILE = config['LOG_FILE']

FROM_IDS = [int(chat_id) for chat_id in config['CHAT_IDS'].split(',')]

JENKINS_USER=config['JENKINS_USER']
JENKINS_PASS=config['JENKINS_PASS']

WAKE_LAN_JOB_URL=config['WAKE_LAN_JOB_URL']
WAKE_LAN_TOKEN=config['WAKE_LAN_TOKEN']

RYZEN_MAC_ADDR=config['RYZEN_MAC_ADDR']
LUIGI_LENOVO_MAC_ADDR=config['LUIGI_LENOVO_MAC_ADDR']

TAPO_C200_IP=config['TAPO_C200_IP']
TAPO_C500_IP=config['TAPO_C500_IP']
TAPO_USERNAME=config['TAPO_USERNAME']
TAPO_PASSWORD=config['TAPO_PASSWORD']
