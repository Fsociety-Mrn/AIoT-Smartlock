import RPi.GPIO as GPIO
from time import sleep
#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
Button = 16
LED = 24
#Setup Button and LED
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    button_state = GPIO.input(Button)
    print(button_state)
    
    print("door is closed") if button_state==1 else print("door is closed")