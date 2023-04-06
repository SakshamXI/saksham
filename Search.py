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
Please type it''')
say('''What You wanna search,Sir
Please type it
type your question here
''') 
a = input("Type your question here ->")

search(a)

