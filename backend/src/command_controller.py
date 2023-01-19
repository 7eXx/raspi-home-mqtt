from flask_restful import Resource, abort, reqparse


class CommandController(Resource):
    arguments = [
        "command",
        "state"
    ]

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.automation = kwargs['automation']
        self.commands = {
            "alarm_ecu_toggle": self.automation.toggle_alarm_ecu,
            "alarm_ecu_set": self.automation.set_alarm_ecu,
            "alarm_antipanic_mode": self.automation.antipanic_mode,
            "gate_ecu_toggle": self.automation.toggle_gate_ecu,
            "gate_ecu_set": self.automation.set_gate_ecu,
            "gate_stop_toggle": self.automation.stop_gate,
        }
        self.parser = reqparse.RequestParser()
        for arg in self.__class__.arguments:
            self.parser.add_argument(arg)

    def put(self):
        args = self.parser.parse_args()

        command, state = args['command'], args['state']

        if not self.is_command_valid(command):
            return abort(400, message="Command provided not available")

        result = self.commands[command](state)

        return {'s': int(result)}, 200

    def is_command_valid(self, command: str) -> bool:
        return command in self.commands
