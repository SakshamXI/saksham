import pyautogui as p
import reminder
import weather
import time
from pyttsx3 import *
import pywhatkit
import datetime
import random
riddles = {
    "What is always in front of you but can't be seen?": "The future.",
    "What has a neck but no head?": "A bottle.",
    "What can you catch but never throw?": "A cold.",
    "What has a heart that doesn't beat?": "An artichoke.",
    "What is full of holes but still holds water?": "A sponge.",
    "What has a face and hands but no arms or legs?": "A clock.",
    "What can run but never walks, has a mouth but never talks, has a bed but never sleeps?": "A river.",
    "What is so fragile that saying its name breaks it?": "Silence.",
    "What is as light as a feather, but even the strongest man cannot hold it for long?": "Breath.",
    "What goes up but never comes down?": "Your age.",
    "What has a thumb and four fingers but isn't alive?": "A glove.",
    "What starts with an E, ends with an E, but only contains one letter?": "An envelope.",
    "What has a head and a tail but no body?": "A coin.",
    "What runs all the way around a backyard but never moves?": "A fence.",
    "What has a ring but no finger?": "A telephone.",
    "What is easy to get into but hard to get out of?": "Trouble.",
    "What begins with T, ends with T, and has T in it?": "A teapot.",
    "What has four legs in the morning, two legs in the afternoon, and three legs in the evening?": "A human.",
    "What starts with an E, ends with an E, but only has one letter in it?": "An envelope.",
    "What is always in front of you but can't be seen?": "The future.",
    "What has a neck but no head?": "A bottle.",
    "What can you catch but never throw?": "A cold.",
    "What has a heart that doesn't beat?": "An artichoke.",
    "What is full of holes but still holds water?": "A sponge.",
    "What has a face and hands but no arms or legs?": "A clock.",
    "What can run but never walks, has a mouth but never talks, has a bed but never sleeps?": "A river.",
    "What is so fragile that saying its name breaks it?": "Silence.",
    "What is as light as a feather, but even the strongest man cannot hold it for long?": "Breath.",
    "What goes up but never comes down?": "Your age.",
    "What starts with an E, ends with an E, but only contains one letter?": "An envelope.",
}
jokes = [ "Why did the tomato turn red? Because it saw the salad dressing!", "Why don’t scientists trust atoms? Because they make up everything!", "What do you call a fake noodle? An impasta!", "Why did the hipster burn his tongue? He drank his coffee before it was cool.", "Why did the cookie go to the doctor? Because it felt crummy!", "Why was the math book sad? Because it had too many problems.", "What do you call a bear with no teeth? A gummy bear!", "Why don't oysters give to charity? They're shellfish!", "What do you call a lazy kangaroo? A pouch potato!", "Why do bees have sticky hair? Because they use honeycombs!", "Why was the computer cold? It left its Windows open!", "Why was the belt arrested? For holding up the pants!", "Why couldn’t the bicycle stand up by itself? Because it was two-tired!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why don't ghosts like rain? It dampens their spirits!", "Why don't skeletons fight each other? They don't have the guts!", "What do you call a singing laptop? A Dell!", "Why did the coffee file a police report? It got mugged!", "Why did the chicken cross the playground? To get to the other slide!", "Why did the tomato turn red? Because it saw the salad dressing!", "What do you call a can opener that doesn't work? A can't opener!", "Why do cows wear bells? Because their horns don't work!", "What do you call a fake noodle? An impasta!", "Why did the orange stop? Because it ran out of juice!", "Why was the math book sad? Because it had too many problems.", "What do you call a lazy kangaroo? A pouch potato!", "What do you call a snowman with a six-pack? An abdominal snowman!", "Why do bees have sticky hair? Because they use honeycombs!", "Why was the computer cold? It left its Windows open!", "Why was the belt arrested? For holding up the pants!"]
f = time.strftime("%H")
k = 1
u = 0
a = 2

if f < "12":
    g = ("Good morning sir")
elif f < "18":
    g = "good afternoon sir"
elif f < "24":

    g = "good evening sir"


def find(a):
    pywhatkit.search(a)


def say(a):
    b = init()
    b.say(a)
    b.runAndWait()
    b.stop()


b = ""
import speech_recognition as s

r = s.Recognizer()


def hear(b, a=None):
    b = ""
    if a is not None:
        say(a)
    with s.Microphone() as m:
        audio = r.listen(m)
        while True:
            try:
                b = b + r.recognize_google(audio)
            except:
                audio = r.listen(m)
                try:
                    b = b + r.recognize_google(audio)
                except:
                    if a is not None:
                        say("Say again i cant get it")
                    pass
            else:
                b.lower()
                break
    return b.lower()
