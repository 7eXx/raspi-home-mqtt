from automation import Automation

class AutomationSingleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if AutomationSingleton.__instance is None:
            AutomationSingleton.__instance = Automation()

        return AutomationSingleton.__instance