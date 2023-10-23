import React from 'react'
import { Appbar,UserApbbar } from '../Components/Appbar'
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

  const [login,setLogin] = React.useState()

  const isAdmins = sessionStorage.getItem('isAdmin');


  React.useEffect(()=>{

    statusLogin()
      .then(user=>{ 

        setLogin(isLoggedIn)
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

      {login || isLoggedIn? <Mainpage isAdminS={isAdmins} />:<Login/>}
      {/* <WelcomePage/> */}
      {/* <Login/> */}
    </div>

  )
}


// import LoginPage from '../pages/Login'
const LoginPage = React.lazy(()=> import('../pages/Login'))
const Signup = React.lazy(()=> import('../pages/signup/Otp_SignIn'))
const ForgotPassword = React.lazy(()=> import('../pages/ForgotPassword'))
const Login = () => {
    return (
      <React.Suspense fallback={<Loading/>}>
        <div>      
          <Routes>

            <Route path="/Login" element={<LoginPage/>}/>
            <Route path="/otp" element={<Signup/>}/>
            <Route path="/ForgotPassword" element={<ForgotPassword/>}/>
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
const MyLocker = React.lazy(()=> import('../pages/admin/MyLocker'))
const ProfileSettings = React.lazy(()=> import('../pages/admin/ProfileSettings'))
const ManageLockerAccess = React.lazy(()=> import('../pages/admin/ManageLockerAccess'))
// const SettingsConfig = React.lazy(()=> import('../pages/admin/SetingsAndConfig'))
const Admin = () =>{
  return (
    <div>      
      <React.Suspense fallback={<Loading/>}>
        <Routes>
          <Route element={<Header/>}>

            {/* Dashboard */}
            <Route path="/Admin/" element={<Dashboard/>}/> 

             {/* My Locker  */}
            <Route path="/Admin/MyLocker" element={<MyLocker/>}/>

            {/* Manage Locker Access*/}
            <Route path="/Admin/ManageLockerAccess" element={<ManageLockerAccess/>}/>

            {/* Profile Settings */}
            <Route path="/Admin/ProfileSettings" element={<ProfileSettings/>}/>

            {/* Settings */}
            {/* <Route path="/Admin/Settings" element={<SettingsConfig/>}/> */}

            <Route path="*" element={<Navigate to="/Admin/"/>}/>

          </Route>
        </Routes> 
      </React.Suspense>
</div>
  )
}

// User Page
const HomepageUser = React.lazy(()=> import('../pages/user/MyLocker_user'))
const User = ()=>{

  const HeaderUser = () => {
    return(
      <>
        <UserApbbar/>
        <Outlet />
      </>
    )
  }

  return(
  <div>
      <React.Suspense fallback={<Loading/>}>
        <Routes>
          <Route element={<HeaderUser/>}>

            <Route path="/User/" element={<HomepageUser/>}/>
            <Route path="*" element={<Navigate to="/User/"/>}/>

          </Route>
        </Routes> 
      </React.Suspense>
  </div>
  )
}
export default Routess