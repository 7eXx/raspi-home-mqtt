from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

BROKER_IP = config['BROKER_IP']
BROKER_PORT = config['BROKER_PORT']
CLIENT_ID = config['CLIENT_ID']
PUBLISH_TIMEOUT = int(config['PUBLISH_TIMEOUT'])
STATUS_TOPIC=config['STATUS_TOPIC']
COMMAND_TOPIC=config['COMMAND_TOPIC']

