import emoji
import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from raspi_home_texx import get_console_logger, file_logger

from src.bot_telegram_builder import BotTelegramBuilder
from src.command_controller import CommandController
from src.status_publisher import StatusPublisher
from raspi_home_texx.automation import Automation
from src.automation_impl import AutomationImpl
from src.automation_mock import AutomationMock

import src.environment as environment
from src.tapo_management import TapoManagement
from src.tapo_management_impl import TapoManagementImpl
from src.tapo_management_mock import TapoManagementMock
from src.wake_lenovo_controller import WakeLenovoController
from src.wake_ryzen_controller import WakeRyzenController

file_logger.set_file_path(environment.LOG_FILE)

app = Flask(__name__)
CORS(app)
api = Api(app)

tapo_management: TapoManagement
if os.getenv('TAPO_MANAGEMENT') == 'mock':
    tapo_management = TapoManagementMock()
else:
    tapo_management = TapoManagementImpl()

automation: Automation
if os.getenv('GPIOZERO_PIN_FACTORY') == 'mock':
    automation = AutomationMock(tapo_management)
else:
    automation = AutomationImpl(tapo_management)

bot = (BotTelegramBuilder()
       .set_token(environment.BOT_TOKEN)
       .set_name(environment.BOT_NAME)
       .set_list_id(environment.FROM_IDS)
       .set_automation(automation)
       .build())

get_console_logger(__name__, environment.LOGGING_LEVEL).info("sto ascoltando")
file_logger.write("Bot gestione allarme avviato")
bot.send_message_to_list(emoji.emojize("Bot gestione allarme pronto :thumbsup:", use_aliases=True))

status_publisher = StatusPublisher(automation)
status_publisher.start()

api.add_resource(CommandController, "/api/command", resource_class_kwargs={'automation': automation})
api.add_resource(WakeRyzenController, "/api/wake_ryzen", resource_class_kwargs={'automation': automation})
api.add_resource(WakeLenovoController, "/api/wake_lenovo", resource_class_kwargs={'automation': automation})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
