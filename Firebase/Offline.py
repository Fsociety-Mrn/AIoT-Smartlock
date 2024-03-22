import requests

from tinydb import TinyDB,Query
from Firebase.firebase import firebaseHistory,firebaseUpdateChild,firebaseRemove
from datetime import datetime,timedelta


# Function to create a database and a table
def __create_database_and_table(table_name):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json")
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
    
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json")
    query_result = db.table(Table_Name).all()
 
    # Offline Insert
    db.close()
    
    return len(query_result)
    
def delete_table(Table_Name=None,dir="/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json"):
    db = TinyDB(dir)    
    
    # Check if the table exists before attempting to delete it
    if Table_Name in db.tables():
        
        print(f"delete_table: table delete {Table_Name}")
        
        # Drop (delete) the specified table
        db.drop_table(Table_Name)
    else:
        print(f"delete_table: {Table_Name} not found")
        # Close the TinyDB instance
    db.close()

# ******* for History
def offline_history(name=None, date=None, time=None, access_type=None, Percentage=None):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json")
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
        
        db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json")
        table = db.table("History")
        

        # Check if the table exists before attempting to delete it        
        if not "History" in db.tables():
            print("History not exist: ", False)
            return 
        
        requests.head("https://www.google.com/", timeout=2)
        
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
            
    except requests.exceptions.Timeout:
        print("updateToDatabase: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"updateToDatabase: Request failed - {e}")
        return None
    except Exception as e:
        pass
        print(f"updateToDatabase: {e}")
        return None
        
# ************** PIN LOGIN ************** #
def pinCodeLogin(pin):
    
    try:
        db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json")
        table = db.table("PIN")

        # Retrieve all records from the table
        records = table.all()

        pins = pin.split("-")
    
        # Initialize variables to store the name and the first part of the pin
        name_found = None
        first_pin_part = "0"
    
        for each in records:
            for name,value in each.items():
                for key,values in value.items():
                    if (values == pin):
                    
                        name_found = name
                        first_pin_part = pins[0]
                        break  # Exit the innermost loop once we've found a match

        return name_found, first_pin_part
    except:
        return None, "0"

# ************** LOCKERS ************** #
def checkLocker(NAME):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/offline.json")
    table = db.table("LOCK")

    # Retrieve all records from the table
    records = table.all()

    LockerNumber = 0
    
    for each in records:
        for name,value in each.items():
            if name == NAME:
                LockerNumber = value["Locker Number"]
                
    return LockerNumber

def save_firebase_data_to_json(TableName,data):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/firebase_data.json")
    
    # Check if the table exists before attempting to delete it
    if TableName in db.tables():
        db.drop_table(TableName)
        
    table = db.table(TableName) 
    table.insert(data)
    
def insert_into_json(TableName=None, name=None,data=None):
    # Load the TinyDB database
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/insert_firebase_data.json")
    table = db.table(TableName)
    
    # Check if the name already exists in the table
    query = Query()
    existing_data = table.search(query.name == name)
    
    # If the name exists, update the existing record; otherwise, insert a new record
    if not existing_data:
        table.insert({"name": name})
        # print(f"Data for {name} inserted successfully.") 
        return
    
    # Assuming each name is unique, updating the first occurrence
    table.update(data, query.name == name)
    # print(f"Data for {name} updated successfully.")
    
def view_data_in_json(TableName):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/insert_firebase_data.json")
    table = db.table(TableName)
    
    return table.all()

def view_firebase_data_in_json(TableName):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/firebase_data.json")
    table = db.table(TableName)
    
    return table.all()[0].items()


    # Iterate over each key in the "LOCK" dictionary
    # for Name, value in table.all()[0].items():
    #     print()
    #     print(f"{Name}:")
    #     print("Locker Number: ",value['Locker Number'])
    #     print("Locker Status: ",value['Locker Status'])
     

# ************** SPAM RECOGNITION ************** #
def __insert_person_permanent_banned(personID):

    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
    table = db.table("permanent_banned")
    table.insert({ "name": personID })
    
def __insert_date_and_time(personID):
    
    if personID == None:
        return
    
    # Create a TinyDB instance and open the database file
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
    
    # Get the current date and time with formatted date add 2 minute
    current_datetime = datetime.now() + timedelta(minutes=2)

    formatted_datetime = current_datetime.strftime("%b %d %Y at %I:%M %p")
    
    # Get the table or create it if it doesn't exist
    table = db.table(personID)
    
    table.insert( {"date": formatted_datetime})

def __is_date_expired(records,date):
    # NOTE: return True if date is not yet expired else False
    try:

        date_string = records[date]['date']
        
        # Convert the date string to a datetime object
        date_format = "%b %d %Y at %I:%M %p"
        date = datetime.strptime(date_string, date_format)
    
        # Get the current datetime
        current_date = datetime.now()
    
        # Compare if the date is in the past
        return date >= current_date
    
    except Exception as e:
        print("error")
        return False
    
def check_person_banned(personID):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
    table = db.table("permanent_banned")

    # Retrieve all records from the table
    records = table.all()
    
    for each in records:
        for name,value in each.items():
            if value==personID:
                db.drop_table(personID)
                return True

    return False

def is_person_temporary_banned(personID,insert):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
    table = db.table(personID)

    # Retrieve a ll records from the table
    records = table.all()
    
    if len(records) == 3 and __is_date_expired(records,2):
        return False

    if len(records) == 6 and __is_date_expired(records,5):
        return False
    
    if len(records) == 9:
        __insert_person_permanent_banned(personID)
        return False
    
    if insert:
        __insert_date_and_time(personID)
    return True

def create_person_temporarily_banned(Person_ID=None,error="PIN",insert=True):
    
    # check if person is permanent banned
    if check_person_banned(Person_ID):
        text= f""" You have been temporarily suspended due to multiple unauthorized access attempts. please contact support for further assistance. 
        your suspended ID: {Person_ID}
            """
        return text,True

    # check if person is temporary banned
    if is_person_temporary_banned(Person_ID,insert):
        return f"Access Denied\nFor smoother access, try {error} Login or use our AIoT Smartlock website for remote unlocking. If you haven't registered your face, please register it. If already registered, ensure your facial biometrics is up to date.",False

    return 'You have multiple unauthorized access attempts.\nPlease return in a minute.',True

def upload_to_firebase_banned():
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
    table = db.table("permanent_banned")
    
    # Retrieve all records from the table
    records = table.all()
    
    firebaseRemove(keyName="suspended")
    for each in records:
        firebaseUpdateChild(keyName="suspended",keyChild=each['name'],value=True)

def delete_person_from_JSON(name_to_delete):
    db = TinyDB("/home/aiotsmartlock/Downloads/AIoT_Smart-lock/Firebase/banned_and_temporary_list.json")
    banned_table = db.table('permanent_banned')
    Person = Query()

    # Find and delete the person with the specified name
    banned_table.remove(Person.name == name_to_delete)

    db.close()