while True:
    while True:
        l = hear(b, None)
        if "wake up" in l:

            say("initializing nerd bot")
            time.sleep(1)
            say(f"{g} nerd bot initialized")
            break
        else:
            pass
    while True:
        
        
        if a == 2:
            say("What can i do sir")
            l = hear(b,a)
            
        else:
            l = hear(b)
        a += 1
        print(l)
        if "youtube" in l:
            say("what to search in it ")
            c = hear(b, a)
            say("opening youtube")
            p.hotkey('shift', 'F9')
            time.sleep(8)
            p.click(504, 57)
            p.write(c)
            p.click(924, 53, clicks=3)
            time.sleep(5)
            p.click(419, 377)
            p.click(419, 377)
            time.sleep(7)
            while True:
                f = hear(b)
                if f in ["skip","pause","play"]:
                    p.click(838, 480)
                elif "close" in f:
                    p.click(1343, 0)
                    break
                elif "switch to" in f:
                    d12 = f.replace("switch to","")
                    p.click(879,56,clicks = 2)
                    p.click(504,57)
                    p.write(d12)
                    p.click(924,53,clicks = 3)
                    time.sleep(5)
                    p.click(419, 377)
                    p.click(419, 377)
                    
                else:
                    pass
                
        elif "play" in l:
            g = l
            m = g.replace("play", " ")
            m.strip()
            say("opening spotify")
            p.hotkey("Ctrl", "Alt", "/")
            time.sleep(8)
            p.click(85, 99)
            p.click(455, 26)
            time.sleep(8)
            p.write(m)
            time.sleep(8)
            p.click(822, 192, clicks=2)
            while True:
                y = ["play", "pause"]
                g = hear(b)
                if "close" in g:
                    p.click(1343, 0)
                    break
                elif "next" in g:
                    p.click(729, 663)
                elif "previous" in g:
                    p.click(632, 655)
                    time.sleep(1)
                    p.click(632, 655)
                elif "switch to" in g:
                    y = g.replace("switch to", "")
                    p.click(711, 24)
                    p.click(455, 29)
                    p.write(y)
                    time.sleep(5)
                    p.click(822, 192, clicks=2)
                elif "pause" or "play" in g:
                    p.click(681, 656)
                else:
                    pass
        elif "reminder" in l:
            while True:
                try:
                    say("of how many hours")
                    p = (hear(b, a))
                    print(p)
                    z = int(p[0])
                    say("of how many minutes")
                    q = (hear(b, a))
                    print(q)
                    y = int(q[0:2])
                    print(y)
                    u = (z * 3600) + (y * 60)
                    print(u)
                except:
                    try:
                        say("of how many hours")
                        p = (hear(b, a))
                        print(p)
                        z = int(p[0])
                        say("of how many minutes")
                        q = (hear(b, a))
                        print(q)
                        y = int(q[0:2])
                        print(y)
                        u = (z * 3600) + (y * 60)
                        print(u)
                    except:
                        pass
                else:
                    break
            reminder.remind(u)
        elif "weather" in l:
            say("wait")
            f = l.replace("weather in ", "")
            print(f)
            try:
                v = weather.weather(f)
            except:
                say("not possible right now my bad")
            else:
                say(v)
        elif "shut" in l:
            say("good bye sir")
            exit()
        elif "sleep" in l:
            say(" going to sleep")
            break
        elif "time" in l:
            y = time.strftime("%H hour %M minute")
            say(y)
        elif "date" in l:
            x = datetime.datetime.now()
            y = x.strftime("%B %d %Y")
            say(y)
        elif "joke" in l:
            a12 = random.randint(0,29)
            say(jokes[a12])
            say("hehehehehehehe")
        elif "riddle" in l:
            a13 = random.randint(1,29)
            a76 = list(riddles)
            say(a76[a13])
            while True:
                s13 = hear(b)
                if "repeat" in s13:
                    say(a76[a13])
                elif "answer" in s13:
                    say(riddles.get(a76[a13]))
                    break
                else:
                    pass
        elif "google" in l:
            say("what to search")
            f34 = hear(b,a)
            try:
                pywhatkit.search(f34)
            except:
                say("can't search right now")
           
            while True:
                f45 = hear(b)
                if "search" in f45:
                    f78 = f45.replace("search","")
                    pywhatkit.search(f78)
                elif "image" in f45:
                    p.click(242,172,clicks = 2)
                elif "close" in f45:
                    p.click(1343,0)
                    break
                else:
                    pass
        else:
            say("developers will try to add this function")
