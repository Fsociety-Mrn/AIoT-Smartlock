import { collection, doc, getDoc, getDocs, setDoc, updateDoc } from "firebase/firestore";
import { Fdb } from '../Configuration'


const collectionRef = collection(Fdb, "users");

// verify if admin or user
export const isAdmin = (UID) => {
    return new Promise((resolve, reject) => {
      getDocs(collectionRef)
        .then((data) => {
          data.forEach((doc) => {
            if (doc.id === UID) {
            //   sessionStorage.setItem('isAdmin', doc.data().isAdmin ? "true" : "false");

    

                // if(doc.data().isAdmin){
                //     LogoutSession()
                //     window.location.reload()
                // }

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

// create userData
export const createUserData = async (UID,lastname,firstname) =>{

  return new Promise(async (resolve, reject) => {

    // Add a new document in collection "cities"
    await setDoc(doc(Fdb, "users", UID), {
      isActive: true,
      isAdmin: false,
      photoUrl: "",
      user: lastname + "," + firstname 
    })
    .then(test=>{
      console.log(test);
      resolve("Good shit")
    })
    .catch(err=>reject(err));
  })

  

}

// update a details
export const updateDetails = async (UID=null, Name=null, File=null) =>{
  if (File) {
    await updateDoc(doc(Fdb, "users", UID), {
      photoUrl: File,
      user: Name
    })
    .then(test=>{
      console.log(test);
      window.location.reload();
    })
    .catch(err=>console.log(err));
  }else{
    await updateDoc(doc(Fdb, "users", UID), {
      user: Name
    })
    .then(test=>{
      console.log(test);
      window.location.reload();
    })
    .catch(err=>console.log(err));
  }

}

// update Name
export const updateName = async (UID=null, Name=null) =>{
  return new Promise(async (resolve, reject) => {
      await updateDoc(doc(Fdb, "users", UID), {
        user: Name
    })
    .then(test=>{
      console.log("gooodhshit")
      resolve(test);
    })
    .catch(err=>reject(err));
  })



}

// ********** GET LOCKER NUMBER ********** //

export const getLockerNumber = async (UID) =>{
  return new Promise(async (resolve, reject) => {
  try {
    const docRef = doc(Fdb, "users", UID); // Assuming Fdb is properly defined elsewhere

    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      const data = docSnap.data();

     

      resolve(data.LockerNumber); // You can return the data or do whatever you want with it
    } else {
      console.log("User document does not exist!");
      reject(null); // Or handle the non-existence case accordingly
    }
  } catch (error) {
    console.error("Error fetching user data:", error);
    reject(error); // Rethrow the error or handle it gracefully
  }

})
}
