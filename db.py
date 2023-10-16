from tinydb import TinyDB,Query
from Firebase.firebase import firebaseHistoryUpdate,firebaseHistory,firebaseVerifyPincode
from Firebase.Offline import offline_history,offline_insert,pinCodeLogin

def updateToDatabase():
    db = TinyDB("Firebase/offline.json")
    table = db.table("History")

    # Retrieve all records from the table
    records = table.all()
    
    for each in records:
        for name,value in each.items():
            for date, value in value.items():
                for time, access_type in value.items():
                    print("--------------------")
                    print(name)
                    print(date)
                    print(time)
                    print(access_type)
                    firebaseHistory(name=name,date=date,time=time,access_type=access_type)

data = pinCodeLogin("00-1010")

print(data[0],data[1])



