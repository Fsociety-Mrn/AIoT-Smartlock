from tinydb import TinyDB

from Firebase.Offline import delete_table

# Create or open the database
db = TinyDB('Firebase/offline.json')

# # Insert your JSON data into the database
# data = {
#     "Fail History": {
#         "1": {"Fail": "Facial Failure"},
#         "2": {"Fail": "Facial Failure"},
#         "3": {"Fail": "Facial Failure"}
#     }
# }
# db.insert(data)

# Query and print the "Fail" values



delete_table("Fail History")

# Close the database
db.close()