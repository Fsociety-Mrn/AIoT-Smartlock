from tinydb import TinyDB, Query

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
    query_result = db.all()

    for item in query_result:
        fail_history = item.get(Table_Name, {})
        return len(fail_history)
    
    
    # Offline Insert
    db.close()
    
    return 0
    

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
