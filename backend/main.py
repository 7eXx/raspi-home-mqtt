import logging
import os
from flask import Flask
from flask_restful import Api

from src.command_controller import CommandController
from src.status_publisher import StatusPublisher
from src.automation import Automation
from src.automation_impl import AutomationImpl
from src.automation_mock import AutomationMock

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

    automation: Automation
    if os.getenv('GPIOZERO_PIN_FACTORY') == 'mock':
        automation = AutomationMock()
    else:
        automation = AutomationImpl()

    status_publisher = StatusPublisher(automation)
    status_publisher.start()

    api.add_resource(CommandController, "/command",
                     resource_class_kwargs={'automation': automation})

    app.run(debug=False, host="0.0.0.0")
