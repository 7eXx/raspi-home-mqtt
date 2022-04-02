import json

class Command:

    def __init__(self) -> None:
        self.command = None
        self.value = None

    def parse_payload(self, payload) -> None:
        data = json.loads(payload)
        self.command = data["command"]
        self.value = data["value"]