import React from "react";
import styles from "./Panel.module.css";
import UserDashboard from "./UserDashboard/UserDashboard";
import UserCard from "./UserCard/UserCard";
import UserInformation from "./UserInformation/UserInformation";
import UserChangePassword from "./UserChangePassword/UserChangePassword";
import UserHistory from "./UserHistory"
import {
  UserEdit,
  DirectboxNotif,
  ProfileCircle,
  Logout
} from "iconsax-react";
import { Row, Col, } from "react-bootstrap";


import { LogoutSession } from "../../utils/Firebase/Authentication/Authentication"; 
import { getUserDetails } from "../../utils/Firebase/Firestore/Firestore"; 


const Panel = (props) => {
  
  const initState = ({
    id,
    username,
    email,
    birthday,
    password,
    isLogin,
    firstName,
    lastName
  }) => ({
    id,
    username,
    email,
    birthday,
    password,
    firstName,
    lastName,
    isLogin
  });

  const changeToggle = (toggle) => {

  
    
    if (toggle === "logout") {
      window.location.reload();
      LogoutSession();
    } else {

      setToggle(toggle);
    }
  };

  const changeUserInformation = (keyInfos, valInfos) => {
    const newInfo = {};



    keyInfos.forEach((keyInfo, idx) => (newInfo[keyInfo] = valInfos[idx]));

    setUser((prev) => ({
      ...prev,
      user: {
        ...prev.user,
        ...newInfo
      }
    }));
  };

  // ************* User Details ************* //
  const [user, setUser] = React.useState(initState({

    id: 1,
    username: "....",
    email: "....",
    birthday: "0-0-0",
    password: "....",
    isLogin: true,
    firstName: "....",
    lastName: "...."
  }));

  React.useState(()=>{


    getUserDetails(props.UID).then(data=>{
   

      setUser({
        id: 1,
        userProfile: data.profilePicture,
        username: data.firstName + " " + data.lastName,
        // username: data.username,
        email: props.email,
        birthday: "1990-01-01",
        password: "password123",
        isLogin: true,
        firstName: data.firstName,
        lastName: data.lastName
      })
    })

  },[])

  const [toggle, setToggle] = React.useState("dashboard");

  // ************* SIDEBAR MENU ************* //
  const sidebarLinks = [
    {
      id: 1,
      border: true,
      text: "Dashboard",
      icon: <DirectboxNotif size="20" color="black" />,
      active: true
    },
    {
      id: 2,
      border: true,
      text: "History",
      icon: <ProfileCircle size="20" color="black" />,
      active: false
    },
    {
      id: 3,
      border: true,
      text: "Setting",
      icon: <UserEdit size="20" color="black" />,
      active: false
    },
    {
      id: 4,
      border: false,
      text: "Logout",
      icon: <Logout size="20" color="black" />,
      active: false
    }
  ];

  return (
    <div className={`${styles["panel-wrapper"]} d-flex align-items-center justify-content-center`}>
      <div className={`${styles.container} d-flex justify-content-center align-items-center p-0`}>
        <Row className={`${styles["panel"]} flex-column flex-md-row justify-content-center align-items-center px-3`}>
          <Col xs={12} sm={8} md={4} className="d-flex flex-column justify-content-center p-0">
            <UserCard
              userProfile={user.userProfile}
              username={user.username}
              userBirthday={user.birthday}
              userEmail={user.email}
              sidebarLinks={sidebarLinks}
              onChangeToggle={changeToggle}
            />
          </Col>
          <Col xs={12} sm={8} md={7} className={`${styles["panel-column"]} bg-white border mt-5 mt-md-0 ms-md-5 p-5`}>
            {toggle === "setting" && (
              <UserInformation
                username={user.username}
                firstName={user.firstName}
                lastName={user.lastName}
                email={user.email}
                birthday={user.birthday}
                onChangeInfo={changeUserInformation}
              />
            )}
            {toggle === "password" && (
              <UserChangePassword
                password={user.password}
                onChangeInfo={changeUserInformation}
              />
            )}
            {toggle === "history" && (
              <UserHistory
                username={user.username}
                firstName={user.firstName}
                lastName={user.lastName}
                email={user.email}
                birthday={user.birthday}
                onChangeInfo={changeUserInformation}
              />
            )}
            {toggle === "dashboard" && (
              <UserDashboard
                username={user.username}
                firstName={user.firstName}
                lastName={user.lastName}
                email={user.email}
                birthday={user.birthday}
                onChangeInfo={changeUserInformation}
              />
            )}
          </Col>
        </Row>
      </div>
    </div>
  );
};

export default Panel;
