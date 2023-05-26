import React from 'react'
import { Appbar } from '../Components/Appbar'

import { 
    Navigate, 
    Route, 
    Routes,
    Outlet
  } from 'react-router-dom'

import { statusLogin } from '../firebase/FirebaseConfig'
import { isAdmin } from '../firebase/Firestore'




// for Login
const Routess = () => {

  const [datas,setDatas] = React.useState()

  const isLoggedIn = sessionStorage.getItem('TOKEN');

  React.useEffect( ()=>{


    statusLogin()
    .then(
      data=> setDatas(isAdmin(data))
    )
                        sessionStorage.setItem('isAdmin',datas) 
  },[])


  return (
 
    <div>
      { isLoggedIn ? (<Mainpage/>) : (<Login/>) }
      {/* { isLoggedIn ? (<Admin />) : (<Login/>) } */}
    </div>

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

// for mainpage
const Mainpage = () =>{
  const isAdminS = sessionStorage.getItem('isAdmin');

  if (isAdminS) {
    return (<Admin/>)
  }
  
  return (<User/>)
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

// user info
const HomepageUser = React.lazy(()=> import('../pages/user/Homepage'))

const User = ()=>{
  return(
  <div>
      <React.Suspense fallback={<div>Loading...</div>}>
        <Routes>
          {/* <Route element={<Header/>}> */}

            <Route path="/User/" element={<HomepageUser/>}/>
            <Route path="*" element={<Navigate to="/User/"/>}/>

          {/* </Route> */}
        </Routes> 
      </React.Suspense>
  </div>
  )
}
export default Routess