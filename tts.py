import playsound
from gtts import gTTS
import time

def speak(text):
    tts =gTTS(text=text,lang="en")
    
    filename="Sounds/Access Denied.mp3"
    tts.save(filename)

    playsound.playsound(filename)

    
speak("Access Denied! use pin code if you are not recognize")
