from pyttsx3 import *
def bol(a):
    c = init()
    c.say(a)
    c.runAndWait()
    c.stop()
import speech_recognition as s
r = s.Recognizer()
print("Say Something...")
bol("Say Something...")
with s.Microphone()as m:
    audio = r.listen(m)
    while True:
        try:
            query = r.recognize_google(audio)
        except:
            print("Speak Again.....")
            bol("Speak Again")
            audio = r.listen(m)
            try:
                query = r.recognize_google(audio)
            except:
                pass
        else:
            break
            
    print(query)
bol(query)










