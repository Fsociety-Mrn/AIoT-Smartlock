import { RTdb } from '../Configuration'
import { 
    ref,
    set,
    remove,
    onValue
} from "firebase/database";

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

    export const getLocker = async (FullName) => {

        const keyRef = ref(RTdb, `LOCK/${FullName}/Locker Number`);

        return new Promise((resolve, reject) => {
            onValue(keyRef, (snapshot) => {

                const data = snapshot.val();
                resolve(data)

             }, (error) => {
                reject(error);
            });
        });
     
    }

// **************** History **************** //
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
    
            console.log("Okay goods")
        } catch (err) {
            console.error(err);
        }
    }

    export const getHistory = async (FullName) => {
        return new Promise((resolve, reject) => {
            try {
                const keyRef = ref(RTdb, `History/${FullName}`);
                onValue(keyRef, (snapshot) => {

                    const data = snapshot.val();
                    resolve(data)

                }, (error) => {
                    reject(error);
                });
            } catch (err) {
                console.error(err);
                reject(null)
            }

        })
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

    export const createPIN = async (FullName,PIN) => {

   
        return new Promise(async (resolve, reject) => {

            const dbRef = ref(RTdb, `PIN/${FullName}/pincode`);
            
            const LockerNumber = await getLocker(FullName)

            try {
                const newPin = String(LockerNumber) + "-" + PIN
                set(dbRef, newPin)
                resolve("Pincode is created!")
            } catch (err) {
                reject("pin not created")
            }

 
        });
    }

// **************** TOKEN VERIFY **************** //

    // verify token users
export const verifyToken = (TOKENs) => {
    return new Promise((resolve, reject) => {
      const dbRef = ref(RTdb, 'Token_User');
  
      onValue(dbRef, (snapshot) => {
        const data = snapshot.val();
  
        if (data) {
          let isValid = false;
  
          Object.entries(data).forEach(([key, value]) => {
            try {
              if (value === TOKENs) {
                console.log(`Data with key ${key} is valid.`);
                removeKey(key)
                    .then(result=> console.log(result))
                    .catch(error=>{
                        console.log(error);
                   
                    });
                isValid = true
               
              } else {
                console.log(`Invalid key`);
                isValid = false;
              }
            } catch (error) {
              console.error(`Error removing key "${key}":`, error);
              reject(false);
            }
          });
  
          resolve(isValid); // Resolve the Promise with the validity status
        } else {
          console.log('No data found');
          reject(false); // Resolve the Promise with false if no data is found
        }
      }, {
        onlyOnce: true // Optional: Ma-trigger lamang ng isang beses
      });
    });
};

  // remove token Key
export const removeKey = (key) => {
    return new Promise((resolve, reject) => {
        const keyRef = ref(RTdb, `Token_User/${key}`);
  
        remove(keyRef)
          .then(() => {
            console.log(`Key "${key}" removed successfully.`);
            resolve("eba sakay sa kalesa")
          })
          .catch((error) => {
            console.error(`Error removing key "${key}":`, error);
            reject(error)
          });
    })

    };
    

// **************** UPDATE NAME **************** //
export const getData = async (Key, FullName) => {
    return new Promise((resolve, reject) => {
        try {
            const keyRef = ref(RTdb, `${Key}/${FullName}`);
            onValue(keyRef, (snapshot) => {

                const data = snapshot.val();
                resolve(data)

            }, (error) => {
                reject(error);
            });
        } catch (err) {
            console.error(err);
            reject(null)
        }

    })
    }

export const updateData = async (Key, OldName, FullName) => {
   
    return new Promise(async (resolve, reject) => {

        try {
       
            const data = await getData(Key, OldName)
            const dbRef = ref(RTdb, `${Key}/${FullName}`);
    
            set(dbRef, data)

            remove(ref(RTdb, `${Key}/${OldName}`)).then(()=>{
                resolve("Updated!")
            })
     

        } catch (err) {
            reject("pin not created")
        }


    });
    }

