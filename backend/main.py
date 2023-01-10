import logging
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

from src.automation_mock import AutomationMock
from src.status_publisher import StatusPublisher
from src.automation import Automation
from src.automation_impl import AutomationImpl

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('alarm_ecu_toggle')
parser.add_argument('gate_ecu_toggle')
parser.add_argument('gate_stop_toggle')
parser.add_argument('alarm_antipanic_mode')


class CommandController(Resource):
    automation: Automation

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.automation = kwargs['automation']

    def put(self):
        args = parser.parse_args()

        if self.is_command_ecu_set(args):
            result = self.automation.toggle_ecu()
        elif self.is_command_antipanic_mode(args):
            result = self.automation.antipanic_mode()
        elif self.is_command_gate_set(args):
            result = self.automation.toggle_gate()
        elif self.is_command_gate_stop_set(args):
            result = self.automation.stop_gate()
        else:
            abort(404, message="Command providded not available")

        return {'s': int(result)}, 200

    def is_command_ecu_set(self, args) -> bool:
        return args['alarm_ecu_toggle'] is not None

    def is_command_antipanic_mode(self, args) -> bool:
        return args['alarm_antipanic_mode'] is not None

    def is_command_gate_set(self, args) -> bool:
        return args['gate_ecu_toggle'] is not None

    def is_command_gate_stop_set(self, args) -> bool:
        return args['gate_stop_toggle'] is not None


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

    automation: Automation = AutomationMock()
    status_publisher = StatusPublisher(automation)
    status_publisher.start()

    api.add_resource(CommandController, "/command",
                     resource_class_kwargs={'automation': automation})

    app.run(debug=False, host='0.0.0.0')
