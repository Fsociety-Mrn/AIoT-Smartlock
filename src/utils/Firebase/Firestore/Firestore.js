import { collection, doc, getDoc, getDocs } from "firebase/firestore";
import { Fdb } from '../Configuration'
import { LogoutSession } from "../Authentication/Authentication";


const collectionRef = collection(Fdb, "users");

// verify if admin or user
export const isAdmin = (UID) => {
    return new Promise((resolve, reject) => {
      getDocs(collectionRef)
        .then((data) => {
          data.forEach((doc) => {
            if (doc.id === UID) {
            //   sessionStorage.setItem('isAdmin', doc.data().isAdmin ? "true" : "false");

    

                if(doc.data().isAdmin){
                    LogoutSession()
                    window.location.reload()
                }

              resolve(doc.data());
            }
          });
          reject(new Error("User not found.")); // Reject if user is not found in the data
        })
        .catch((error) => {
          reject(error); // Reject any errors that occur during the retrieval of data
        });
    });
};


// ********** PROFILE SETTINGS ********** //

// get userDetails
export const getUserDetails = async (UID) =>{
  try {
    const docRef = doc(Fdb, "users", UID); // Assuming Fdb is properly defined elsewhere

    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      const data = docSnap.data();

      const fullName = data.user.split(",")

      const details = {
        profilePicture: data.photoUrl,
        firstName: fullName[1],
        lastName: fullName[0]
      }

      return details; // You can return the data or do whatever you want with it
    } else {
      console.log("User document does not exist!");
      return null; // Or handle the non-existence case accordingly
    }
  } catch (error) {
    console.error("Error fetching user data:", error);
    throw error; // Rethrow the error or handle it gracefully
  }
}