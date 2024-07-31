# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

import win32com.client 

l = ["Rahul", "Nishant", "Harry"]
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
for i in l:
    print(f"shoutout to {i}")
    speaker.speak(f"Shoutout to {i}")