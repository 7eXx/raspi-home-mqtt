
from src.automation import Automation
from src.command_subscriber import CommandSubscriber
from src.status_publisher import StatusPublisher


if __name__ == "__main__":

    automation = Automation()

    command_subscriber = CommandSubscriber(automation)
    command_subscriber.start_loop()

    # status_publisher = StatusPublisher(automation)
    # status_publisher.start_publishing()
