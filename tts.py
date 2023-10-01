import playsound
from gtts import gTTS
import time

def speak(text):
    tts =gTTS(text=text,lang="en")
    
    filename="Sounds/please blink.mp3"
    tts.save(filename)

    playsound.playsound(filename)

    
speak("Authenticated")

