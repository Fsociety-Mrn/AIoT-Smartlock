import playsound
from gtts import gTTS
import time

def speak(text):
    tts =gTTS(text=text,lang="en")
    
    filename="pages/Access Granted.mp3"
    tts.save(filename)

    playsound.playsound(filename)

    
speak("Authenticated")

