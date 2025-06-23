from kivy.app import App
from kivy.lang import Builder
from jnius import autoclass
from android_notify import Notification
from android.permissions import request_permissions, Permission
import schedule
import time

# SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
#     packagename=u'org.test.notifyapp',
#     servicename=u'Notify'
# )

permissions = [Permission.POST_NOTIFICATIONS]
request_permissions(permissions)

KV = """
Button:
    text: 'push me!'
    on_release: 
        app.vibrate()
        # app.notification_method()
        app.notify()
"""


class NotificationApp(App):
    def build(self):
        return Builder.load_string(KV)

    # @staticmethod
    # def notify():
    #     Notification(
    #         title="Hello",
    #         message="This is a basic notification."
    #     ).send()

    # @staticmethod
    # def notification_method():
    #     PythonActivity = autoclass('org.kivy.android.PythonActivity')
    #     NotificationManager = autoclass('android.app.NotificationManager')
    #     NotificationCompat = autoclass('androidx.core.app.NotificationCompat')
    #     NotificationChannel = autoclass('android.app.NotificationChannel')
    #     NotificationCompatBuilder = autoclass('androidx.core.app.NotificationCompat$Builder')
    #     BuildVersion = autoclass('android.os.Build$VERSION')
    #
    #     context = PythonActivity.mActivity
    #     notification_manager = context.getSystemService(context.NOTIFICATION_SERVICE)
    #
    #     channel_id = "default_channel"
    #     if BuildVersion.SDK_INT >= 26:
    #         channel = NotificationChannel(
    #             channel_id,
    #             "Default Channel",
    #             NotificationManager.IMPORTANCE_HIGH
    #         )
    #         notification_manager.createNotificationChannel(channel)
    #
    #     builder = NotificationCompatBuilder(context, channel_id)
    #     builder.setContentTitle("This is my notification title")
    #     builder.setContentText("This is the notification message")
    #     builder.setSmallIcon(autoclass("android.R$drawable").ic_dialog_info)
    #     builder.setDefaults(NotificationCompat.DEFAULT_ALL)
    #     builder.setPriority(NotificationCompat.PRIORITY_HIGH)
    #
    #     notification_manager.notify(1, builder.build())

    # @staticmethod
    # def start_foreground_service():
    #     print("trying to start service......")
    #     service = autoclass(SERVICE_NAME)
    #     mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
    #     argument = ''
    #     service.start(mActivity, argument)
        # self.service = service

        # PythonService = autoclass('org.kivy.android.PythonService')
        # Intent = autoclass('android.content.Intent')
        # mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        #
        # intent = Intent(mActivity, PythonService)
        # mActivity.startForegroundService(intent)

    @staticmethod
    def vibrate():
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        Context = autoclass('android.content.Context')
        vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
        vibrator.vibrate(200)

if __name__ == '__main__':
    NotificationApp().run()
