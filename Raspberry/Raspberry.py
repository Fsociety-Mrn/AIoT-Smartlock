from Firebase.firebase import firebaseRead
# import RPi.GPIO as GPIO
import time
import threading

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# # SETUP PIN
# GPIO.setup(21,GPIO.OUT)
# GPIO.setup(20,GPIO.OUT)
# GPIO.setup(16,GPIO.OUT)
# GPIO.setup(12,GPIO.OUT)
# GPIO.setup(7,GPIO.OUT)
# GPIO.setup(8,GPIO.OUT)
# GPIO.setup(25,GPIO.OUT)
# GPIO.setup(24,GPIO.OUT)
# GPIO.setup(23,GPIO.OUT)
# GPIO.setup(18,GPIO.OUT)

def openLocker():
    data = firebaseRead("LOCK")
    for key,value in data.items():
        # OpenLockers(key=int(value['Locker Number']), value=value['Locker Status'])
        threading.Thread(target=OpenLockers, args=(int(value['Locker Number']),value['Locker Status'],)).start()
        
def OpenLockers(key,value):

    if value:
        print("Open Lockers")
        print(key,value)
        
        # GPIO.output(key,value)
        time.sleep(1)
        # GPIO.output(key,GPIO.LOW)
        
        print(key,False)
        
# GPIO.cleanup()