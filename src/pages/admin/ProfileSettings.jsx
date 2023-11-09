import React, { useState } from 'react';
import './ProfileSettings.css'; // Link to your CSS file
import { LogoutSession } from '../../Authentication/Authentication'
import { Change_password } from '../../Authentication/Validation'
import { 
  getUserDetails,
  imageUpload, 
  updateDetails 
} from '../../firebase/Firestore'
import { statusLogin,changing_password } from '../../firebase/FirebaseConfig'
import { Avatar, Fab, Grid, Typography } from '@mui/material';
import { DesktopTextbox, MobileTextbox } from '../../Components/Textfield';
import { Box, Stack } from '@mui/system';
import EditIcon from '@mui/icons-material/Edit';
import defaultImage from "../../Images/logo512.png"


const Account = () => {

  const [name, setName] = useState({
    uid: "",
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
  const [dataImage, setDataImage] = useState() //Data Image

  const uploadImage = e => {
    let fileReader = new FileReader();
    setDataImage(e.target.files[0])
    fileReader.readAsDataURL(e.target.files[0]);

    fileReader.onload = (event) => {
      setImage(event.target.result)
    }

  }

  // save changes
  const handleFormSubmit = (e) => {
    e.preventDefault();

    if (dataImage) {
      imageUpload(dataImage,name.uid).then(url=>{
        updateDetails(
          name.uid, 
          String(name.lastName + "," + name.firstName),
          url);})
    }else{
      updateDetails(name.uid,String(name.lastName + "," + name.firstName));
    }
 
  };

  // change password
  const [isChangePasswordOpen, setIsChangePasswordOpen] = useState(false);
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [errorChange, setErrorChange] = useState({
    currentPassword: false,
    currentPasswordError: '',
    newPassword: false,
    newPasswordError:''
  })
  

  // submit password
  const handlePasswordChange = e => {
    e.preventDefault();
    setIsChangePasswordOpen(true);
  };

  // change password 
  const handleCloseChangePassword = async e => {
    e.preventDefault();
    // setIsChangePasswordOpen(false);
    try{

      // validate passwords
      await Change_password.validate({ CurrentPassword: oldPassword , NewPassword: newPassword}, { abortEarly: false });
      
      // change password
      changing_password(oldPassword, newPassword)
        .then((result) => {
          setErrorChange({
            currentPassword: result.oldPassword,
            currentPasswordError: result.oldPasswordMessage,
          
            newPassword: result.newPassword,
            newPasswordError: result.newPasswordMessage,
          });

        })
        .catch((error) => {
          alert("Unexpected error:", error);
        });


    }catch(validationError){
      // Extract specific er ror messages for email and password
      const CurrentPassword = validationError.inner.find((error) => error.path === 'CurrentPassword');
      const NewPassword = validationError.inner.find((error) => error.path === 'NewPassword');
      
      setErrorChange({
          currentPassword: !!CurrentPassword,
          currentPasswordError: CurrentPassword && CurrentPassword.message,
        
          newPassword: !!NewPassword,
          newPasswordError: NewPassword && NewPassword.message,
        })

    }

  };


  // cancel password
  const handleCancelPassword = e => {
    e.preventDefault();
    setIsChangePasswordOpen(false);

    setOldPassword('');
    setNewPassword('');
  }


  return (

    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Grid 
      container   
      direction="row"
      justifyContent="center"
      alignItems="center"
      spacing={0}
      padding={2}
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

              <Typography variant='h5' color="black" fontWeight="lighter" fontSize="0.9rem">lisboamillen30@gmail.com</Typography>
            </Stack>

{/* ==================================== Update Password ==================================== */} 


            <DesktopTextbox 
            type="text" 
            id="oldPassword" 
            placeholder='Hello Friend'
            value={newPassword} 
            fullWidth
            onChange={(e) => setNewPassword(e.target.value)} 
            error={errorChange.newPassword}
            helperText={errorChange.newPasswordError}
            />

            <DesktopTextbox 
            type="text" 
            id="newPassword" 
            placeholder='Hello Friend'
            value={newPassword} 
            fullWidth
            onChange={(e) => setNewPassword(e.target.value)} 
            error={errorChange.newPassword}
            helperText={errorChange.newPasswordError}
            />

            <DesktopTextbox 
            type="text" 
            id="newPassword" 
            placeholder='Hello Friend'
            value={newPassword} 
            fullWidth
            onChange={(e) => setNewPassword(e.target.value)} 
            error={errorChange.newPassword}
            helperText={errorChange.newPasswordError}
            />
            
          </Stack>

        </Grid>

      </Grid>

    </div>

    // <div className="account-container">

    //   <div className="account-card">

    //     <h1>Profile Settings</h1>

    //     <form onSubmit={handleFormSubmit}>
    //       <Stack spacing={1}>

    //         <Stack 
    //         spacing={2}   
    //         direction="column"
    //         justifyContent="center"
    //         alignItems="center">




      
    //        </Stack>

    //         <label htmlFor="firstNames">First name:</label>
    //         <input type="text" id="firstNames" value={name.firstName} onChange={(e) => setName({...name, firstName:e.target.value})} required />
          
    //         <label htmlFor="lastNames">Last name:</label>
    //         <input type="text" id="lastNames" value={name.lastName} onChange={(e) => setName({...name, lastName: e.target.value})} required />

      
    //         <button type="submit">Save Changes</button>
    //       </Stack>
    //     </form>

    //       <div className="links">
    //         <button onClick={handlePasswordChange}>Change Password</button>
    //       </div>

    //       <div className="links">
    //         <button onClick={() => {LogoutSession();window.location.reload(); }}>Logout</button>
    //       </div>
      
    //   </div>


    //   {isChangePasswordOpen && (
    //     <div className="modal">
    //       <div className="card-modal">
    //         <h2>Change Password</h2>

    //         <label htmlFor="oldPassword">Old Password:</label>
    //         <DesktopTextbox 
    //         type="text" 
    //         id="oldPassword" 
    //         value={oldPassword} 
    //         fullWidth
    //         onChange={(e) => setOldPassword(e.target.value)} 
    //         error={errorChange.currentPassword}
    //         helperText={errorChange.currentPasswordError}
    //         />

    //         <br/>
    //         <br/>

    //         <label htmlFor="newPassword">New Password:</label>
    //         <DesktopTextbox 
    //         type="text" 
    //         id="newPassword" 
    //         value={newPassword} 
    //         fullWidth
    //         onChange={(e) => setNewPassword(e.target.value)} 
    //         error={errorChange.newPassword}
    //         helperText={errorChange.newPasswordError}
    //         />
            
    //         <div className="button-group">
    //           <button className="cancel-button" onClick={handleCancelPassword}>Cancel</button>
    //           <button className="save-button" onClick={handleCloseChangePassword}>Save</button>
    //         </div>
    //       </div>
    //     </div>
    //   )}

    // </div>

  );
}

export default Account;
