import { RTdb } from "./FirebaseConfig"
import { 
    ref, 
    // get, 
    onValue, 
    remove 
    // update 
} from "firebase/database";


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
const removeKey = (key) => {
    const keyRef = ref(RTdb, `GenerateToken_User/${key}`);
  
    remove(keyRef)
      .then(() => {
        console.log(`Key "${key}" removed successfully.`);
      })
      .catch((error) => {
        console.error(`Error removing key "${key}":`, error);
      });
  };