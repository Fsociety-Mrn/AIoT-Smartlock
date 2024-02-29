from Firebase.firebase import firebaseRead, lockerUpdate
from Firebase.Offline import save_firebase_data_to_json,view_firebase_data_in_json
# import RPi.GPIO as GPIO
import time
import threading
import requests

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# batch_one_locker = [21,20,16,12,7,8,25]
# batch_one_doorSensor = [26,19,13,6,5,8,11]

# for number in batch_one_locker:
#     GPIO.setup(number,GPIO.OUT)
#     GPIO.output(number,True)
    
# for pin in batch_one_doorSensor:
#     GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Open the Locker Remotely
def openLocker():
    try:
        data_firebase = firebaseRead("LOCK")

        if not data_firebase == False:
            save_firebase_data_to_json(TableName="LOCK", data=data_firebase)
            
        data = view_firebase_data_in_json("LOCK")

        for key,value in data:
            if key and value['Locker Number'] and value['Locker Status']:
                
                lockerUpdate(name=key, value=False)
                
                threading.Thread(target=OpenLockers, args=(key, int(value['Locker Number']),value['Locker Status'],)).start()
 
    except Exception as e:
        print("Open Locker: ", e)
        
def gpio_manual(key,value):
    print(key,value)
    # GPIO.output(int(key),value)
    
def OpenLockers(name,key,value):

    if value:
        print("Open Lockers: ")
        print(name,value)
        
        # gpio_manual(int(key),GPIO.LOW)
        time.sleep(2)
        # gpio_manual(int(key),GPIO.HIGH)
        
        print("Open Lockers: ")
        print(name,False)
        
def door_status(pin):
    # door = True if GPIO.input(pin) == GPIO.LOW else False
    # return not GPIO.input(pin)

    return True
