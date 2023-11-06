import React, { useState } from "react";
import FormInput from "../../Forms/FormInput/FormInput";
import Titles from "../../Titles/Titles";
import { Form, Row, Col, Button, Stack } from "react-bootstrap";

// validation
import { Change_password } from "../../../utils/Validation/Validation";

// reset password 
import { updatePasswords } from "../../../utils/Firebase/Authentication/Authentication";


const UserInformation = ({ UID, firstName, lastName }) => {


  const [user,setUser] = useState({
    currentPassword: "",
    newPassword: "",
    confirmPassword: "",
  })

  const [error,setError] = useState({
    currentPassword: false,
    currentPasswordMessage: "",

    newPassword: false,
    newPasswordMessage: "",

    confirmPassword: false,
    confirmPasswordMessage: ""
  })

  const [showPasswordModal, setShowPasswordModal] = useState(false);

  const handleShowPasswordModal = () => {
    setShowPasswordModal(!showPasswordModal);
  };

 

  const handleUpdateName = async (e) => {
    try {
      e.preventDefault()

      await Change_password.validate({ 
        currentPassword: user.currentPassword, 
        newPassword: user.newPassword,
        confirmPassword: user.confirmPassword,
      }, { abortEarly: false });


      updatePasswords(user.currentPassword,user.confirmPassword).then(()=>{
        setError({
          currentPassword: false,
          currentPasswordMessage: "",
      
          newPassword: false,
          newPasswordMessage: "",
      
          confirmPassword: false,
          confirmPasswordMessage: ""
        })
      }
      ).then(err=>{
        setError({
          currentPassword: err.oldPassword,
          currentPasswordMessage: err.oldPasswordMessage,
      
          newPassword: true,
          newPasswordMessage: "",
      
          confirmPassword: true,
          confirmPasswordMessage: ""
        })
      })
      



  } catch (validationError) {
    
      // Extract specific error messages for email and password
      const currentPassword = validationError.inner.find((error) => error.path === 'currentPassword');
      const newPassword = validationError.inner.find((error) => error.path === 'newPassword');
      const confirmPassword = validationError.inner.find((error) => error.path === 'confirmPassword');

// If validation errors occur
      setError({
        currentPassword: !!currentPassword,
        currentPasswordMessage: currentPassword && currentPassword.message,

        newPassword: !!newPassword,
        newPasswordMessage: newPassword && newPassword.message,

        confirmPassword: !!confirmPassword,
        confirmPasswordMessage: confirmPassword && confirmPassword.message
      });



  }
  
  };

  return (
    <>
      <Titles
        title="Manage Your Password 🔐"
        text="Easily update or reset your password to keep your account secure."
      />
      <Form>
        <Row className="mt-3 px-2">

        {/* <div class="alert alert-warning" role="alert">
        Please generate face update OTP in the dashboard
        </div> */}

        <Stack gap={2} className="col-md-10 mx-auto"> 

        <FormInput
            xs={12}
            sm
            lg

            type={showPasswordModal ? 'text' : 'password'}

            as={Col}
            inpClass="py-2"
            // className="p-0"
            name="currentPassword"
            controlId="first-name-input"
            text="Current Password"
            placeholder="Enter your current password"
            size="sm"
            value={user.currentPassword}
            onChange={e=>setUser({...user, currentPassword: e.target.value})}

            valid={error.currentPassword}
            helperText={error.currentPasswordMessage}
          />
        
          <FormInput
            xs={12}
            sm
            lg
            as={Col}
            inpClass="py-2"

            type={showPasswordModal ? 'text' : 'password'}

            // className="p-0"
            name="newPassword"
            controlId="first-name-input"
            text="New Password"
            placeholder="Enter your new password"
            size="sm"
            value={user.newPassword}
            onChange={e=>setUser({...user, newPassword: e.target.value})}

            valid={error.newPassword}
            helperText={error.newPasswordMessage}
          />


          <FormInput
            xs={12}
            lg
            as={Col}
            inpClass="py-2"

            type={showPasswordModal ? 'text' : 'password'}

            // className="p-0 ms-lg-5 mt-3 mt-lg-0"
            name="confirmPassword"
            controlId="last-name-input"
            text="Confirm Password"
            placeholder="Confirm your new password"
            size="sm"
            value={user.confirmPassword}
            onChange={e=>setUser({...user, confirmPassword: e.target.value})}

            valid={error.confirmPassword}
            helperText={error.confirmPasswordMessage}
          />


          <Form.Check // prettier-ignore
          type="checkbox"
          id="Show Password"
          label="Show Password"
          style={{ color: "rgb(61, 152, 154)", borderColor: "rgb(12, 14, 36)"}}
          hecked={showPasswordModal}
          onChange={handleShowPasswordModal}
             />

        </Stack>
        </Row>


        <div className="d-flex justify-content-center align-items-center px-5 pt-3">

          <Stack gap={2} className="col-md-8 mx-auto">

          <Button
            variant="primary"

            onClick={handleUpdateName}

            style={{
                background: 'rgb(61, 152, 154)',
                color: 'white' // Set the text color
              }}

          >
            update password
          </Button>
          </Stack>
        </div>
      </Form>
    </>
  );
};


export default UserInformation;
