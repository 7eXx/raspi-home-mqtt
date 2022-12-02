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
    def put(self):
        args = parser.parse_args()
        self.__abort_if_command_not_valid(args)

        return None, 201

    def __abort_if_command_not_valid(self, args):
        if args['alarm_ecu_set'] == None and \
            args['gate_ecu_set'] == None and \
            args['gate_stop_set'] == None:
            abort(404, message="Command providded not available")
            

api.add_resource(CommandController, "/command")

if __name__ == "__main__":

    app.run(debug=True)

    # logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s")

    # automation = Automation()

    # status_publisher = StatusPublisher(automation)
    # status_publisher.start_publishing()
