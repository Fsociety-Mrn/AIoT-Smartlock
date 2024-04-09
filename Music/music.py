from pygame import mixer 
from time import sleep
import threading


def play_music(file_path,time=1):
    
    sleep(time)
    # Starting the mixer 
    mixer.init() 

    # Loading the song 
    mixer.music.load(file_path) 

    # Setting the volume 
    mixer.music.set_volume(0.8) 

    # Start playing the song 
    mixer.music.play() 

    # Wait for the music to finish
    while mixer.music.get_busy():
        pass

    # Stop the mixer 
    mixer.music.stop()

# # Usage example
# if __name__ == "__main__":
#     mp3_file_path = "Music/Welcome.mp3"
#     play_music(mp3_file_path)


threading.Thread(args=("Music/Welcome.mp3",),target=play_music).start()