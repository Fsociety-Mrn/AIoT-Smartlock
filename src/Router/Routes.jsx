import React from 'react'
import { Appbar } from '../Components/Appbar'

import { 
    Navigate, 
    Route, 
    Routes,
    Outlet
  } from 'react-router-dom'

import { statusLogin } from '../firebase/FirebaseConfig'






const Routess = () => {

  let LoginStatus = sessionStorage.getItem('TOKEN')

  React.useEffect( ()=>{
    statusLogin()
  },[])

  return (
    // <React.Suspense fallback={<div>Loading...</div>}>
    <div>
      { LoginStatus ? (<Admin/>) : (<Login/>) }
    </div>
    // </React.Suspense>
  )
}


// import LoginPage from '../pages/Login'
const LoginPage = React.lazy(()=> import('../pages/Login'))
const Login = () => {
    return (
      <React.Suspense fallback={<div>Loading...</div>}>
        <div>      



        <Routes>

            <Route path="/Login" element={<LoginPage/>}/>
            <Route path="*" element={<Navigate to="/Login"/>}/>

        </Routes> 

        </div>
      </React.Suspense>
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

  // import Homepage from '../pages/admin/Homepage'
const Homepage = React.lazy(()=> import('../pages/admin/Homepage'))
const MyAccount = React.lazy(()=> import('../pages/admin/Account'))
const CheckLocker  = React.lazy(()=> import('../pages/admin/LockerAvailable'))
const ManageLocker = React.lazy(()=> import('../pages/admin/ManageLocker'))
const Admin = () =>{

  return (
    <div>      
      <React.Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route element={<Header/>}>

            <Route path="/Admin/" element={<Homepage/>}/>
            <Route path="/Admin/MyAccount" element={<MyAccount/>}/>
            <Route path="/Admin/LockerAvailable" element={<CheckLocker/>}/>
            <Route path="/Admin/ManageLocker" element={<ManageLocker/>}/>
            <Route path="*" element={<Navigate to="/Admin/"/>}/>

          </Route>
        </Routes> 
      </React.Suspense>
</div>
  )
}



export const routesRouter = [
  { path: '/', component: Homepage }
];


export default Routess