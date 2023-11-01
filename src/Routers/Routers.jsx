import React from 'react'
import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

// import LoginForm from '../Components/Forms/LoginForm';
// import RegisterForm from '../Components/Forms/RegisterForm';



import Login from './Pages/Login';
import Mainmenu from './Pages/Mainmenu';

import { statusLogin } from '../utils/Firebase/Authentication/Authentication';
// import { isAdmin } from '../utils/Firebase/Firestore/Firestore';


const Routers = () => {

  const [toggle, setToggle] = useState("");
  const [email, setEmail] = useState()
  const [UID, setUID] = useState()

  const changeToggle = (toggle) => {
    setToggle(toggle)
  };

  useEffect(() => {

    // Check the status login
    statusLogin()
      .then(user=>
        { 

   
          if (user !== null) 
            {
              setUID(user.uid)
              setEmail(user.email)

              changeToggle("panel")
            // verify user
            // isAdmin(user.uid).then(data=>
            //   {
            //     data.isAdmin ? changeToggle("login") : changeToggle("panel")
            //   })

          }else{
            setToggle("login") 
            setEmail("")
          }

      })

    }, [toggle]);

  return (
    <div>

        {toggle === "panel" && <Mainmenu email={email} UID={UID} />}
        {toggle === "login" && <Login />}
    </div>
  )
}

export default Routers