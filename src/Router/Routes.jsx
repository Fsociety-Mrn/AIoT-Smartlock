import React from 'react'
import { Appbar } from '../Components/Appbar'
import Loading from '../pages/Loading'
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

  const isLoggedIn = sessionStorage.getItem('TOKEN');

  const isAdmins = sessionStorage.getItem('isAdmin');


  React.useEffect(()=>{

    statusLogin()
      .then(user=>{ 
        // verify Admin
        isAdmin(user.uid)
          .then(data=>{
            console.log(data.isAdmin);
            sessionStorage.setItem('isAdmin', data.isAdmin ? "true" : "false");  
          }).catch(error=> console.log(error))
        }).catch(error=> console.log(error))
    },[])
  return (
 
    <div>

      {isLoggedIn ? <Mainpage isAdminS={isAdmins} />:<Login/>}
      {/* <WelcomePage/> */}
      {/* <Login/> */}
    </div>

  )
}


// import LoginPage from '../pages/Login'
const LoginPage = React.lazy(()=> import('../pages/Login'))
const Signup = React.lazy(()=> import('../pages/signup/Otp_SignIn'))
const Login = () => {
    return (
      <React.Suspense fallback={<Loading/>}>
        <div>      
          <Routes>

            <Route path="/Login" element={<LoginPage/>}/>
            <Route path="/otp" element={<Signup/>}/>
            <Route path="*" element={<Navigate to="/Login"/>}/>

          </Routes> 

        </div>
      </React.Suspense>
    )
  }



// for mainpage
const WelcomePage = React.lazy(()=> import('../pages/Welcome'))
const Mainpage = ({ isAdminS }) =>{

  if (isAdminS === "true"){
    console.log("admin")
    return <Admin/>
  }else if(isAdminS === "false"){
    console.log("user")
    return <User/>
  }else{
    return <WelcomePage />
  }
  

  // return (
  //   <div>
  //     {isAdminS === "true" ? <Admin/> : <User/>}
  //   </div>
  // )

}

const Header = () => {
    return(
      <>
        <Appbar/>
        <Outlet />
      </>
    )
  }

// Admin Page
const Dashboard = React.lazy(()=> import('../pages/admin/Dashboard'))
const Homepage = React.lazy(()=> import('../pages/admin/Homepage'))
const MyAccount = React.lazy(()=> import('../pages/admin/Account'))
const CheckLocker  = React.lazy(()=> import('../pages/admin/LockerAvailable'))
const ManageLocker = React.lazy(()=> import('../pages/admin/ManageLocker'))
const SettingsConfig = React.lazy(()=> import('../pages/admin/SetingsAndConfig'))
const Admin = () =>{


  return (
    <div>      
      <React.Suspense fallback={<Loading/>}>
        <Routes>
          <Route element={<Header/>}>

            {/* Dashboard */}
            <Route path="/Admin/" element={<Dashboard/>}/> 

             {/* My Locker  */}
            <Route path="/Admin/MyLocker" element={<Homepage/>}/>

            {/* Locker Available */}
            <Route path="/Admin/LockerAvailable" element={<CheckLocker/>}/>

            {/* Manage Locker */}
            <Route path="/Admin/ManageLocker" element={<ManageLocker/>}/>

            {/* Profile Settings */}
            <Route path="/Admin/ProfileSettings" element={<MyAccount/>}/>

            {/* Settings */}
            <Route path="/Admin/Settings" element={<SettingsConfig/>}/>

            <Route path="*" element={<Navigate to="/Admin/"/>}/>

          </Route>
        </Routes> 
      </React.Suspense>
</div>
  )
}

// User Page
const HomepageUser = React.lazy(()=> import('../pages/user/Homepage'))
const User = ()=>{

  return(
  <div>
      <React.Suspense fallback={<Loading/>}>
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