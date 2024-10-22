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


# remove key
def firebaseRemove(keyName):
    try:
        requests.head("https://www.google.com/", timeout=1)
        # if not response.status_code == 200:
        #     print(f"Request failed with status code: {response.status_code}")
            
        # print(f"Request successful: {response.status_code}")
 
        return db.child(keyName).remove()
    except requests.exceptions.Timeout:
        print("firebaseRemove: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"firebaseRemove: Request failed - {e}")
        return False
    
# read the specific data
def firebaseRead(keyName):    
    try:
        requests.head("https://www.google.com/", timeout=1)
        # if not response.status_code == 200:
        #     print(f"Request failed with status code: {response.status_code}")
            
        # print(f"Request successful: {response.status_code}")
 
        return db.child(keyName).get().val()
    except requests.exceptions.Timeout:
        print("firebaseRead: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"firebaseRead: Request failed - {e}")
        return False
    except Exception as e:
        pass
        print(f"firebaseRead: keyname is not existed")
        return False

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
        return False 

def firebaseUpdateChild(keyName,keyChild,value):
    try:
        requests.head("http://www.google.com/", timeout=3)
        db.child(keyName).child(keyChild).set(value)
        return True
    except requests.exceptions.Timeout:
        pass
        print("firebaseUpdateChild: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        pass
        print(f"firebaseUpdateChild: Request failed - {e}")
        return False
    except:
        pass
        return False
    finally:
        return True 

# create data
def firebaseCreate(keyName, value):
    return db.child(keyName).set(value)

# verify token User
def firebaseTokenVerify(token):
    try:
        requests.head("http://www.google.com/", timeout=3)
        data = db.child("GenerateToken_FacialUpdate").get().val()
        

        for Name,data in data.items():
            print(Name)
            
            if not data['TOKEN'] == token:
                print("Token Expired")
                return None,False
            
            # Convert expiration date and time strings to datetime objects
            expiration_datetime = datetime.strptime(data['EXPIRATION']['date'] + " " + data['EXPIRATION']['time'], "%b %d %Y %I:%M:%S %p")
        
            # Get the current date and time
            current_datetime = datetime.now()

            # Check if expiration date and time have passed
            if expiration_datetime < current_datetime:
                print("Token for {} has expired.".format(Name))
                return None,False
            
            # filter date if expired
            print(expiration_datetime)
            print(current_datetime)
            
            return Name,False

            
        # If the token matches, get the name
        # name = [name for name, tk in data.items() if tk == token][0]
        # return name,False
    except requests.exceptions.Timeout:
        pass
        print("firebaseTokenVerify: Request timed out")
        return None,True
    except requests.exceptions.RequestException as e:
        pass
        print(f"firebaseTokenVerify: Request failed - {e}")
        return None ,True   
    except Exception as e:
        print(f"Error: {e}")
        pass
        return None,False

# delete token after it verify
def firebaseDeleteVerifiedToken(name=None):
    try:
        # Delete the specific field
        db.child("GenerateToken_FacialUpdate").child(name).remove()
        print("field deleted successfully.")
    except Exception as e:
        pass
        print("An error occurred:", e)

# add Facial or Pin code Login
def firebaseHistory(name=None, date=None, time=None, access_type=None, percentage=None):
    
    try:    
        requests.head("http://www.google.com/", timeout=timeout)
        
        # Push the new entry to the database under the specified name, date, and time
        db.child("History").child(name).child(date).child(time).set(
            {
                "Access_type": access_type,
                "Percentage" : percentage
            })

        return True
    
    except requests.exceptions.Timeout:
        print("firebaseHistory: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"firebaseHistory: Request failed - {e}")
        return False
    except:
        pass
        # offline_history(name=None, date=None, time=None, access_type=None)
        return False

# add Facial or Pincode Login
def firebaseHistoryUpdate(key,data):
    try:    
        requests.head("http://www.google.com/", timeout=timeout)
        
        # Push the new entry to the database under the specified name, date, and time
        db.child("History").child(key).update(data)

        return True
    
    except requests.exceptions.Timeout:
        print("firebaseHistoryUpdate: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"firebaseHistoryUpdate: Request failed - {e}")
        return False
    
    except:
        print("error")
        pass
        return False

# verify pincode
def firebaseVerifyPincode(username=None, pincode=None):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        
        user_data = db.child("PIN").get().val()
        for key, value in user_data.items():
            if str(value["username"]) == username and str(value["pincode"]) == pincode:
                return key  # Ibalik ang pangalan ng key (hal. "Name" o "Name2") na nauugnay sa username at pincode
        
        return None
    
    except requests.exceptions.Timeout:
        print("firebaseVerifyPincode: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"firebaseVerifyPincode: Request failed - {e}")
        return None
    
    except Exception as e:
        print("Error:", e)
        pass
        return None
    
# verify pincode
def firebaseVerify_Pincode():
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        
        user_data = db.child("PIN").get().val()
        data = []
        for name,value in user_data.items():

            data.append({ name:value })
        return data
    
    except requests.exceptions.Timeout:
        print("firebaseVerifyPincode: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"firebaseVerifyPincode: Request failed - {e}")
        return None
    
    except Exception as e:
        print("firebaseVerifyPincode:", e)
        pass
        return None
    
def lockerList():
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        
        user_data = db.child("LOCK").get().val()
        data = []
        for name,value in user_data.items():

            data.append({ name: value})
        return data
    
    except requests.exceptions.Timeout:
        print("lockerList: Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"lockerList: Request failed - {e}")
        return None         
    except Exception as e:
        print("lockerList:", e)
        pass
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
        pass
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
        pass
        return False
    

def firebaseSetLock(isLock=None):
    try:    
        # Push the new entry to the database under the specified name, date, and time
        db.child("AIoT Lock").child("isLock").set(isLock)
        return True
    except:
        pass
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
        pass
    
def firebaseTokenLOCK(token):
    try:
        data = db.child("AIoT Lock").child("data").child("token").get().val()
    
        if str(data) == str(token):
           
            return True
        
        return False
    
    except Exception as e:
        print(f"Error: {e}")
        pass
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
        pass
        return True
    
def lockerUpdate(name,value):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        
        db.child("LOCK").child(name).child("Locker Status").set(value)
        return True
    
    except requests.exceptions.Timeout:
        print("lockerUpdate: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"lockerUpdate: Request failed - {e}")
        return False
            
    except Exception as e:
        print("lockerUpdate:", e)
        pass
        return False
    
def firebase_set_unlock(value):
    try:
       db.child("AIoT Lock").child("isLock").set(value)
       return True
            
    except Exception as e:
        print("Error:", e)
        pass
        return None
    
def locker_sensor(keyName,value):
    try:
        
        db.child("Locker").child(keyName).set(value)
        return True
            
    except Exception as e:
        print("locker_sensor:", e)
        pass
        return False


# data = firebaseTokenVerify("VWAJEI")

# print(data)