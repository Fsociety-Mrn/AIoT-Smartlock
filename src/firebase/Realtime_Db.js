
import TokenGenerator from "../Components/TokenGenerator";
import { RTdb } from "./FirebaseConfig"
import { 
    ref,  
    onValue, 
    remove,
    set,
    push
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
export const generateToken = async (LockerNumber) => {
return new Promise((resolve, reject) => {
  try {
    const Token = TokenGenerator();

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

    const formattedDate = String(newDate.toLocaleString('en-US', dateOptions)).replace(",", "");
    const formattedTime = newDate.toLocaleString('en-US', timeOptions);

    const data = {
      LockerNumber: LockerNumber,
      OTP: Token,
      EXPIRATION: {
        date: formattedDate,
        time: formattedTime
      }
    }


    const tokensRef = ref(RTdb, 'GenerateToken_User');
    const newTokenRef = push(tokensRef); // This generates a unique key

    set(newTokenRef, data);

    console.log("🎉 One-Time Password (OTP) for signing up has been generated! 🚀");

    resolve(Token)

  } catch (err) {
    console.error(err);
    reject(err)
  }
})
}

export const TokenList = () => {
  const dbRef = ref(RTdb, 'GenerateToken_User');

  return new Promise((resolve, reject) => {
    onValue(dbRef, (snapshot) => {

      const data = snapshot.val();
      const currentTime = new Date();

      // Filter out expired tokens
      const validTokens = data && Object.values(data).filter(token => {
        const expirationDate = new Date(`${token.EXPIRATION.date} ${token.EXPIRATION.time}`);
        return expirationDate > currentTime;
      });

      // Remove expired tokens
      const expiredTokens = data && Object.entries(data).filter(([key, token]) => {
        const expirationDate = new Date(`${token.EXPIRATION.date} ${token.EXPIRATION.time}`);

        return expirationDate <= currentTime;
      });

      
      // Remove expired tokens from the database
      const removalPromises = expiredTokens && expiredTokens.map(([key]) => removeKey(key));

      // Wait for all removal operations to complete
      Promise.all(removalPromises)
        .then(() => {
          console.log('Expired tokens removed successfully.');
          resolve(validTokens);
        })
        .catch((error) => {
          console.error('Error removing expired tokens:', error);
          reject(error);
        });
    }, (error) => {
      reject(error);
    });
  });
}

// get token limit
export const get_token_limit = async () => {
  return new Promise((resolve, reject) => {
    try {
      const dbRef = ref(RTdb, 'token/limit');

      onValue(dbRef, (snapshot) => {
        const data = snapshot.val();
        resolve(data) 
      })
  
    } catch (err) {
      console.error(err);
      reject(err)
    }
  })
}

export const add_token_cap = async (data) =>{
  return new Promise((resolve, reject) => {
    try{

      const tokensRef = ref(RTdb, 'token/cap');
      const newTokenRef = push(tokensRef); // This generates a unique key

      set(newTokenRef, data);
      resolve("add to token cap")
    }catch(e){
      console.error(e)
      reject(e)
    }
  })
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

export const changeLockerNumber = async (KeyName,Name,LockerNumber) => {
  return new Promise(async (resolve, reject) => {
    try {
      const keyRef = ref(RTdb, `${KeyName}/${Name}/Locker Number`);
      
      set(keyRef,LockerNumber);
      resolve("locker Number Updated")
    } catch (err) {
      reject(err);
    }
  })
}

export const getLockerSensor = async (locker) => {
  return new Promise((resolve, reject) => {
    try {
      const dbRef = ref(RTdb, `Locker/${locker}`);
      onValue(dbRef, (snapshot) => 
        {
          const data = snapshot.val();
          console.log(data)
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

export const removePIN = async (FullName) => {

  return new Promise((resolve, reject) => { 
    
    const keyRef = ref(RTdb, `PIN/${FullName}`);

    remove(keyRef)
      .then(() => {
        console.log(`removed successfully.`);
        resolve('removed successfully.')
      })
      .catch((error) => {
        console.error(`Error removing:`, error);
        reject(`Error removing:`, error)
      });
  })

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

// push History
export const pushHistory = async (FullName) => {
  try {

      const now = new Date();

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

      const dateNow = String(now.toLocaleString('en-US', dateOptions)).replace(",", "");
      const timeNow = now.toLocaleString('en-US', timeOptions);


      const keyRef = ref(RTdb, `History/${FullName}/${dateNow}/${timeNow}`);

      set(keyRef,{
          "Access_type": String("IoT Access")
      });
  } catch (err) {
      console.error(err);
  }
}

// remove History of user
export const removeUser = async (KeyName,Name) =>{
  const keyRef = ref(RTdb, `${KeyName}/${Name}`);
  
  remove(keyRef)
    .then(() => {
      console.log(`removeUser(): removed successfully.`);
    })
    .catch((error) => {
      console.error(`removeUser(): Error removing:`, error);
    });
}

// **************** view suspended person **************** //
export const getSuspended = async () => {
  return new Promise((resolve, reject) => {
    try {
      const dbRef = ref(RTdb, `suspended`);
      onValue(dbRef, (snapshot) => 
        {
          const data = snapshot.val();

          if (!data) {
            resolve({});
          } else {
            // Transform the data into the desired format
            const revisedData = Object.keys(data).reduce((acc, key) => {
              acc[key] = {
                personID: key,
                status: data[key]
              };
              return acc;
            }, {});
            resolve(revisedData);

          }
        }, (error) => 
        {
          reject(error);
        });

    }catch(error){
      reject(error);
    }
  });
}

export const updateSuspended = async (personID) => {
  return new Promise((resolve, reject) => {
    try {
      const dbRef = ref(RTdb, `suspended/${personID}`);
      set(dbRef,false);
      resolve("okay")

    }catch(error){
      reject(error);
    }
  });
}
