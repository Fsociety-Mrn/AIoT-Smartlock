import { collection,getDocs } from "firebase/firestore";
import { Fdb,statusLogin } from './FirebaseConfig'

const collectionRef = collection(Fdb, "users");

// verify if admin or user
export const isAdmin = async () =>{

    return await getDocs(collectionRef)

        .then(data=>{

            data.forEach(async doc=>{
                const uid = doc.id

                const data = await statusLogin();
                if (uid === data) {
                    sessionStorage.setItem('TOKEN',"Login");  
                    sessionStorage.setItem('isAdmin', doc.data().isAdmin ? "true" : "false");
                    // console.log(doc.data().isAdmin)
                    return doc.data().isAdmin;
                }
        
                
            }) 

        });
  
}