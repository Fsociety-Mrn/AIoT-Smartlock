import Titles from "../../Titles/Titles";
import { Form, Button, Modal, Alert, Col, Container, Stack, Row } from "react-bootstrap"; // Import Alert from React Bootstrap

import React, { useState } from "react"; // Import React and useState
import './Dashboard.css'; // Make sure this is the correct path to your CSS file

// Firebase.Database
import { 
  openLocker, 
  pushHistory, 
  pushToken,
  removeToken,
  checkPin,
  createPIN,
  verifyPIN
} from "../../../utils/Firebase/Database/Database";

// Firebase.Firestore
import { getLockerNumber } from "../../../utils/Firebase/Firestore/Firestore"; 


// validation
import { pinSchema,NewpinSchema } from "../../../utils/Validation/Validation"

import Code from "../../../utils/Code"



const UserDashboard = (props) => {

  // State to manage the modal and alert
  const [showModal, setShowModal] = useState(false);
  const [showModalCreate, setShowModalCreate] = useState(false);
  const [showAlert, setShowAlert] = useState(false);

  // State to store the old PIN and new PIN
  const [oldPin, setOldPin] = useState("");
  const [newPin, setNewPin] = useState("");
  const [createPin,setCreatePIN] = useState({
    newPin: "",
    confirmPin: ""
  })
  const [error,setError] = useState({
    pin1: false,
    pin1Error: "",

    pin2: false,
    pin2Error: ""
  })
  const [checkPIN, setCheckPIN] = useState(false);

  // State for the slider 
  const [sliderValue, setSliderValue] = useState(0);
  const [isUnlocking, setIsUnlocking] = useState(false);
  const [status, setStatus] = useState("");
  const [count, setCount] = useState(0);

  const [lockerNumber, setLockerNumber] = useState()

  // State for the Update Faces
  const [Token,setToken] = useState()
  const [isDisable,setIsdisable] = useState(false)
  const [Timer,setTimer] = useState()
  const [tokenStatus, setTokenStatus] = useState("")

  const OpenLocker = async (FullName) => {
    const data = await getLockerNumber(props.UID)

    setLockerNumber(data)

    openLocker({
      FullName: FullName,
      value: false,
      number: data
    })

  }

  React.useEffect(() => {


    const FullName = String(props.firstName + " " + props.lastName).toUpperCase()



  

    // *************** for Change PIN *************** // 
      checkPin(FullName).then(result=>setCheckPIN(result))
 
    // *************** for Faces *************** //

    if(Timer < 0){

      setTimer(null)
      setIsdisable(false)
      removeToken(FullName)

      return
    }

    // *************** for Locker *************** //
    if(count < 0){
      setStatus("SLIDE TO OPEN your Locker")
      setSliderValue(0)
      setCount(null)
      setIsUnlocking(false)

      OpenLocker(FullName)
      // openLocker({
      //   FullName: FullName,
      //   value: false
      // })

      return
    }


    const intervalId = setInterval(() => {

     
        setCount(count - 1);
        setStatus(`${count} LEFT TO LOCK`)  
      
      if (Timer !== null)
      {
        setTimer(Timer - 1);
        setTokenStatus(`Expires in ${Timer}`)
      }

    }, 1000);

    return () => {

      clearInterval(intervalId);
      // removeToken(FullName);

    };

  }, [count, Timer, props.firstName, props.lastName, props.UID]);

  // Function to handle opening the modal
  const handleShowModal = () => {
    setShowModal(true);
    setShowAlert(false); // Hide any previous alerts when opening the modal
  };

  const handleShowModalCreate = () => {
    setShowModalCreate(true);
    setShowAlert(false); // Hide any previous alerts when opening the modal
  };

  // Function to handle closing the modal
  const handleCloseModal = () => {
    setShowModal(false);
    setShowAlert(false); // Hide any previous alerts when closing the modal
  };

  const handleCloseModalCreate = () => {
    setShowModalCreate(false);
    setShowAlert(false); // Hide any previous alerts when closing the modal
  };

  // Function to handle form submission for 
  const handleSubmitCreate = async (event) => {
    event.preventDefault();
    try {

      await pinSchema.validate({ PIN: createPin.newPin, PIN2: createPin.confirmPin }, { abortEarly: false });
      const FullName = String(props.firstName + " " + props.lastName).toUpperCase()
      
      createPIN(FullName,createPin.confirmPin).then(e=>{
        setError({
          pin1: false,
          pin1Error: "",
      
          pin2: false,
          pin2Error: ""
        })

        handleCloseModalCreate()

      })
    } catch (validationError) {

      // Extract specific error messages for email and password
      const emailError = validationError.inner.find((error) => error.path === 'PIN');
      const passwordError = validationError.inner.find((error) => error.path === 'PIN2');

    // If validation errors occur
      setError({
        pin1: !!emailError,
        pin1Error: emailError && emailError.message,

        pin2: !!passwordError,
        pin2Error: passwordError && passwordError.message
      });

    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {

      await NewpinSchema.validate({ PIN: oldPin, PIN2: newPin}, { abortEarly: false });
      const FullName = String(props.firstName + " " + props.lastName).toUpperCase()
      verifyPIN(FullName, oldPin).then(result=>{

        // if pincode is verified
        result && createPIN(FullName,newPin).then(result=> {     
          setError({
            pin1: false,
            pin1Error: "",
      
            pin2: false,
            pin2Error: ""
          })

          setNewPin("")
          setOldPin("")
          handleCloseModal()
        })

        // if pincode is verified
        !result && setError({ pin1: false, pin1Error: "", pin2: true, pin2Error: "old pin is not verified" })
      })


    } catch (validationError) {

      // Extract specific error messages for email and password
      const emailError = validationError.inner.find((error) => error.path === 'PIN');
      const passwordError = validationError.inner.find((error) => error.path === 'PIN2');

    // If validation errors occur
      setError({
        pin1: !!emailError,
        pin1Error: emailError && emailError.message,

        pin2: !!passwordError,
        pin2Error: passwordError && passwordError.message
      });

    }
  };

  // Function for slider 
  const handleSliderChange = (event) => {
    const newValue = parseInt(event.target.value);

    const FullName = String(props.firstName + " " + props.lastName).toUpperCase()



    if (newValue >= 100){

      openLocker({
        FullName: FullName,
        value: true,
        number: lockerNumber
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
    setTimer(30)

    pushToken({ FullName: FullName,Code: tokenCode })

  }

  return (
    <>
      <Titles
      title="Welcome to the Dashboard! 🎉"
      text="Explore insights, take control, and make informed decisions with ease."
       
      className="text-center text-nowrap"
      />

      <Container>
        <Row className="d-flex flex-column justify-content-center align-items-center mt-4">

          {/* open locker */}
          <Col md={10} sm={12}>
            <div className="d-flex flex-column justify-content-center align-items-center my-2 px-4" >
              <h1 className="text-nowrap">{status}</h1>

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

          {/* Token and Update Faces */}
          <Col md={10} sm={12} className="mt-3">

            <Stack gap={2} className="col-md-12 mx-auto">
         

              {/* Token Code */}
              {isDisable && 
                <div className="text-danger text-center">

                Generate Face Update OTP Code: <strong>{Token}</strong> 
                <p>({tokenStatus})</p>
                </div>
              }

              <Button
              variant="primary"
              className="p-2"
              onClick={handleToken}
              style={{
                background: 'rgb(61, 152, 154)',
                color: 'white' // Set the text color
              }}
              >
                generate face update OTP
              </Button>

              {/* Add the "Change Pin" button with modal */}
              {!checkPIN &&<Button
              variant="primary"
              className="p-2 mt-1"
              type="button"
              style={{
                background: 'rgb(61, 152, 154)',
                color: 'white' // Set the text color
              }}
              onClick={handleShowModal} // Show modal on button click
              >
                 change locker pin
              </Button>}


              {checkPIN && <div className="text-danger text-center mt-2">
                Please create locker PIN
              </div>}

              {checkPIN && <Button
              variant="primary"
              className="p-2"
              type="button"
              style={{
                background: 'rgb(61, 152, 154)',
                color: 'white' // Set the text color
              }}
              onClick={handleShowModalCreate} // Show modal on button click
              >
                create pin
              </Button>}

            </Stack>
          </Col>
        </Row>
      </Container>

      {/* Modal for changing PIN */}
      <Modal 
      show={showModal} onHide={handleCloseModal}
      >

        <Modal.Header closeButton>
          <Modal.Title>Change 4-Digit Locker PIN</Modal.Title>
        </Modal.Header>

        <Modal.Body>




          <Form className="mt-1" >

            {/* Old Pin */}
            <Form.Group controlId="oldPin">
              <Form.Label>Old PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter old PIN"
                value={oldPin}
                onChange={(e) => setOldPin(e.target.value)}
              />
              {error.pin1 && (
              <Alert variant="danger mt-2">
                {error.pin1Error}
              </Alert>
            )}
            </Form.Group>

            <br/>

            <Form.Group controlId="newPin">

            {/* New Pin */}
              <Form.Label>Confirm PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter new PIN"
                value={newPin}
                onChange={(e) => setNewPin(e.target.value)}
              />

            {/* Add an alert for incorrect old PIN */}
            {error.pin2 && (
              <Alert variant="danger mt-2">
                {error.pin2Error}
              </Alert>
            )}

            </Form.Group>


            <div className="d-flex justify-content-center align-items-center">
            <Button variant="primary" type="submit" className="my-3 p-2 "
            style={{
              background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
              color: 'white',
              width: "70%" // Set the text color
            }} 
            onClick={handleSubmit}
            >
              Save Changes
            </Button>

            </div>
          </Form>
        </Modal.Body>
      </Modal>

      {/* Modal for create PIN */}
      <Modal 
      show={showModalCreate} onHide={handleCloseModalCreate}
      >

        <Modal.Header closeButton>
          <Modal.Title>Create 4-Digit Locker PIN</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <Form onSubmit={handleSubmit}>

            {/* New Pin */}
            <Form.Group controlId="newPin">
              <Form.Label>New PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="new PIN"
                value={createPin.newPin}
                onChange={(e) => setCreatePIN({...createPin, newPin:e.target.value})}
              />
              {error.pin1 && (
              <Alert variant="danger mt-2">
                {error.pin1Error}
              </Alert>
            )}
            </Form.Group>

            <br/>

            <Form.Group controlId="confirmPIN">

            {/* Confirm Pin */}
              <Form.Label>Confirm PIN</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter confirm PIN"
                value={createPin.confirmPin}
                onChange={(e) => setCreatePIN({...createPin, confirmPin:e.target.value})}
              />
            {/* Add an alert for incorrect old PIN */}
            {error.pin2 && (
              <Alert variant="danger mt-2">
                {error.pin2Error}
              </Alert>
            )}
            </Form.Group>

            {/* Add an alert for incorrect old PIN */}
            {showAlert && (
              <Alert variant="danger">
                Incorrect old PIN. Please try again.
              </Alert>
            )}
            
            <div className="d-flex justify-content-center align-items-center">
            <Button variant="primary" type="submit" className="my-3 p-2 "
            style={{
              background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
              color: 'white',
              width: "70%" // Set the text color
            }} 
            onClick={handleSubmitCreate}
            >
              Create PIN
            </Button>

            </div>
          </Form>
        </Modal.Body>
      </Modal>
    </>
  );
};


export default UserDashboard;
