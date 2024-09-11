from flask_restful import Resource
from src.base_automation import BaseAutomation


class WakeRyzenController(Resource):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.automation: BaseAutomation = kwargs['automation']

    def get(self):
        result = self.automation.wake_ryzen()
        if result:
            return {'status': result}, 200
        else:
            return {'status': result}, 500
