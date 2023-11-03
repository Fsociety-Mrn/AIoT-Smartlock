import React, { useState } from "react";
import FormInput from "../../Forms/FormInput/FormInput";
import Titles from "../../Titles/Titles";
import { Form, Row, Col, Button, Modal, Stack } from "react-bootstrap";

import UserChangePassword from "../UserChangePassword/UserChangePassword";

// validation
import { Name_Schema } from "../../../utils/Validation/Validation";

// change name
import { updateName } from "../../../utils/Firebase/Firestore/Firestore"; 
import { updateData} from "../../../utils/Firebase/Database/Database";

const UserInformation = ({ UID, firstName, lastName }) => {


  const [user,setUser] = useState({
    firstName: firstName,
    lastName: lastName
  })

  const [error,setError] = useState({
    firstName: false,
    firstNameMessage: "",

    lastName: false,
    lastNameMessage: ""
  })

  const [showPasswordModal, setShowPasswordModal] = useState(false);

  const handleShowPasswordModal = () => {
    setShowPasswordModal(true);
  };

  const handleClosePasswordModal = () => {
    setShowPasswordModal(false);
  };

  const handleUpdateName = async (e) => {
    try {
      await Name_Schema.validate({ firstName: user.firstName, lastName: user.lastName }, { abortEarly: false });
      
      // // NOTE: KEY = History, NAME = FIRST AND LAST NAME UPPERCASE
      // const LOCK = await getData("LOCK",String(user.firstName + " " + user.lastName).toUpperCase())
      // console.log("LOCK", LOCK)

      // const History = await getData("History",String(user.firstName + " " + user.lastName).toUpperCase())
      // console.log("History", History)

      // const PIN = await getData("PIN",String(user.firstName + " " + user.lastName).toUpperCase())
      // console.log("PIN", PIN)

  

      updateName(UID, String(user.lastName + "," + user.firstName))
      .then(res=>{


        // LOCK UPDATED
        updateData("LOCK",String(firstName + " " + lastName).toUpperCase(), String(user.firstName + " " + user.lastName).toUpperCase())
          .then(result=>{

            // History
            updateData("History",String(firstName + " " + lastName).toUpperCase(), String(user.firstName + " " + user.lastName).toUpperCase())
            .then(result=>{

                       // PIN
                       updateData("PIN",String(firstName + " " + lastName).toUpperCase(), String(user.firstName + " " + user.lastName).toUpperCase())
                       .then(result=>{
                         console.log(result)
                         setError({
                           firstName: false,
                           firstNameMessage: "",
                           lastName: false,
                           lastNameMessage: ""
                         })
                         window.location.reload()
                     })
          })

        })



  
      })
      .catch(err=>{
        setError({
          firstName: true,
          firstNameMessage: err,
          lastName: true,
          lastNameMessage: ""
        })


      })


  } catch (validationError) {

      // Extract specific error messages for email and password
      const firstName = validationError.inner.find((error) => error.path === 'firstName');
      const lastName = validationError.inner.find((error) => error.path === 'lastName');

// If validation errors occur
      setError({
        firstName: !!firstName,
        firstNameMessage: firstName && firstName.message,

        lastName: !!lastName,
        lastNameMessage: lastName && lastName.message
      });



  }
  
  };

  return (
    <>
      <Titles
        title="Welcome to the Information"
        text="Check or change your information as you want"
      />
      <Form>
        <Row className="mt-5 px-2">

        <div class="alert alert-warning" role="alert">
          Please generate the token in dashbaord to update your Facial Biometrics
        </div>
        
          <FormInput
            xs={12}
            sm
            lg
            as={Col}
            inpClass="py-2"
            className="p-0"
            name="firstName"
            controlId="first-name-input"
            text="First Name"
            placeholder="Hello"
            size="sm"
            value={user.firstName}
            onChange={e=>setUser({...user, firstName: e.target.value})}

            valid={error.firstName}
            helperText={error.firstNameMessage}
          />


          <FormInput
            xs={12}
            lg
            as={Col}
            inpClass="py-2"
            className="p-0 ms-lg-5 mt-3 mt-lg-0"
            name="lastName"
            controlId="last-name-input"
            text="Last Name"
            placeholder="Friend"
            size="sm"
            value={user.lastName}
            onChange={e=>setUser({...user, lastName: e.target.value})}

            valid={error.lastName}
            helperText={error.lastNameMessage}
          />

          
        </Row>


        <div className="d-flex justify-content-center align-items-center p-3">

          <Stack gap={2} className="col-md-8 mx-auto">
            <Button
            onClick={handleUpdateName}
            variant="primary"
            style={{
                background: 'rgb(61, 152, 154)',
                color: 'white' // Set the text color
              }}

          >
            update
          </Button>
    
   

          <Button
            variant="primary"

            onClick={handleShowPasswordModal}

            style={{
                background: 'rgb(61, 152, 154)',
                color: 'white' // Set the text color
              }}

          >
            change Password
          </Button>
          </Stack>
        </div>
      </Form>

      {/* Password Change Modal */}
      <Modal show={showPasswordModal} onHide={handleClosePasswordModal}>
        <Modal.Header closeButton>
          <Modal.Title>Change Password</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {/* Create a separate component for the password change form */}
          <UserChangePassword />
        </Modal.Body>
      </Modal>
    </>
  );
};


export default UserInformation;
