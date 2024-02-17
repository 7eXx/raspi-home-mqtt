from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

BROKER_HOST = config['BROKER_HOST']
BROKER_PORT = config['BROKER_PORT']
CLIENT_ID = config['CLIENT_ID']
PUBLISH_TIMEOUT = int(config['PUBLISH_TIMEOUT'])
STATUS_TOPIC=config['STATUS_TOPIC']
COMMAND_TOPIC=config['COMMAND_TOPIC']
LOGGING_LEVEL=config['LOGGING_LEVEL']

BOT_TOKEN = config['BOT_TOKEN']
BOT_NAME = config['BOT_NAME']

LOG_FILE = config['LOG_FILE']

FROM_IDS = [int(chat_id) for chat_id in config['CHAT_IDS'].split(',')]

