import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("Firebase/secret.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://aiot-smartlock-default-rtdb.asia-southeast1.firebasedatabase.app/?offline=True"
})

ref = db.reference("/")

print(ref.get())