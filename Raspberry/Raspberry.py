from Firebase.firebase import firebaseRead


def openLocker():
    data = firebaseRead("LOCK")
    for key,value in data.items():
        print("Locker Number: ",int(value['Locker Number']))
        print("Locker Status: ",value['Locker Status'])
        print("=============================")