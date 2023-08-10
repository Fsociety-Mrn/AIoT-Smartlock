import React, { useState } from 'react';
import './Account.css'; // Link to your CSS file
import { LogoutSession } from '../../Authentication/Authentication'
import { 
  getUserName,
  getUserDetails,
  imageUpload, 
  updateDetails 
} from '../../firebase/Firestore'
import { statusLogin } from '../../firebase/FirebaseConfig'
import { 
  Avatar,
  Fab  
} from '@mui/material';
import { Stack } from '@mui/system';
import EditIcon from '@mui/icons-material/Edit';
import defaultImage from "../../Images/logo512.png"


const Account = () => {


  const [name, setName] = useState({
    uid: "",
    firstName: "",
    lastName: ""
  });

  const [isChangePasswordOpen, setIsChangePasswordOpen] = useState(false);
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');


  const handlePasswordChange = () => {
    setIsChangePasswordOpen(true);
  };

  const handleCloseChangePassword = () => {
    setIsChangePasswordOpen(false);
    setOldPassword('');
    setNewPassword('');
  };


  // get username in firestore
  React.useEffect(()=>{
    let isMounted = true;

    const fetchUserStatus = async () => {
      try {
        const user = await statusLogin();
        if (isMounted) {

          const details = await getUserDetails(user.uid)

          // const name = await getUserName(user.uid);

          console.log(details)

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
    // update dateils included images
  //  const result = await imageUpload(dataImage)

  if (dataImage) {
    imageUpload(dataImage,name.uid).then(url=>{
      updateDetails(
        name.uid, 
        String(name.lastName + "," + name.firstName),
        url);
    })
  }else{
    updateDetails(name.uid,String(name.lastName + "," + name.firstName));
  }
 
  };

  return (

    <div className="account-container">

      <div className="account-card">

        <h1>Profile Settings</h1>

        <form onSubmit={handleFormSubmit}>
          <Stack spacing={1}>

            <Stack 
            spacing={2}   
            direction="column"
            justifyContent="center"
            alignItems="center">

              <Avatar
              // alt={title}
              src={image}
              sx={{ width: 200, height: 200, border: "2px solid rgb(61, 152, 154)" }}
              >A</Avatar>

              <label htmlFor="contained-button-file" >
                <input 
                accept="image/*" 
                id="contained-button-file" 
                type="file" 
                onChange={uploadImage}
                hidden/>
                  <Fab color='primary' variant='extended' 
                  component="span" 
                  sx={{
                    textTransform: 'capitalize',
                    gap: 1
                  }}>
                    <EditIcon/>
                    Edit Image
                  </Fab>
              </label>
      
           </Stack>

            <label htmlFor="name">First name:</label>
            <input type="text" id="name" value={name.firstName} onChange={(e) => setName({...name, firstName:e.target.value})} required />
          
            <label htmlFor="name">Last name:</label>
            <input type="text" id="name" value={name.lastName} onChange={(e) => setName({...name, lastName: e.target.value})} required />

      
            <button type="submit">Save Changes</button>
          </Stack>
        </form>

          <div className="links">
            <button onClick={handlePasswordChange}>Change Password</button>
          </div>

          <div className="links">
            <button onClick={() => {LogoutSession();window.location.reload(); }}>Logout</button>
          </div>
      
      </div>


      {isChangePasswordOpen && (
        <div className="modal">
          <div className="card-modal">
            <h2>Change Password</h2>
            <label htmlFor="oldPassword">Old Password:</label>
            <input type="password" id="oldPassword" value={oldPassword} onChange={(e) => setOldPassword(e.target.value)} />

            <label htmlFor="newPassword">New Password:</label>
            <input type="password" id="newPassword" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} />
            <div className="button-group">
              <button className="cancel-button" onClick={handleCloseChangePassword}>Cancel</button>
              <button className="save-button" onClick={handleCloseChangePassword}>Save</button>
            </div>
          </div>
        </div>
      )}

    </div>

  );
}

export default Account;
