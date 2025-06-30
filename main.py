from kivy.app import App
from kivy.lang import Builder
from jnius import autoclass
from android_notify import Notification
from android.permissions import request_permissions, Permission


SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
    packagename=u'org.test.notifyapp',
    servicename=u'Notify'
)

permissions = [Permission.POST_NOTIFICATIONS, Permission.SEND_SMS]
request_permissions(permissions)

Notification.passed_check=True

KV = """
Button:
    text: 'push me!'
    on_release: 
        app.vibrate()
        app.notify()
"""


class NotificationApp(App):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.start_foreground_service()

    @staticmethod
    def notify():
        Notification(
            title="Hello",
            message="This is a basic notification."
        ).send()

    @staticmethod
    def start_foreground_service():
        print("trying to start service......")
        service = autoclass(SERVICE_NAME)
        mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
        argument = ''
        service.start(mActivity, argument)
        return service

    @staticmethod
    def vibrate():
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        Context = autoclass('android.content.Context')
        vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
        vibrator.vibrate(200)

if __name__ == '__main__':
    NotificationApp().run()
