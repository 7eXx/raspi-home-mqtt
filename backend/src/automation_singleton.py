from automation_impl import AutomationImpl

class AutomationSingleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if AutomationSingleton.__instance is None:
            AutomationSingleton.__instance = AutomationImpl()

        return AutomationSingleton.__instance