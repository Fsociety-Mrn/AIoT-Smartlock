import playsound
from gtts import gTTS
import time

def speak(text):
    tts =gTTS(text=text,lang="en")
    
    filename="Sounds/helloFriend.mp3"
    tts.save(filename)

    playsound.playsound(filename)

    
speak(""".Verify that you have both the gTTS and playsound libraries installed. You can use the pip show command to check their versions and installation status.
Confirm that the "helloFriend.mp3" file is being saved in the expected directory. You can print the absolute file path before playing it to ensure it is correct.""")
