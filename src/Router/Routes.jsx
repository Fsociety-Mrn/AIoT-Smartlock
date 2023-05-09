import React from 'react'
import LoginPage from '../pages/Login'
import { 
    Navigate, 
    Route, 
    Routes 
  } from 'react-router-dom'

const Routess = () => {
  return (
    <div><Login/></div>
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

export default Routess