import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Panel from "./Components/Panel/Panel";

const App = () => {
  const [toggle, setToggle] = useState("");

  const changeToggle = (toggle) => setToggle(toggle);

  useEffect(() => {
    // Replace this logic with your own to determine the initial state of `toggle`
    // For testing purposes, we'll assume the user is logged in.
    const userIsLoggedIn = true;

    if (userIsLoggedIn) {
      changeToggle("panel");
    } else {
      changeToggle("register");
    }
  }, []);

  return <>{toggle === "panel" && <Panel />}</>;
};

export default App;
