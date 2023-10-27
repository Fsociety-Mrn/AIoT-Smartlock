import Titles from "../../Titles/Titles";
import { Form, Button, Modal, Alert, Col } from "react-bootstrap"; // Import Alert from React Bootstrap

import React, { useState } from "react"; // Import React and useState
import './Dashboard.css'; // Make sure this is the correct path to your CSS file

// Firebase.Database
import { 
  openLocker, 
  pushHistory, 
  pushToken,
  removeToken 
} from "../../../utils/Firebase/Database/Database";

import Code from "../../../utils/Code"


const UserDashboard = (props) => {

  // State to manage the modal and alert
  const [showModal, setShowModal] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  // State to store the old PIN and new PIN
  const [oldPin, setOldPin] = useState("");
  const [newPin, setNewPin] = useState("");

  // State for the slider 
  const [sliderValue, setSliderValue] = useState(0);
  const [isUnlocking, setIsUnlocking] = useState(false);
  const [status, setStatus] = useState("");
  const [count, setCount] = useState(0);

  // State for the Update Faces
  const [Token,setToken] = useState()
  const [isDisable,setIsdisable] = useState(false)
  const [Timer,setTimer] = useState(30)
  const [tokenStatus, setTokenStatus] = useState("")

  React.useEffect(() => {

    const FullName = String(props.firstName + " " + props.lastName).toUpperCase()

    // *************** for Faces *************** //

    if(Timer < 0){
      setStatus("SLIDE TO OPEN THE LOCKERS")
      setSliderValue(0)
      setTimer(null)
      setIsUnlocking(false)

      openLocker({
        FullName: FullName,
        value: false
      })

      return
    }

    
    const intervalFaces = setInterval(() => {

        setTimer(Timer - 1);
     
        setTokenStatus(`Expires at ${Timer}`)
     

    }, 1000);

   
     

    // *************** for Locker *************** //
    if(count < 0){
      setStatus("SLIDE TO OPEN THE LOCKERS")
      setSliderValue(0)
      setCount(null)
      setIsUnlocking(false)

      openLocker({
        FullName: FullName,
        value: false
      })

      return
    }


    const intervalId = setInterval(() => {
      setCount(count - 1);
      setStatus(`${count} LEFT TO LOCK`)
    }, 1000);

    return () => {
      clearInterval(intervalId)
      clearInterval(intervalFaces)
    };

  }, [count,Timer, props.firstName, props.lastName]);

  // Function to handle opening the modal
  const handleShowModal = () => {
    setShowModal(true);
    setShowAlert(false); // Hide any previous alerts when opening the modal
  };

  // Function to handle closing the modal
  const handleCloseModal = () => {
    setShowModal(false);
    setShowAlert(false); // Hide any previous alerts when closing the modal
  };

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // Replace '1234' with the actual correct old PIN
    if (oldPin === "1234") {
      // Old PIN is correct
      // Add your logic for changing the PIN here
      // Once the PIN is changed, you can close the modal
      handleCloseModal();
    } else {
      // Old PIN is incorrect, show an alert
      setShowAlert(true);
    }
  };

  // Function for slider 
  const handleSliderChange = (event) => {
    const newValue = parseInt(event.target.value);

    const FullName = String(props.firstName + " " + props.lastName).toUpperCase()

    if (newValue >= 100){
      openLocker({
        FullName: FullName,
        value: true
      })

      pushHistory(FullName)
      setIsUnlocking(true)
      setCount(5)
      // setStatus(`5 LEFT TO LOCK`)
    }
    else{
      setSliderValue(newValue)
    }

  };

  // Function to generate Token Faces
  const handleToken = e => {

    e.preventDefault()
    const tokenCode = Code()
    const FullName = String(props.firstName + " " + props.lastName).toUpperCase()

    setToken(tokenCode)
    setIsdisable(true)
    pushToken({ FullName: FullName,Code: tokenCode })

  }

  return (
    <>
      <Titles
      title="Welcome to the Dashboard! 🎉"
      text="Explore insights, take control, and make informed decisions with ease."
      />

      <Form>
        <div className="d-flex flex-column justify-content-center align-items-center mt-4">

          {/* open locker */}
          <Col md={10} sm={12}>
            <div className="d-flex flex-column justify-content-center align-items-center my-2 px-4" >
              <h1>{status}</h1>

              <input 
              type="range" 
              className="pullee"
              min="0"
              max="100"
              value={sliderValue}
              onChange={handleSliderChange}
              disabled={isUnlocking}
              />

            </div>
          </Col>
      
          <p class="lead">Token</p>
            <p> Expire at 30 </p>

          <div className="text-danger ">
          This is your TOKEN
          </div>

 
          <Button
          variant="primary"
          className="my-2 px-4"
          type="submit"
          style={{ width: "70%" }}
          onClick={handleToken}
          >
            Update Faces
          </Button>

          {/* Add the "Change Pin" button with modal */}
          <Button
          variant="primary"
          className="my-2 px-4"
          type="button"
          style={{ width: "70%" }}
          onClick={handleShowModal} // Show modal on button click
          >
            Change Pin
          </Button>

   
        </div>
      </Form>

      {/* Modal for changing PIN */}
      <Modal show={showModal} onHide={handleCloseModal}>

        <Modal.Header closeButton>
          <Modal.Title>Change PIN</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="oldPin">
              <Form.Label>Old PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter old PIN"
                value={oldPin}
                onChange={(e) => setOldPin(e.target.value)}
              />
            </Form.Group>

            <Form.Group controlId="newPin">
              <Form.Label>New PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter new PIN"
                value={newPin}
                onChange={(e) => setNewPin(e.target.value)}
              />
            </Form.Group>

            {/* Add an alert for incorrect old PIN */}
            {showAlert && (
              <Alert variant="danger">
                Incorrect old PIN. Please try again.
              </Alert>
            )}

            <Button variant="primary" type="submit">
              Save Changes
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </>
  );
};


export default UserDashboard;
