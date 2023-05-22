import { 
    setPersistence, 
    signInWithEmailAndPassword, 
    browserSessionPersistence 
} from "firebase/auth";

import { auth } from '../firebase/FirebaseConfig'


export const LoginSession = async (user) => {

    const login = await setPersistence(auth, browserSessionPersistence)
        .then(async () =>{

            return await signInWithEmailAndPassword(auth, user.email, user.password)
                .then(
                    userdata=> {
                        console.log(userdata)
                    }
                )
                .catch(error=>{
                    console.log(error.code)
                    console.log(error.message)
                })

    })

}