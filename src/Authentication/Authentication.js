
import { 
    setPersistence, 
    signInWithEmailAndPassword, 
    browserSessionPersistence 
} from "firebase/auth";

import { auth } from '../firebase/FirebaseConfig'


// Login 
export const LoginSession = async (user) => {

    await setPersistence(auth, browserSessionPersistence)
        .then(async () =>{

            return await signInWithEmailAndPassword(auth, user.email, user.password)
                .then(
                    ()=> {
                        return String("Login Successful")
                    }
                )
                .catch(error=>{
                    console.log(error)
                    const errorMessage = error.message.match(/\((.*?)\)/)[1];
                    const errorMessages = errorMessage.replace('auth/', '').replace(/-/g, ' ');
                    console.log(errorMessages)
                    return errorMessages
                })
    })

}