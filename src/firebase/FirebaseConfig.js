// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
import { EmailAuthProvider, getAuth, onAuthStateChanged, reauthenticateWithCredential, sendPasswordResetEmail, updatePassword } from "firebase/auth"
import { getFirestore } from "firebase/firestore";
import { getDatabase } from "firebase/database";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
  authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.REACT_APP_FIREBASE_DATABASE_URL,
  projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID,
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.REACT_APP_FIREBASE_APP_ID,
  measurementId: process.env.REACT_APP_FIREBASE_MEASUREMENT_ID
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);

// for firebase authentication
export const auth = getAuth(app);

// for firesstore database
export const Fdb  = getFirestore(app);

// for realtime database
export const RTdb = getDatabase(app);

// check the login status
export const statusLogin = () => {

  return new Promise((resolve, reject) => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        sessionStorage.setItem('TOKEN',"Login")   

                            // window.location.reload();
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

// re authenticate
export const reauthentication = (CurrentPass) => {
  return new Promise((resolve, reject) => {
    const credential = EmailAuthProvider.credential(auth.currentUser.email, CurrentPass);

    reauthenticateWithCredential(auth.currentUser, credential)
    .then(() => {
      resolve({
        Password: false,
        PasswordMessage: "User Authenticated",
      })
    })
    .catch((error) => {

      reject({
        Password: true,
        PasswordMessage: "Invalid password",
      })

    });

  })
}

