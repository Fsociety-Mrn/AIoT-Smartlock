import pyrebase
import os
import requests

timeout = 1

# firebase API keys
config = {
  "apiKey": os.environ.get("REACT_APP_FIREBASE_API_KEY"),
  "authDomain": os.environ.get("REACT_APP_FIREBASE_AUTH_DOMAIN"), 
  "databaseURL": "https://aiot-smartlock-default-rtdb.asia-southeast1.firebasedatabase.app", 
  "storageBucket": os.environ.get("REACT_APP_FIREBASE_STORAGE_BUCKET")
}
firebase = pyrebase.initialize_app(config)
db = firebase.database() # realTime database

# read the specific data
def firebaseRead(keyName):
    return db.child(keyName).get().val()

# read the specific data with child
def firebaseReadChild(keyName,valueName):
    try:
        #requests.head("https://www.google.com/", timeout=timeout)
        return bool(db.child(keyName).child(valueName).get().val())
    except requests.ConnectionError:
        print("Walang Internet")
        return False

# update the current data
def firebaseUpdate(keyName, value):
    try:
        db.child(keyName).set(value)
    except:
        #print("Walang Internet")
        return False 
    finally:
        print(db.child(keyName).get().val())
        # print("pumasok sa database")
        return True

def firebaseUpdateChild(keyName,keyChild,value):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        db.child(keyName).child(keyChild).set(value)
       
    except requests.ConnectionError:
        #print("Walang Internet")
        return False
    except:
        return False
    finally:
        return True 

# create data
def firebaseCreate(keyName, value):
    return db.child(keyName).set(value)

# firebaseCreate("Smartlock Status", True)

# verify token User
def firebaseTokenVerify(token):
    try:
        # Read the 'GenerateToken_FacialUpdate' node and check if the token exists
        token_ref = db.child("GenerateToken_FacialUpdate")
        snapshot = token_ref.get()

        if snapshot.exists():
            data = snapshot.val()
            # Check if the token exists in the database
            return data
            # if token in data.values():
            #     # If the token matches, get the name
            #     name = [name for name, tk in data.items() if tk == token][0]
            #     return name
            # else:
            #     return None
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

print(firebaseTokenVerify("swIHY4"))