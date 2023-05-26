
import { 
    setPersistence, 
    signInWithEmailAndPassword, 
    browserSessionPersistence,
    signOut,
} from "firebase/auth";

import { auth } from '../firebase/FirebaseConfig'


// Login 
export const LoginSession = (user) => {
    return new Promise((resolve, reject) => {

      setPersistence(auth, browserSessionPersistence)

        .then(() => {
          signInWithEmailAndPassword(auth, user.email, user.password)

            .then(() => {
                window.location.reload();
              resolve("Login Successful");
            })
            .catch((error) => {
              console.log(error);
              const errorMessage = error.message.match(/\((.*?)\)/)[1];
              const errorMessages = errorMessage.replace('auth/', '').replace(/-/g, ' ');

              reject(errorMessages);
            });
        })
        .catch((error) => {
          console.log(error);
          reject("An error occurred during login.");
        });
    });
  };


  // Logout
export const LogoutSession = async () => {
    await signOut(auth).then(()=>{
        console.log("Succesfull signout")
        sessionStorage.clear()

    }).catch((err)=>console.log(err))
  
}
  