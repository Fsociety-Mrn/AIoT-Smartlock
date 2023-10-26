import { 
    EmailAuthProvider, 
    onAuthStateChanged, 
    reauthenticateWithCredential, 
    sendPasswordResetEmail, 
    updatePassword,
    setPersistence, 
    signInWithEmailAndPassword, 
    browserLocalPersistence,
    signOut,
    // createUserWithEmailAndPassword,
} from "@firebase/auth";

// import { createUserData } from '../firebase/Firestore'

import { auth } from "../Configuration";

// check the login status
export const statusLogin = () => {

    return new Promise((resolve, reject) => {
      onAuthStateChanged(auth, (user) => {
        if (user) {
          sessionStorage.setItem('TOKEN',"login")   
          console.log(sessionStorage.getItem('TOKEN'))
          resolve(user);
        } else {
  
          sessionStorage.clear()
          resolve(null);
        }
      }, reject);
    });
};
  
// change password
export const changing_password = (CurrentPass = null, NewPassword = null) => {
  
    return new Promise((resolve, reject) => {
      const credential = EmailAuthProvider.credential(auth.currentUser.email, CurrentPass);
  
      reauthenticateWithCredential(auth.currentUser, credential)
        .then(() => {
          updatePassword(auth.currentUser, NewPassword)
            .then(() => {
              console.log("Password changed successfully");
              resolve({
                oldPassword: false,
                oldPasswordMessage: "Invalid password",
                newPassword: false,
                newPasswordMessage: ""
              });
            })
            .catch((error) => {
              console.error("Error updating password:");
              resolve({
                oldPassword: true,
                oldPasswordMessage: "",
                newPassword: true,
                newPasswordMessage: "An error occurred while updating the password."
                
              });
            });
        })
        .catch((error) => {
  
          resolve({
            oldPassword: true,
            oldPasswordMessage: "Invalid password",
            newPassword: true,
            newPasswordMessage: ""
          });
        });
    });
}
  
// forgot Password
export const ForgotPasswords = (email) => {
    return new Promise((resolve, reject) => {
      sendPasswordResetEmail(auth, email)
        .then(() => {
          // Password reset email sent successfully
          resolve({
            message: "Password reset email sent!",
            error: false
          });
        })
        .catch((error) => {
  
          // An error occurred
          reject({
            message:error
            .message    
            .replace("Firebase: Error", "")
            .replace("auth/","")
            .replace("(","")
            .replace(")","")
            .replace("-", " ")
            .replace("-", " "),
            error: true
          });
        });
    });
};
  
// Login 
export const LoginSession = (user) => {
    return new Promise((resolve, reject) => {

      setPersistence(auth, browserLocalPersistence)

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

//   // create account
//   export const createAccount = (email, password) => {
//     return new Promise((resolve, reject) => {
//       createUserWithEmailAndPassword(auth, email, password)
//         .then((res) => {
//           console.log(res.user.uid);
//           createUserData(res.user.uid);

  
//           resolve(res); // Resolve the promise with the response from createUserWithEmailAndPassword
//         })
//         .catch((error) => {
//           console.log(error);

//           console.log(error);
//           const errorMessage = error.message.match(/\((.*?)\)/)[1];
//           const errorMessages = errorMessage.replace('auth/', '').replace(/-/g, ' ');

//           reject(errorMessages); // Reject the promise with the error from createUserWithEmailAndPassword
//         });
//     });
//   };
