from flask_restful import Resource
from src.base_automation import BaseAutomation


class WakeRyzenController(Resource):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.automation: BaseAutomation = kwargs['automation']

    def get(self):
        return self.automation.wake_ryzen(), 200
