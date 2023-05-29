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

  const isLoggedIn = sessionStorage.getItem('TOKEN');

  const isAdmins = sessionStorage.getItem('isAdmin');

  const [admins,setAdmins] = React.useState({
    Name: "",
    profile: ""
  })


  React.useEffect(()=>{
    // statusLogin().then(user=>console.log(user.uid))
    statusLogin()
      .then(user=>{ 

        setAdmins({
          Name: user.displayName,
          profile: user.photoURL
        })


        // verify Admin
        isAdmin(user.uid)
          .then(data=>{
            sessionStorage.setItem('isAdmin', data ? "true" : "false");  
            
            // if (!isAdmins){
            //   window.location.reload()
            // }
    
          }).catch(error=> console.log(error))
        }).catch(error=> console.log(error))

    
  },[])
  return (
 
    <div>
    
      {isLoggedIn ? <Mainpage isAdminS={isAdmins} Users={admins.Name} photoUrl={admins.profile}/>:<Login/>}
      {/* <WelcomePage/> */}
      {/* <Login/> */}
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
const WelcomePage = React.lazy(()=> import('../pages/Welcome'))
const Mainpage = ({ isAdminS, Users, photoUrl }) =>{


  if (isAdminS === "true"){
    return <Admin/>
  }else if(isAdminS === "false"){
    return <User/>
  }else{
    return <WelcomePage User={Users} photoUrl={photoUrl}/>
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
      <React.Suspense fallback={<div>Loading...</div>}>
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