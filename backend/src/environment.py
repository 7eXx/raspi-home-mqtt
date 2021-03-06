from dotenv import dotenv_values

config = {
    **dotenv_values(".env.local"),
    **dotenv_values(".env")
}

BROKER_IP = config['BROKER_IP']
BROKER_PORT = config['BROKER_PORT']
PUBLISH_TIMEOUT = int(config['PUBLISH_TIMEOUT'])
STATUS_TOPIC=config['STATUS_TOPIC']
COMMAND_TOPIC=config['COMMAND_TOPIC']

