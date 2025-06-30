from time import sleep
from android_notify import Notification


def notify():
    Notification(
        title="Hello",
        message="This is a basic notification."
    ).send()


if __name__ == '__main__':
    while True:
        print("Service running.......")
        notify()
        sleep(5)