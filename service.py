from time import sleep
from android_notify import Notification
from jnius import autoclass
from plyer import vibrator


PythonService = autoclass("org.kivy.android.PythonService")
PythonService.mService.setAutoRestartService(True)

def notify():
    Notification(
        title="Hello",
        message="This is a basic notification.",
    ).send()

    # vibrator.pattern([0, 1, 1, 1])

    # PythonActivity = autoclass('org.kivy.android.PythonActivity')
    # activity = PythonActivity.mActivity
    # Context = autoclass('android.content.Context')
    # vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
    # vibrator.vibrate(200)

if __name__ == '__main__':
    while True:
        print("Service running.......")
        notify()
        sleep(10)