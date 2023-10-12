from tinydb import TinyDB

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
query_result = db.all()

for item in query_result:
    fail_history = item.get("Fail History", {})
    for test_num, test_data in fail_history.items():
        fail_reason = test_data.get("Fail")
        if fail_reason:
            print(f"Test {test_num}: {fail_reason}")

# Close the database
db.close()
