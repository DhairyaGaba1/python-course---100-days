#Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import time 
from plyer import notification  
REPEAT_INTERVAL = 3600 # Repeat frequency in seconds

  
notification_title = 'GREETINGS FROM ALPHA!'  
notification_message = 'Please have a glass of water'  
  

while True:
  notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )  
  time.sleep(REPEAT_INTERVAL)