import React, { useState } from 'react';
import './ProfileSettings.css'; // Link to your CSS file
import { Change_password } from '../../Authentication/Validation'
import { 
  getUserDetails, imageUpload, updateDetails,
} from '../../firebase/Firestore'
import { statusLogin,changing_password } from '../../firebase/FirebaseConfig'
import { Button,Stack,Avatar, Grid, Typography } from '@mui/material';
import { DesktopTextbox } from '../../Components/Textfield';

import FormControlLabel from '@mui/material/FormControlLabel';

import Checkbox from '@mui/material/Checkbox';

import EditIcon from '@mui/icons-material/Edit';
import defaultImage from "../../Images/logo512.png"



const Account = () => {

  const [name, setName] = useState({
    uid: "",
    email: "",
    firstName: "",
    lastName: ""
  });



  // get username in firestore
  React.useEffect(()=>{
    let isMounted = true;

    const fetchUserStatus = async () => {
      try {
        const user = await statusLogin();
        if (isMounted) {

          const details = await getUserDetails(user.uid)

          const [lastName, firstName] = details.user.split(",");
          setName({
            uid:user.uid,
            email: user.email,
            firstName: firstName,
            lastName: lastName
          });

          details.photoUrl ? setImage(details.photoUrl) : setImage(image)

        }
      } catch (error) {
        console.error('Error fetching user status:', error);
      }
    };

    fetchUserStatus();

    return () => {
      isMounted = false;
    };
  },[])


  // upload images
  const [image,setImage] = useState(defaultImage) //image

  const uploadImage = e => {
    const dataImage = e.target.files[0]

    if (e.target.files[0]) {
      imageUpload(dataImage,name.uid).then(url=>{
        updateDetails(
          name.uid, 
          String(name.lastName + "," + name.firstName),
          url);
  
        })
    }

  }

  // change password
  const [isChangePasswordOpen, setIsChangePasswordOpen] = useState(false);

  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPasswordPassword] = useState('');

  const [errorChange, setErrorChange] = useState({
    currentPassword: false,
    currentPasswordError: '',

    newPassword: false,
    newPasswordError:'',

    confirmPassword: false,
    confirmPasswordError:''
  })
  

  // submit password
  const handlePasswordChange = e => {
    e.preventDefault();
    setIsChangePasswordOpen(!isChangePasswordOpen);
  };

  // change password 
  const handleCloseChangePassword = async e => {
    e.preventDefault();
    // setIsChangePasswordOpen(false);
    try{

      // validate passwords
      await Change_password.validate({ 
        CurrentPassword: oldPassword, 
        NewPassword: newPassword,
        ConfirmPassword: confirmPassword
      }, { abortEarly: false });
      
      // change password
      changing_password(oldPassword, newPassword)
        .then((result) => {
          setErrorChange({
            currentPassword: result.oldPassword,
            currentPasswordError: result.oldPasswordMessage,
          
            newPassword: result.newPassword,
            newPasswordError: result.newPasswordMessage,

            confirmPassword: false,
            confirmPasswordError:''
          });

          window.location.reload()
        })
        .catch((error) => {
          alert("Unexpected error:", error);
        });


    }catch(validationError){
      // Extract specific er ror messages for email and password
      const CurrentPassword = validationError.inner.find((error) => error.path === 'CurrentPassword');
      const NewPassword = validationError.inner.find((error) => error.path === 'NewPassword');
      const ConfirmPassword = validationError.inner.find((error) => error.path === 'ConfirmPassword');

      setErrorChange({
          currentPassword: !!CurrentPassword,
          currentPasswordError: CurrentPassword && CurrentPassword.message,
        
          newPassword: !!NewPassword,
          newPasswordError: NewPassword && NewPassword.message,

          confirmPassword: !!ConfirmPassword,
          confirmPasswordError:ConfirmPassword && ConfirmPassword.message,
        })

    }

  };


  return (

    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
 
      <Grid 
      container   
      direction="row"
      justifyContent="center"
      alignItems="center"
      spacing={0}
      marginTop={12}
      paddingX={1}
      style={{ 
        minHeight: "100vh"
      }}
      >

        <Grid item xs={12} md={5} sm={12} 
        sx={{
          borderRadius: '20px',
          backgroundColor: 'white',
          padding: '30px'
        }}>
        
          <Stack 
          spacing={2}   
          direction="column"
          justifyContent="center"
          alignItems="center">


{/* ==================================== Profile Picture ==================================== */}
            <label htmlFor="contained-button-file">
              
              {/* Profile Avatar */}
              <div
              style={{
                width: '200px',
                height: '200px',
                border: '2px solid rgb(61, 152, 154)',
                borderRadius: "50%",
                position: 'relative',
                cursor: 'pointer',
              }}
              >

                <Avatar
                src={image}
                sx={{ width: '100%', height: '100%' }}
                >
                  A
                </Avatar>

                {/* Edit Profile Icon */}
                <div
                style={{
                  position: 'absolute',
                  bottom: '0',
                  right: '10px',
                  width: '40px',
                  height: '40px',
                  backgroundColor: '#EFECE3', // White circular background
                  borderRadius: '50%', // Circular shape
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
                >
                  <EditIcon size="20" color="rgb(61, 152, 154)" />
                </div>
              </div>

              {/* Edit Profile Input */}
              <input
              accept="image/*"
              id="contained-button-file"
              type="file"
              onChange={uploadImage}
              hidden
                />
            </label>

{/* ==================================== Name and Email ==================================== */} 
            <Stack 
            direction="column"
            justifyContent="center"
            alignItems="center">

              <Typography variant='h5' color="black" fontWeight="bold" fontSize="1.3rem">
                {String(name.firstName + " " + name.lastName).toUpperCase()} 
              </Typography>

              <Typography variant='h5' color="black" fontWeight="lighter" fontSize="0.9rem">{name.email}</Typography>
            </Stack>

{/* ==================================== Update Password ==================================== */} 
            
            {/* Old Password */}
            <DesktopTextbox 
            type={isChangePasswordOpen ? "text" : "password"}
            id="oldPassword" 
            placeholder='Old Password'
            value={oldPassword} 
            fullWidth
            onChange={(e) => setOldPassword(e.target.value)} 
            error={errorChange.currentPassword}
            helperText={errorChange.currentPasswordError}
            />

            {/* New Password */}
            <DesktopTextbox 
            type={isChangePasswordOpen ? "text" : "password"}
            id="newPassword" 
            placeholder='New Password'
            value={newPassword} 
            fullWidth
            onChange={(e) => setNewPassword(e.target.value)} 
            error={errorChange.newPassword}
            helperText={errorChange.newPasswordError}
            />

            {/* Confirm Password */}
            <DesktopTextbox 
            type={isChangePasswordOpen ? "text" : "password"}
            id="newPassword" 
            placeholder='Confirm Password'
            value={confirmPassword} 
            fullWidth
            onChange={(e) => setConfirmPasswordPassword(e.target.value)} 
            error={errorChange.confirmPassword}
            helperText={errorChange.confirmPasswordError}
            />

            {/* Show Password */}
            <FormControlLabel
            control={
              <Checkbox checked={isChangePasswordOpen} onChange={handlePasswordChange} />
            }
            label="Show Password"
          />
   
            
            {/* Change Password */}
            <Button
            fullWidth
            variant="contained"
            color="primary" // You can adjust the color based on your design
            style={{
              marginTop: '20px', // Add some spacing from the elements above
              borderRadius: '8px', // Add rounded corners for a modern look
            }}
            onClick={handleCloseChangePassword}
            >

              
              Change Password
            </Button>
    
          </Stack>

        </Grid>

      </Grid>

    </div>

  );
}

export default Account;
