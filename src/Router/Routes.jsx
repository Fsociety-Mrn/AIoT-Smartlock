import React from 'react'
import { Appbar } from '../Components/Appbar'
import Loading from '../pages/Loading'
import { 
    Navigate, 
    Route, 
    Routes
  } from 'react-router-dom'

import { statusLogin } from '../firebase/FirebaseConfig'
import { isAdmin } from '../firebase/Firestore'
import { LogoutSession } from '../Authentication/Authentication'

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

            if (data.isAdmin)
            {

          
              sessionStorage.setItem('isAdmin', "true");  
            }else{
              LogoutSession()
            }

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
  }else{
    return <WelcomePage />
  }
  
}



// Admin Page
const Admin = () =>{
  return (
    <div>      
      <React.Suspense fallback={<Loading/>}>
        <Routes>


            {/* Dashboard */}
            <Route path="/Admin" element={<Appbar/>}/> 
            <Route path="*" element={<Navigate to="/Admin"/>}/>

       
        </Routes> 
      </React.Suspense>
</div>
  )
}


export default Routess