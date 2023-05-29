import React from 'react'
import { LogoutSession } from '../../Authentication/Authentication'

const Dashboard = () => {
    
  return (
    <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
    <br/>
    <br/>
    <br/>

    <br/>

    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <h1>Dashboard</h1>

    <button onClick={(e)=>{
      LogoutSession();
      window.location.reload();
      }}>Logout</button>
    
    </div>
  )
}

export default Dashboard