import React from 'react'
import LoginPage from '../pages/Login'
import Homepage from '../pages/admin/Homepage'
import { Appbar } from '../Components/Appbar'

import { 
    Navigate, 
    Route, 
    Routes,
    Outlet,
  } from 'react-router-dom'

  import { auth } from '../firebase/FirebaseConfig'

  import { getAuth,onAuthStateChanged } from "firebase/auth";

const Routess = () => {

  const [loginUser, setLoginUser] = React.useState(false)
  
  React.useEffect( ()=>{
     onAuthStateChanged(auth, (user) => {
      if (user) {
        // User is signed in, see docs for a list of available properties
        // https://firebase.google.com/docs/reference/js/firebase.User
        const uid = user.uid;
        console.log(user)
        setLoginUser(true)
        // ...
      } else {
        // User is signed out
        // ...
        setLoginUser(false)
      }
    });
  },[])

  return (
    <div>

      { loginUser ? <Admin/> : <Login/> }
      {/* <Admin/> */}
    </div>
  )
}

const Login = () => {
    return (
      <div>      
        <Routes>
    
            <Route path="/Login" element={<LoginPage/>}/>
            <Route path="*" element={<Navigate to="/Login"/>}/>
  
        </Routes> </div>
    )
  }


const Header = () => {
    return(
      <>
        <Appbar/>
        <Outlet />
      </>
    )
  }

const Admin = () =>{
  return (
    <div>      
      <Routes>
        <Route element={<Header/>}>
          <Route path="/Admin/" element={<Homepage/>}/>
          <Route path="*" element={<Navigate to="/Admin/"/>}/>
        </Route>
      </Routes> </div>
  )
}
export default Routess