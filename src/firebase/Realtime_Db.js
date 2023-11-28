
import TokenGenerator from "../Components/TokenGenerator";
import { RTdb } from "./FirebaseConfig"
import { 
    ref,  
    onValue, 
    remove,
    set
} from "firebase/database";

// **************** for Token Users **************** //

// verify token users
export const verifyToken = (TOKENs) => {
    return new Promise((resolve, reject) => {
      const dbRef = ref(RTdb, 'GenerateToken_User');
  
      onValue(dbRef, (snapshot) => {
        const data = snapshot.val();
  
        if (data) {
          let isValid = false;
  
          Object.entries(data).forEach(([key, value]) => {
            try {
              if (value === TOKENs) {
                console.log(`Data with key ${key} is valid.`);
                removeKey(key);
                isValid = true;
              } else {
                console.log(`Invalid key`);
                isValid = false;
              }
            } catch (error) {
              console.error(`Error removing key "${key}":`, error);
              resolve(false);
            }
          });
  
          resolve(isValid); // Resolve the Promise with the validity status
        } else {
          console.log('No data found');
          resolve(false); // Resolve the Promise with false if no data is found
        }
      }, {
        onlyOnce: true // Optional: Ma-trigger lamang ng isang beses
      });
    });
};

// remove token Key
export const removeKey = (key) => {
    const keyRef = ref(RTdb, `GenerateToken_User/${key}`);
  
    remove(keyRef)
      .then(() => {
        console.log(`Key "${key}" removed successfully.`);
      })
      .catch((error) => {
        console.error(`Error removing key "${key}":`, error);
      });
};

// generate a token
export const generateToken = async () => {
  try {
      const Token = TokenGenerator()

      // Get the current date and time
      const currentDate = new Date();

      // Add 3 hours to the current time
      const newDate = new Date(currentDate.getTime() + 3 * 60 * 60000); // 3 hours in milliseconds

      const dateOptions = {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      };
  
      const timeOptions = {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true,
      };

      const formattedDate = String(currentDate.toLocaleString('en-US', dateOptions)).replace(",", "");
      const formattedTime = newDate.toLocaleString('en-US', timeOptions);

      const data = {
        OTP: Token,
        EXPIRATION: {
          date: formattedDate,
          time: formattedTime
        }
      }

    const tokensList = await getListOFTokens(); // Assuming getListOFTokens() returns a list of tokens
    set(ref(RTdb, 'GenerateToken_User/' + tokensList),data);
    alert("🎉 One-Time Password (OTP) for signing up has been generated! 🚀");

  } catch (err) {
    console.error(err);
  }
}

const getListOFTokens = () => {
  const dbRef = ref(RTdb, 'GenerateToken_User');

  return new Promise((resolve, reject) => {
    onValue(dbRef, (snapshot) => {
      const data = snapshot.val();
      if (data && typeof data === 'object') {
        const numberOfTokens = Object.keys(data).length;
        resolve(numberOfTokens);
      } else {
        // Handle the case when data is null or not an object
        resolve(0); // Return 0 tokens or any default value as per your requirement
      }
    }, (error) => {
      reject(error);
    });
  });
  
}

// **************** AIoT Lock**************** //

// Push to AIoT Token For unlock
export const AIoT_unlock = async (data) => {
  return new Promise(async (resolve, reject) => {

    const dbRef = ref(RTdb, `AIoT Lock/data`);

    try {
      set(dbRef, data)
      resolve("OTP is created")
    } catch (err) {
      reject("OTP not created")
    }

  });
}

export const get_AIoT_unlock = async () =>{
  const dbRef = ref(RTdb, 'AIoT Lock');

  return new Promise((resolve, reject) => {
    onValue(dbRef, (snapshot) => {
      const data = snapshot.val();
      resolve(data)
    }, (error) => {
      reject(error);
    });
  });
}

// remove token Key
export const remove_token_data = () => {
    const keyRef = ref(RTdb, `AIoT Lock/data`);
  
    remove(keyRef)
      .then(() => {
        console.log(`removed successfully.`);
      })
      .catch((error) => {
        console.error(`Error removing:`, error);
      });
};

// **************** Open the Locker **************** //
export const openLocker = async (props) => {
  try {
      const keyRef = ref(RTdb, `LOCK/${props.FullName}/`);
      
      const data ={
          "Locker Status": props.value,
          "Locker Number": props.number
      }
      set(keyRef,data);

  } catch (err) {
      console.error(err);
  }
}

// **************** generate a token and Remove Token **************** //
export const pushToken = async (props) => {
  try {
      set(ref(RTdb, 'GenerateToken_FacialUpdate/' + props.FullName),String(props.Code));
  } catch (err) {
      console.error(err);
  }
}

export const removeToken = (FullName) => {
  const keyRef = ref(RTdb, `GenerateToken_FacialUpdate/${FullName}`);

  remove(keyRef)
      .then(() => {
          console.log(FullName)
          console.log(`Key "${FullName}" removed successfully.`);
      })
      .catch((error) => {
          console.error(`Error removing key "${FullName}":`, error);
      });
};

// **************** createPIN setup **************** //
export const checkPin = (FullName) => {
  return new Promise((resolve, reject) => {
      try {
          const dbRef = ref(RTdb, `PIN/${FullName}`);
          onValue(dbRef, (snapshot) => {
              const data = snapshot.val();

              data ? resolve(false) : resolve(true)
          }, (error) => {
          reject(error);
    });
  }catch(error){
      reject(error);
  }
  });
}

export const verifyPIN = (FullName,PIN) => {
  return new Promise((resolve, reject) => {
      try {

          const dbRef = ref(RTdb, `PIN/${FullName}`);
          onValue(dbRef, (snapshot) => {
              const data = snapshot.val();
        
              resolve(data.pincode.split("-")[1] === PIN)

          }, (error) => {
          reject(error);
          });

      }catch(error){
          reject(error);
      }
  });
}  

export const createPIN = async (FullName,PIN,LockerNumber) => {
  return new Promise(async (resolve, reject) => {

      const dbRef = ref(RTdb, `PIN/${FullName}/pincode`);
      
      try {
          const newPin = String(LockerNumber) + "-" + PIN
          set(dbRef, newPin)
          resolve("Pincode is created!")
      } catch (err) {
          reject("pin not created")
      }


  });
}

// **************** get history of all data **************** //
export const getHistory = async () => {
  return new Promise((resolve, reject) => {
    try {
      const dbRef = ref(RTdb, `History`);
      onValue(dbRef, (snapshot) => 
        {
          const data = snapshot.val();
          resolve(data) 
        }, (error) => 
        {
          reject(error);
        });

    }catch(error){
      reject(error);
    }
  });
}