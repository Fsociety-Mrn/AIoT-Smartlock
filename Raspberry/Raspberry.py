from Firebase.firebase import firebaseRead, lockerUpdate
import RPi.GPIO as GPIO
import time
import threading
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

batch_one_locker = [21,20,16,12,7,8,25]
batch_one_doorSensor = [26,19,13,6,5,8,11]

for number in batch_one_locker:
    GPIO.setup(number,GPIO.OUT)
    GPIO.output(number,True)
    
for pin in batch_one_doorSensor:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def openLocker():
    try:
        requests.head("https://www.google.com/", timeout=1)
        data = firebaseRead("LOCK")
        
        for key,value in data.items():
                        
            if key: 
                threading.Thread(target=OpenLockers, args=(key, int(value['Locker Number']),value['Locker Status'],)).start()
    
    except Exception as e:
        print("Error Open Locker: ", e)
        
def gpio_manual(key,value):
    print(key,value)
    GPIO.output(int(key),value)
    
def OpenLockers(name,key,value):

    if value:
        print("Open Lockers: ")
        print(key,value)
        
        gpio_manual(int(key),GPIO.LOW)
        time.sleep(2)
        gpio_manual(int(key),GPIO.HIGH)
        
        lockerUpdate(name=name, value=False)
        
def door_status(pin):
    door = True if GPIO.input(pin) == GPIO.LOW else False
    return door

    # return False
