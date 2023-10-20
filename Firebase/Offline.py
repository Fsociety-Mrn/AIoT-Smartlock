from tinydb import TinyDB, Query
from Firebase.firebase import firebaseHistory

# Function to create a database and a table
def __create_database_and_table(table_name):
    db = TinyDB("Firebase/offline.json")
    table = db.table(table_name)
    return db, table

# Function to insert data into the table
def offline_insert(TableName, data):
    
    # Create the database and table
    db, table = __create_database_and_table(TableName)
    table.insert(data)
    
    # Offline Insert
    db.close()

# Function to get print 
def total_fail(Table_Name):
    
    db = TinyDB("Firebase/offline.json")
    query_result = db.table(Table_Name).all()
 
    # Offline Insert
    db.close()
    
    return len(query_result)
    
def delete_table(Table_Name):
    db = TinyDB("Firebase/offline.json")    
    
    # Check if the table exists before attempting to delete it
    if Table_Name in db.tables():
        
        print("wala kuys")
        
        # Drop (delete) the specified table
        db.drop_table(Table_Name)
    else:
        print("may error")
        # Close the TinyDB instance
    db.close()

# ******* for History
def offline_history(name=None, date=None, time=None, access_type=None):
    db = TinyDB("Firebase/offline.json")
    table = db.table("History")
    
    data = {
        name:{
            date:{
                time: access_type
            }
        }
    }
    
    table.insert(data)
    
    db.close()
    
def updateToDatabase():
    db = TinyDB("Firebase/offline.json")
    table = db.table("History")

    # Retrieve all records from the table
    records = table.all()
    
    for each in records:
        for name,value in each.items():
            for date, value in value.items():
                for time, access_type in value.items():
                    firebaseHistory(name=name,date=date,time=time,access_type=access_type)
                
        delete_table("History")
        
# ************** PIN LOGIN ************** #
def pinCodeLogin(pin):
    db = TinyDB("Firebase/offline.json")
    table = db.table("PIN")

    # Retrieve all records from the table
    records = table.all()

    pins = pin.split("-")
    
    # Initialize variables to store the name and the first part of the pin
    name_found = None
    first_pin_part = None
    
    for each in records:
        for name,value in each.items():
            for key,values in value.items():
                if (values == pin):
                    
                    name_found = name
                    first_pin_part = pins[0]
                    break  # Exit the innermost loop once we've found a match

    return name_found, first_pin_part

# ************** LOCKERS ************** #
def checkLocker(NAME):
    db = TinyDB("Firebase/offline.json")
    table = db.table("LOCK")

    # Retrieve all records from the table
    records = table.all()

    LockerNumber = 0
    
    for each in records:
        for name,value in each.items():
            if name == NAME:
                LockerNumber = value["Locker Number"]
                
    return LockerNumber
    