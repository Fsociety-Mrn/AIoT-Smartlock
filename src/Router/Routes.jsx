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

  import { onAuthStateChanged } from "firebase/auth";

const Routess = () => {

  const [loginUser, setLoginUser] = React.useState(false)
  
  React.useEffect( ()=>{
     onAuthStateChanged(auth, (user) => {
      if (user) {
        setLoginUser(true)
      } else {
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