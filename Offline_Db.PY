from tinydb import TinyDB, Query

# Function to create a database and a table
def create_database_and_table(db_filename, table_name):
    db = TinyDB(db_filename)
    table = db.table(table_name)
    return db, table

# Function to insert data into the table
def insert_data(table, data):
    table.insert(data)

# Function to query data from the table
def query_data(table, query_condition):
    User = Query()
    result = table.search(query_condition)
    return result

# Function to update data in the table
def update_data(table, query_condition, update_values):
    table.update(update_values, query_condition)

# Function to delete data from the table
def delete_data(table, query_condition):
    table.remove(query_condition)

# Function to close the database
def close_database(db):
    db.close()

# Main program
if __name__ == '__main__':
    # Create the database and table
    db, table = create_database_and_table('Firebase/my_database.json', 'my_table')

    # Insert data into the table
    data = {'name': 'John', 'age': 30}
    insert_data(table, data)

    # Query data from the table
    result = query_data(table, Query().name == 'John')
    print("Query Result:", result)

    # Update data in the table
    update_data(table, Query().name == 'John', {'age': 31})
    result = query_data(table, Query().name == 'John')
    print("Updated Query Result:", result)

    # Delete data from the table
    delete_data(table, Query().name == 'John')

    # Close the database
    close_database(db)
