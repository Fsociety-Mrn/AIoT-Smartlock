
import { 
    setPersistence, 
    signInWithEmailAndPassword, 
    browserSessionPersistence,
    signOut,
    createUserWithEmailAndPassword,
} from "firebase/auth";

import { auth } from '../firebase/FirebaseConfig'
import { createUserData } from '../firebase/Firestore'

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

  // create account
  export const createAccount = (email, password) => {
    return new Promise((resolve, reject) => {
      createUserWithEmailAndPassword(auth, email, password)
        .then((res) => {
          console.log(res.user.uid);
          createUserData(res.user.uid);
          resolve(res); // Resolve the promise with the response from createUserWithEmailAndPassword
        })
        .catch((error) => {
          console.log(error);

          console.log(error);
          const errorMessage = error.message.match(/\((.*?)\)/)[1];
          const errorMessages = errorMessage.replace('auth/', '').replace(/-/g, ' ');

          reject(errorMessages); // Reject the promise with the error from createUserWithEmailAndPassword
        });
    });
  };

