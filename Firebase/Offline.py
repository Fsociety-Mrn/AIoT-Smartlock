from tinydb import TinyDB
from Firebase.firebase import firebaseHistory
from datetime import datetime,timedelta

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
        
        print("delete_table: wala kuys")
        
        # Drop (delete) the specified table
        db.drop_table(Table_Name)
    else:
        print("Offline: delete_table")
        # Close the TinyDB instance
    db.close()

# ******* for History
def offline_history(name=None, date=None, time=None, access_type=None, Percentage=None):
    db = TinyDB("Firebase/offline.json")
    table = db.table("History")
    
    data = {
        name:{
            date:{
                time: 
                    {
                        "Access_type" : access_type,
                        "Percentage"  : Percentage
                    },
            }
        }
    }
    
    table.insert(data)
    
    db.close()
    
def updateToDatabase():
    
    try:

        
        db = TinyDB("Firebase/offline.json")
        table = db.table("History")

        # Retrieve all records from the table
        records = table.all()
    
        for each in records:
            for name,value in each.items():
                for date, value in value.items():
                    for time, access_type in value.items():
                    
                    # I-convert ang dictionary sa listahan ng mga tuples
                        key_value_list = [(key, value) for key, value in access_type.items()]
           
                        firebaseHistory(name=name,
                                    date=date,
                                    time=time,
                                    access_type=key_value_list[0][1],
                                    percentage=key_value_list[1][1])
                
            delete_table("History")
    except Exception as e:
        pass
        print("error")
        
# ************** PIN LOGIN ************** #
def pinCodeLogin(pin):
    
    try:
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
    except:
        return "None", "0"

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

# ************** SPAM RECOGNITION ************** #
def __insert_person_permanent_banned(personID):

    db = TinyDB("Firebase/banned_and_temporary_list.json")
    table = db.table("permanent_banned")
    table.insert({ "name": personID })
    
def __insert_date_and_time(personID):
    
    # Create a TinyDB instance and open the database file
    db = TinyDB("Firebase/banned_and_temporary_list.json")
    
    # Get the current date and time with formatted date add 1 minute
    current_datetime = datetime.now()

    formatted_datetime = current_datetime.strftime("%b %d %Y at %I:%M %p")
    
    # Get the table or create it if it doesn't exist
    table = db.table(personID)
    
    table.insert( {"date": formatted_datetime})
    
    return False
    

def check_person_banned(personID):
    db = TinyDB("Firebase/banned_and_temporary_list.json")
    table = db.table("permanent_banned")

    # Retrieve all records from the table
    records = table.all()
    
    for each in records:
        for name,value in each.items():
            if value==personID:
                return True

    return False

def is_person_temporary_banned(personID):
    db = TinyDB("Firebase/banned_and_temporary_list.json")
    table = db.table(personID)

    # Retrieve a ll records from the table
    records = table.all()
    
    for each in records:
        for key,date in each.items():
            print(date)
    
    # default value
    value = False
    
    if len(records) == 3:
        value = True
    
    if len(records) == 6:
        value = True
    
    if len(records) == 9:
        __insert_person_permanent_banned(personID)
        return True
    
    __insert_date_and_time(personID)
    return value



