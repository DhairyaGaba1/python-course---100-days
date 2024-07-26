import time
t=int(time.strftime("%H"))
if t>0 and t<12:
    print("Good morning!")
elif t>12 and t<5:
    print("Good afternoon!")
else:
    print("Good evening!")
    
#CORRECT.