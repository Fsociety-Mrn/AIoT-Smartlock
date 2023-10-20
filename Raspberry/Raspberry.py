from Firebase.firebase import firebaseRead
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# SETUP PIN
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

def openLocker():
    data = firebaseRead("LOCK")
    for key,value in data.items():
        OpenLockers(key=int(value['Locker Number']), value=value['Locker Status'])
        
def OpenLockers(key,value):
    GPIO.output(key,value)
    print("Open Lockers")
    print(key,value)