import { collection,getDocs } from "firebase/firestore";
import { Fdb,statusLogin } from './FirebaseConfig'

const collectionRef = collection(Fdb, "users");

// verify if admin or user
export const isAdmin = (UID) => {
    return new Promise((resolve, reject) => {
      getDocs(collectionRef)
        .then((data) => {
          data.forEach((doc) => {
            if (doc.id === UID) {
            //   sessionStorage.setItem('isAdmin', doc.data().isAdmin ? "true" : "false");
              resolve(doc.data().isAdmin);
            }
          });
          reject(new Error("User not found.")); // Reject if user is not found in the data
        })
        .catch((error) => {
          reject(error); // Reject any errors that occur during the retrieval of data
        });
    });
  };
  