import logging
from flask import Flask
from flask_restful import Api

from src.command_controller import CommandController
from src.automation_mock import AutomationMock
from src.status_publisher import StatusPublisher
from src.automation import Automation

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

    automation: Automation = AutomationMock()
    status_publisher = StatusPublisher(automation)
    status_publisher.start()

    api.add_resource(CommandController, "/command",
                     resource_class_kwargs={'automation': automation})

    app.run(debug=False, host="0.0.0.0")
