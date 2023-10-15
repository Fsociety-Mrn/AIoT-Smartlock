from tinydb import TinyDB
from Firebase.firebase import firebaseHistoryUpdate
from Firebase.Offline import offline_history

def retrieve_data_from_tinydb():
    db = TinyDB("Firebase/test.json")
    table = db.table("History")

    # Retrieve all records from the table
    records = table.all()
    
    return records
    
data = retrieve_data_from_tinydb()

for each in data:
    for key,value in each.items():
        print(key, value)
        firebaseHistoryUpdate(key,value)
    

# offline_history(name="Lisboa,Art", date="Oct 15 2023", time="7:35 AM", access_type="Access Granted")