import { collection,getDocs, doc, setDoc } from "firebase/firestore";
import { Fdb } from './FirebaseConfig'

const collectionRef = collection(Fdb, "users");

// verify if admin or user
export const isAdmin = (UID) => {
    return new Promise((resolve, reject) => {
      getDocs(collectionRef)
        .then((data) => {
          data.forEach((doc) => {
            if (doc.id === UID) {
            //   sessionStorage.setItem('isAdmin', doc.data().isAdmin ? "true" : "false");
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

// get users list
export const userData = async () => {
  return await getDocs(collectionRef)
    .then((querySnapshot) => {
      const userDataArray = querySnapshot.docs
      .filter((document) => !document.data().isAdmin) // Filter out isAdmin = true
      .map((document) => ({
        id: document.id,
        ...document.data(),
      }));
      // console.log(userDataArray) ;
      return userDataArray;
    })
    .catch((error) => {
      console.log(error);
      return []; // Return an empty array in case of an error
    });
};

// create collection
export const createUserData = async (UID) =>{
  // Add a new document in collection "cities"
  await setDoc(doc(Fdb, "users", UID), {
    isActive: "Los Angeles",
    isAdmin: "CA",
    photoUrl: "USA",
    user: "Lisboa, Artmillen C"
  });
}