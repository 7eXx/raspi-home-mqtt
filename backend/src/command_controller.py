from flask_restful import Resource, abort, reqparse



class CommandController(Resource):
    arguments = [
        "command",
        "state"
    ]

    commands = [
        "alarm_ecu_toggle",
        "alarm_ecu_set",
        "alarm_antipanic_mode"
        "gate_ecu_toggle",
        "gate_ecu_set",
        "gate_stop_toggle"
    ]

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.automation = kwargs['automation']
        self.parser = reqparse.RequestParser()
        for arg in self.__class__.arguments:
            self.parser.add_argument(arg)

    def put(self):
        args = self.parser.parse_args()

        command, state = args['command'], args['state']

        if not self.is_command_valid(command):
            return abort(400, message="Command provided not available")

        if command == "alarm_ecu_toggle":
            result = self.automation.toggle_alarm_ecu()
        elif command == "alarm_ecu_set" and state is not None:
            result = self.automation.set_alarm_ecu(int(state))
        elif command == "alarm_antipanic_mode":
            result = self.automation.antipanic_mode()
        elif command == "gate_ecu_toggle":
            result = self.automation.toggle_gate_ecu()
        elif command == "gate_ecu_set" and state is not None:
            result = self.automation.set_gate_ecu(int(state))
        elif command == "gate_stop_toggle":
            result = self.automation.stop_gate()
        else:
            return abort(400, message="Wrong combination for command and state")

        return {'s': int(result)}, 200

    def is_command_valid(self, command: str) -> bool:
        return command in self.__class__.commands
