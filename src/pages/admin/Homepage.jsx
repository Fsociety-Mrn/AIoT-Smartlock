import React from 'react'
import { LogoutSession } from '../../Authentication/Authentication'
const homepage = () => {
  return (
    <div>
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
    <h1>My Locker</h1>
    <button onClick={(e)=>{
      LogoutSession();
      window.location.reload();
      }}>Logout</button>
    
    
    </div>
  )
}

export default homepage