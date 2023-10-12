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

