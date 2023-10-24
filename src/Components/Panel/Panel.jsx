import { PureComponent } from "react";
import styles from "./Panel.module.css";
import UserDashboard from "./UserDashboard/UserDashboard";
import UserCard from "./UserCard/UserCard";
import UserInformation from "./UserInformation/UserInformation";
import UserChangePassword from "./UserChangePassword/UserChangePassword";
import {
  UserEdit,
  DirectboxNotif,
  ProfileCircle,
  Logout
} from "iconsax-react";
import { Row, Col, } from "react-bootstrap";

// Sample user data (replace this with your actual data)
const sampleUser = {
  id: 1,
  username: "sampleUser",
  email: "sample@example.com",
  birthday: "1990-01-01",
  password: "password123",
  isLogin: true,
  firstName: "John",
  lastName: "Doe"
};

class Panel extends PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      user: { ...this.initState(sampleUser) },
      toggle: "setting"
    };
    this.state = {
      user: { ...this.initState(sampleUser) },
      toggle: "dashboard"
    };

    this.sidebarLinks = [
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

    this.logOut = this.logOut.bind(this);
    this.changeToggle = this.changeToggle.bind(this);
    this.changeUserInformation = this.changeUserInformation.bind(this);
  }

  initState({
    id,
    username,
    email,
    birthday,
    password,
    isLogin,
    firstName,
    lastName
  }) {
    return {
      id,
      username,
      email,
      birthday,
      password,
      firstName,
      lastName,
      isLogin
    };
  }

  logOut() {
    this.changeUserInformation(["isLogin"], [false]);
  }

  changeToggle(toggle) {
    this.setState({ toggle });
  }

  changeUserInformation(keyInfos, valInfos) {
    let newInfo = {};

    keyInfos.forEach((keyInfo, idx) => (newInfo[keyInfo] = valInfos[idx]));

    this.setState((prev) => ({
      user: {
        ...prev.user,
        ...newInfo
      }
    }));
  }

  render() {
    return (
      <div
        className={`${styles["panel-wrapper"]} d-flex align-items-center justify-content-center`}
      >
        <div
          className={`${styles.container} d-flex justify-content-center align-items-center p-0`}
        >
          <Row
            className={`${styles["panel"]} flex-column flex-md-row justify-content-center align-items-center px-3`}
          >
            <Col
              xs={12}
              sm={8}
              md={4}
              className="d-flex flex-column justify-content-center p-0"
            >
              <UserCard
                username={this.state.user.username}
                userBirthday={this.state.user.birthday}
                userEmail={this.state.user.email}
                sidebarLinks={this.sidebarLinks}
                onChangeToggle={this.changeToggle}
              />
            </Col>

            <Col
              xs={12}
              sm={8}
              md={7}
              className={`${styles["panel-column"]} bg-white border mt-5 mt-md-0 ms-md-5 p-5`}
            >
              {this.state.toggle === "setting" && (
                <UserInformation
                  username={this.state.user.username}
                  firstName={this.state.user.firstName}
                  lastName={this.state.user.lastName}
                  email={this.state.user.email}
                  birthday={this.state.user.birthday}
                  onChangeInfo={this.changeUserInformation}
                />
              )}
              {this.state.toggle === "password" && (
                <UserChangePassword
                  password={this.state.user.password}
                  onChangeInfo={this.changeUserInformation}
                />
              )}
              {this.state.toggle === "dashboard" && (
                <UserDashboard
                  username={this.state.user.username}
                  firstName={this.state.user.firstName}
                  lastName={this.state.user.lastName}
                  email={this.state.user.email}
                  birthday={this.state.user.birthday}
                  onChangeInfo={this.changeUserInformation}
                />
              )}
            </Col>
          </Row>
        </div>
      </div>
    );
  }
}

export default Panel;
