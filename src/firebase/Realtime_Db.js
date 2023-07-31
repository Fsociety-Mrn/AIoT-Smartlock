import { RTdb } from "./FirebaseConfig"
import { 
    ref,  
    onValue, 
    remove,
    set
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
export const generateToken = async (uniqueID) => {
  try {
    const tokensList = await getListOFTokens(); // Assuming getListOFTokens() returns a list of tokens
    set(ref(RTdb, 'GenerateToken_User/' + tokensList),String(uniqueID));
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


// generate a token for Facial
export const generateToken_Facial = (Name, uniqueID) => {
  try {
    set(ref(RTdb, 'GenerateToken_FacialUpdate/' + Name),String(uniqueID))
    .then(res=>console.log(res))
    .catch(err=>console.log(err));
    
  } catch (err) {
    console.error(err);
  }
}
