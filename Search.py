import speech_recognition as s
import datetime
g = datetime.datetime.now()

from pywhatkit import *
def say (a):
    import pyttsx3
    pyobj = pyttsx3.init()
    pyobj . say(a)
    pyobj . runAndWait()

import time
t = time.strftime("%H:%M")
x = time.strftime("%H")
print("Time->",t)
print("Date->",g.strftime("%b.%d.%Y"))
if x< "12":
    print(f"Good Morning Sir,")
    say(f"Good Morning Sir,")
elif x<"18":
    print(f"Good Afternoon Sir,")
    say(f"Good Afternoon Sir,")
elif x<"24":
    print(f"Good Evening Sir,")
    say(f"Good Evening Sir,")
print('''What You wanna search,Sir
Do You Want To Speak Or Type
To Type -> Press 1
To Speak -> Press 2''')
say('''What You wanna search,Sir
Do You Want To Speak Or Type
To Type Press 1
To Speak  Press 2''')
say("Enter Your Choice Here")
b = int(input("Enter Your Choice Here ->"))
match b:
    case 1:
        l = input("Enter What You Wanna Search->")
        search(l)
    case 2:
        
        r = s.Recognizer()
        say("Say What You Wanna Search")
        print("Say What You Wanna Search")
        with s.Microphone()as m:
            audio = r.listen(m)
            while True:
                try:
                    query = r.recognize_google(audio)
                except:
                    print("Speak Again.....")
                    say("Speak Again")
                    audio = r.listen(m)
                    try:
                        query = r.recognize_google(audio)
                    except:
                        pass
                else:
                    break
        search(query)

    case _:
        print("Invalid Choice")
        say("Invalid Choice")




