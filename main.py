import time
from plyer import notification

if __name__=="__main__":
    notification.notify(
    title="****BGMI time Limit reached****",
    message="You have played the game for continuously 4 hours.So now for your own health kindly please take a break and come back after some time.",
    app_icon="C:\Reminder Application py\gunsight.ico",
    timeout=10
 )