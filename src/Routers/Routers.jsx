import React from 'react'
import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Panel from "../Components/Panel/Panel";
// import LoginForm from '../Components/Forms/LoginForm';
import RegisterForm from '../Components/Forms/RegisterForm';



const Routers = () => {
    const [toggle, setToggle] = useState("");

    const changeToggle = (toggle) => setToggle(toggle);
  
    useEffect(() => {
      // Replace this logic with your own to determine the initial state of `toggle`
      // For testing purposes, we'll assume the user is logged in.
      const userIsLoggedIn = false;
  
      if (userIsLoggedIn) {
        changeToggle("panel");
      } else {
        changeToggle("login");
      }
    }, []);

  return (
    <div>
        {toggle === "panel" && <Panel />}
        {toggle === "login" && <RegisterForm />}
    </div>
  )
}

export default Routers