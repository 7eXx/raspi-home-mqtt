from flask_restful import Resource, abort, reqparse


class CommandController(Resource):
    resources = [
        "alarm_ecu_toggle",
        "alarm_ecu_set",
        "gate_ecu_toggle",
        "gate_ecu_set",
        "gate_stop_toggle",
        "alarm_antipanic_mode",
    ]

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.automation = kwargs['automation']
        self.parser = reqparse.RequestParser()
        for arg in self.__class__.resources:
            self.parser.add_argument(arg)

    def put(self):
        args = self.parser.parse_args()

        if self.is_command_ecu_toggle(args):
            result = self.automation.toggle_alarm_ecu()
        elif self.is_command_ecu_set(args):
            result = self.automation.set_alarm_ecu(int(args['alarm_ecu_set']))
        elif self.is_command_antipanic_mode(args):
            result = self.automation.antipanic_mode()
        elif self.is_command_gate_toggle(args):
            result = self.automation.toggle_gate_ecu()
        elif self.is_command_gate_set(args):
            result = self.automation.set_gate_ecu(int(args['gate_ecu_set']))
        elif self.is_command_gate_stop_set(args):
            result = self.automation.stop_gate()
        else:
            return abort(404, message="Command provided not available")

        return {'s': int(result)}, 200

    def is_command_ecu_toggle(self, args) -> bool:
        return args['alarm_ecu_toggle'] is not None

    def is_command_ecu_set(self, args) -> bool:
        return args['alarm_ecu_set']

    def is_command_antipanic_mode(self, args) -> bool:
        return args['alarm_antipanic_mode'] is not None

    def is_command_gate_toggle(self, args) -> bool:
        return args['gate_ecu_toggle'] is not None

    def is_command_gate_set(self, args) -> bool:
        return args['gate_ecu_set'] is not None

    def is_command_gate_stop_set(self, args) -> bool:
        return args['gate_stop_toggle'] is not None
