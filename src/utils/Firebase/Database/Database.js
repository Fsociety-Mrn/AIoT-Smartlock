import { RTdb } from '../Configuration'
import { 
    ref,
    set,
    remove
    // onValue, 
    // update 
} from "firebase/database";

  // generate a token
    export const openLocker = async (props) => {
        try {
            const keyRef = ref(RTdb, `LOCK/${props.FullName}/Locker Status`);

            set(keyRef,props.value);
     
        } catch (err) {
            console.error(err);
        }
    }

  //  History 
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
    

    // generate a token
    export const pushToken = async (props) => {
        try {
            set(ref(RTdb, 'GenerateToken_FacialUpdate/' + props.FullName),String(props.Code));
        } catch (err) {
            console.error(err);
        }
    }

    // remove token Key
    export const removeToken = (FullName) => {
        const keyRef = ref(RTdb, `GenerateToken_FacialUpdate/${FullName}`);
  
        remove(keyRef)
            .then(() => {
                console.log(`Key "${FullName}" removed successfully.`);
            })
            .catch((error) => {
                console.error(`Error removing key "${FullName}":`, error);
            });
    };