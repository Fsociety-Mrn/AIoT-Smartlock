import pyrebase
import os
import requests
from datetime import datetime

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

# verify token User
def firebaseTokenVerify(token):
    try:
        data = db.child("GenerateToken_FacialUpdate").get().val()
        
              
        # If the token matches, get the name
        name = [name for name, tk in data.items() if tk == token][0]
        return name
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# delete token after it verify
def firebaseDeleteVerifiedToken(name=None):
    try:
        # Delete the specific field
        db.child("GenerateToken_FacialUpdate").child(name).remove()
        print("field deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)

# add Facial/ Pincode Login
def firebaseHistory(name=None, date=None, time=None, access_type=None, percentage=None):
    
    try:    
        # Push the new entry to the database under the specified name, date, and time
        db.child("History").child(name).child(date).child(time).set(
            {
                "Access_type": access_type,
                "Percentage" : percentage
            })

        return True
    except:
        # offline_history(name=None, date=None, time=None, access_type=None)
        return False

# add Facial/ Pincode Login
def firebaseHistoryUpdate(key,data):
    try:    
        requests.head("http://www.google.com/", timeout=timeout)
        
        # Push the new entry to the database under the specified name, date, and time
        db.child("History").child(key).update(data)

        return True
    except:
        print("error")
        return False

# verify pincode
def firebaseVerifyPincode(username=None, pincode=None):
    try:
        user_data = db.child("PIN").get().val()
        for key, value in user_data.items():
            if str(value["username"]) == username and str(value["pincode"]) == pincode:
                return key  # Ibalik ang pangalan ng key (hal. "Name" o "Name2") na nauugnay sa username at pincode
        
        return None
    except Exception as e:
        print("Error:", e)
        return None
    
# verify pincode
def firebaseVerifyPincode():
    try:
        user_data = db.child("PIN").get().val()
        data = []
        for name,valuesss in user_data.items():

            data.append({name:valuesss})
        return data
            
    except Exception as e:
        print("Error:", e)
        return None
    
def lockerList():
    try:
        user_data = db.child("LOCK").get().val()
        data = []
        for name,valuesss in user_data.items():

            data.append({name:valuesss})
        return data
            
    except Exception as e:
        print("Error:", e)
        return None
# print(firebaseVerifyPincode(username="artlisboa", pincode="1010"))


# print("Name: ",firebaseTokenVerify("MggPBs"))

# result = firebaseTokenVerify("MggPBss")
# if not result == None:
#     print("goods")
# else:
#     print("not goods")

# res = update_realtime_database(name="Lisboa,Art", date="June 19 2023", time="7:07 AM", access_type="ACCESS DENIED")
# print(res)


# firebaseDeleteVerifiedToken("For,Testing")

def firebaseHistoryUpdate(key,data):
    try:    
        # Push the new entry to the database under the specified name, date, and time
        db.child("History").child(key).update(data)

        return True
    except:
        print("error")
        return False
    
# ************************* CHECK LOCK ************************* #
def firebaseCheckLock():
    try:
        data = db.child("AIoT Lock").child("isLock").get().val()
        
        if data:
            print("GAGSTI MAY LAMAN") 
            return True
        else:
            firebaseSetLock(isLock=True)
            print("walang laman")
            return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    

def firebaseSetLock(isLock=None):
    try:    
        # Push the new entry to the database under the specified name, date, and time
        db.child("AIoT Lock").child("isLock").set(isLock)
        return True
    except:
        # offline_history(name=None, date=None, time=None, access_type=None)
        return False
    
# ************************* delete token after it verify ************************* #
def firebaseDeleteToken():
    try:
        # Delete the specific field
        db.child("AIoT Lock").child("data").remove()
        print("field deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)
    
def firebaseTokenLOCK(token):
    try:
        data = db.child("AIoT Lock").child("data").child("token").get().val()
    
        if str(data) == str(token):
            print("Goodshit")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error: {e}")
        return False

def firebase_check_expiration():
    try:
        expiration_data = db.child("AIoT Lock").child("data").child("expiration").get().val()

        # Assuming the format of expiration_data is as mentioned in your example
        expiration_date_str = expiration_data['date'] + ' ' + expiration_data['time']
        expiration_datetime = datetime.strptime(expiration_date_str, '%b %d %Y %I:%M:%S %p')

        current_datetime = datetime.now()

        if current_datetime > expiration_datetime:
            print("Expiration date and time have passed.")
            return True
        else:
            print("Expiration date and time are still valid.")
            return False
    
    except Exception as e:
        print(f"Error: {e}")
        return True
    
def lockerUpdate(name,value):
    try:
       db.child("LOCK").child(name).child("Locker Status").set(value)
       return True
            
    except Exception as e:
        print("Error:", e)
        return None
    
def firebase_set_unlock(value):
    try:
       db.child("AIoT Lock").child("isLock").set(value)
       return True
            
    except Exception as e:
        print("Error:", e)
        return None
