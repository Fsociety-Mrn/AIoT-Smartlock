from tinydb import TinyDB, Query
import json
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
        
        print("Ture")
        
        # Drop (delete) the specified table
        db.drop_table(Table_Name)
    else:
        print("false")
        # Close the TinyDB instance
    db.close()


def offline_history(name=None, date=None, time=None, access_type=None):
    db = TinyDB("Firebase/test.json")
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
    

def retrieve_data_from_tinydb():
    db = TinyDB("Firebase/test.json")
    table = db.table("History")

    # Retrieve all records from the table
    records = table.all()

    json_data_list = []

    for record in records:
        json_data_list.append(record)
        


    db.close()
    
    return json_data_list
