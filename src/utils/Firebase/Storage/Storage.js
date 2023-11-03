import { 
    getDownloadURL, 
    ref, 
    uploadBytes
  } from "firebase/storage";

 import { storage } from "../Configuration";


// Upload image
export async function imageUpload(file,UID){

    const imag = ref(storage,`userProfile/${UID}`)
    return await uploadBytes(imag,file)
    .then(()=> 
    {
       return getDownloadURL(imag);   
    })
  
  }