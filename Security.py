import time
from pyttsx3 import *
def bol(a):
    b = init()
    b.say(a)
    b.runAndWait()
    b.stop()
    
g = 1
a = 9876 #Change PASSWORD ACCORDING TO YOUR REQUIREMENTS
i = 1
while i < 2:
    bol("Enter Password")
    c = int(input("Enter Password"))
    if c == 9876:
            print("Allowed")
            bol("Allowed")
            break
    else:
        if g %4 == 0:
            print("Try Again After 30 seconds")
            bol("Try Again After 30 seconds")
            time.sleep(30)
            print("Try Now")
            bol("Try Now")
        else:
            print("Not Allowed")
            bol("Not Allowed")
    g += 1
    
    
    
