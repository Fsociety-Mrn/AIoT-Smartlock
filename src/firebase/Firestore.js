import { collection,getDocs, doc, setDoc, getDoc,updateDoc, deleteDoc  } from "firebase/firestore";
import { Fdb } from './FirebaseConfig'
import { 
  getDownloadURL, 
  getStorage, 
  ref, 
  uploadBytes
} from "firebase/storage";


const storage = getStorage();
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
      // .filter((document) => !document.data().isAdmin) // Filter out isAdmin = true
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
    isActive: true,
    isAdmin: false,
    photoUrl: "",
    user: "first name, last name"
  })
  .then(test=>{
    console.log(test);
    window.location.reload();
  })
  .catch(err=>console.log(err));
  

}

// get user name
export const getUserName = async (UID) =>{
  try {
    const docRef = doc(Fdb, "users", UID); // Assuming Fdb is properly defined elsewhere

    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      const data = docSnap.data();

      console.log(data.user);

      return data.user; // You can return the data or do whatever you want with it
    } else {
      console.log("User document does not exist!");
      return null; // Or handle the non-existence case accordingly
    }
  } catch (error) {
    console.error("Error fetching user data:", error);
    throw error; // Rethrow the error or handle it gracefully
  }
}

// update a username
export const updateName = async (UID,Name) =>{

 
    await updateDoc(doc(Fdb, "users", UID), {
      user: Name
    })
    .then(test=>{
      console.log(test);
      window.location.reload();
    })
    .catch(err=>console.log(err));
}

// Upload image
export async function imageUpload(file,UID){

  const imag = ref(storage,`userProfile/${UID}`)
  return await uploadBytes(imag,file)
  .then(()=> 
  {
     return getDownloadURL(imag);   
  })

}

// url
export const url = async (file) => {
  const imag = ref(storage,`userProfile/${file.name }`)
  await getDownloadURL(imag).then(e=>{return e})
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

// get userDetails
export const getUserDetails = async (UID) =>{
  try {
    const docRef = doc(Fdb, "users", UID); // Assuming Fdb is properly defined elsewhere

    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      const data = docSnap.data();

      return data; // You can return the data or do whatever you want with it
    } else {
      console.log("User document does not exist!");
      return null; // Or handle the non-existence case accordingly
    }
  } catch (error) {
    console.error("Error fetching user data:", error);
    throw error; // Rethrow the error or handle it gracefully
  }
}

// update Locker Number
export const updateLocker = async (UID=null, LockerNumber=null) =>{

  await updateDoc(doc(Fdb, "users", UID), {
    LockerNumber: LockerNumber
  })
    .then(test=>{
      alert("Your locker has been updated! Please set a new PIN code.");
      window.location.reload();
    })
    .catch(err=>console.log(err));


}

// update a username
export const promoteAdmin = async (UID,Name) =>{

  await updateDoc(doc(Fdb, "users", UID), {
    isAdmin: true
  })
  .then(test=>{
    alert(`${Name} is promoted as a Admin`);
    window.location.reload();
  })
  .catch(err=>console.log(err));
}


// update a username
export const setUserStatus = async (UID,status) =>{

  await updateDoc(doc(Fdb, "users", UID), {
    isActive: status
  })
  .then(()=>{
    window.location.reload();
  })
  .catch(err=>console.log(err));
}

// delete User
export const deleteUser =  (UID) =>{

  return new Promise(async (resolve, reject) => {
    try{

      const userDoc = doc(Fdb, "users", UID);
      await deleteDoc(userDoc);  
      alert("Successful remove")
      resolve("Successful remove")
  
    }catch(e){
      alert("Error removing")
      reject("Error removing")
    }
  })

}