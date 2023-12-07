from Firebase.firebase import firebaseRead, lockerUpdate
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = [21,20,16,12,7,8]

for number in PIN:
    GPIO.setup(number,GPIO.OUT)
    GPIO.output(number,GPIO.LOW)

def openLocker():
    try:
        data = firebaseRead("LOCK")
        for key,value in data.items():
        # print("KEY",key)
        # OpenLockers(key=int(value['Locker Number']), value=value['Locker Status'])
            if key: 
                threading.Thread(target=OpenLockers, args=(key, int(value['Locker Number']),value['Locker Status'],)).start()
    except:
        print("Error Open Locker")
        
        
def OpenLockers(name,key,value):

    if value:
        print("Open Lockers")
        print(key,value)
        
        GPIO.output(int(key),value)
        time.sleep(2)
        GPIO.output(int(key),GPIO.LOW)
        
        lockerUpdate(name=name, value=False)
        
        print(key,False)
        
# GPIO.cleanup()