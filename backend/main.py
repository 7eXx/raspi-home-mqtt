import logging
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from src.automation import Automation
from src.command_subscriber import CommandSubscriber
from src.status_publisher import StatusPublisher

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('alarm_ecu_set')
parser.add_argument('gate_ecu_set')
parser.add_argument('gate_stop_set')

class CommandController(Resource):
    __automation: Automation = None

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__automation = kwargs['automation']

    def put(self):
        args = parser.parse_args()

        if self.is_command_ecu_set(args):
            result = self.__automation.ecu_toggle()
        elif self.is_command_gate_set(args):
            result = self.__automation.gate_toggle()
        elif self.is_command_gate_stop_set(args):
            result = self.__automation.gate_stop()
        else:
            abort(404, message="Command providded not available")

        return ({'s': int(result)}, 200)

    def is_command_ecu_set(self, args) -> bool:
        return args['alarm_ecu_set'] != None
    
    def is_command_gate_set(self, args) -> bool:
        return args['gate_ecu_set'] != None

    def is_command_gate_stop_set(self, args) -> bool:
        return args['gate_stop_set'] != None

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

    automation = Automation()
    status_publisher = StatusPublisher(automation)
    status_publisher.start()

    api.add_resource(CommandController, "/command", 
        resource_class_kwargs={'automation': automation})

    app.run(debug=False)
