import { RTdb } from '../Configuration'
import { 
    ref,
    set,
    remove,
    onValue
    // update 
} from "firebase/database";

// **************** Open the Locker **************** //
    export const openLocker = async (props) => {
        try {
            const keyRef = ref(RTdb, `LOCK/${props.FullName}/Locker Status`);

            set(keyRef,props.value);
     
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
    
            set(keyRef,String("IoT Access"));
    
            console.log("Okay goods")
        } catch (err) {
            console.error(err);
        }
    }
    
// **************** generate a token **************** //
    export const pushToken = async (props) => {
        try {
            set(ref(RTdb, 'GenerateToken_FacialUpdate/' + props.FullName),String(props.Code));
        } catch (err) {
            console.error(err);
        }
    }

// **************** remove token Key **************** //
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



// **************** PIN setup **************** //
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

    export const createPIN = async (FullName,PIN) => {

        const dbRef = ref(RTdb, `PIN/${FullName}/pincode`);
        return new Promise(async (resolve, reject) => {
            const LockerNumber = await getLocker(FullName)

            try {
                const newPin = String(LockerNumber) + "-"+PIN
                set(dbRef, newPin)
                resolve("Pincode is created!")
            } catch (err) {
                reject("pin not created")
            }

 
        });
      }


