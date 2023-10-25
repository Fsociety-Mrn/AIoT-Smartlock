import React from 'react'
import { Navigate, Route, Routes } from 'react-router'


const LoginPage = React.lazy(()=> import('../../Components/Forms/LoginForm'))
const Signup = React.lazy(()=> import('../../Components/Forms/RegisterForm'))
const Loading = React.lazy(()=> import('../../Components/Forms/Loading'))

const Login = () => {
  return (
    <React.Suspense fallback={<Loading/>}>
        <div>      
          <Routes>

            <Route path="/Login" element={<LoginPage/>}/>
            <Route path="/Signup" element={<Signup/>}/>

            <Route path="*" element={<Navigate to="/Login"/>}/>

          </Routes> 

        </div>
      </React.Suspense>
  )
}

export default Login