import { collection,getDocs } from "firebase/firestore";
import { Fdb } from './FirebaseConfig'

const collectionRef = collection(Fdb, "users");

// verify if admin or user
export const isAdmin = async (Useruid) =>{

    return await getDocs(collectionRef)

        .then(data=>{

            data.forEach(doc=>{

                if (doc.id === Useruid){
            
                    // sessionStorage.setItem('isAdmin',doc.data().isAdmin) 

                    return doc.data().isAdmin
                }
                
            }) 

        });

}