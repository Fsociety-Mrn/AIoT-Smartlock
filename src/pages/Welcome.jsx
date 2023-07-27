import { Avatar, Button, Fab, Grid, Stack, Typography } from '@mui/material'
import React from 'react'
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ICON from '../Images/logo512.png'
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase/FirebaseConfig';
import { getUserName,updateName } from '../firebase/Firestore';

import { MobileTextbox } from '../Components/Textfield';

const Welcome = () => {


  const [currentUser, setCurrentUser] = React.useState(null);
  const [checkName,setName] = React.useState(null);
  const [UID,setUID] = React.useState(null);

  React.useEffect(() => {
    // Firebase auth listener to check for changes in user authentication status
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      if (user) {

        getUserName(user.uid)
        .then(result=>
          {
            // check if name has not yet change
            if (result === "first name, last name"){

              setCurrentUser(null);
              setName(true);
              setUID(user.uid);

            }else{
              setCurrentUser(result);
              setName(null);
            }
            

          }
        )
        .catch(err=>alert(err));

      } else {
        // User is signed out
        setCurrentUser(null);
      }
    });

    // Clean up the listener when the component unmounts
    return () => unsubscribe();
  }, []);



  return (
    <div>
      {checkName ? <UpdateName UID={UID}/> : <ContinueToMain currentUser={currentUser}/>}
  
      
    </div>
    
  )
}

export default Welcome


const ContinueToMain = ({currentUser}) =>{

  const [screenWidth, setScreenWidth] = React.useState(window.innerWidth);

 // Function to update the screen width state on window resize
  const handleResize = () => {
    setScreenWidth(window.innerWidth);
  };

  // Determine the variant based on the screen width
  const variant = screenWidth < 700 ? 'h5' : 'h4';
  const variantWelcome = screenWidth < 700 ? 'h4' : 'h3';

  React.useEffect(() => {

    window.addEventListener("resize", handleResize);
  
    // Clean up the listener when the component unmounts
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

      <Grid 
      container   
      direction="column"
      justifyContent="center"
      alignItems="center"
      spacing={1}
      style={{ 
        minHeight: "100vh"
      }}
      >
        <Stack   
        direction="column"
        justifyContent="center"
        alignItems="center" 
        spacing={3}>

          {/* Icon */}
          <Avatar
          src={ICON}
          sx={{ 
            width: 100, 
            height: 100,
            border: "3px solid rgb(61, 152, 154)" }}
          >H</Avatar>
          
          {/* Greetings */}
          <Typography 
          variant={variantWelcome} 
          // variant='h3'
          style={{ 
            backgroundImage: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)', 
            WebkitBackgroundClip: 'text', 
            WebkitTextFillColor: 'transparent' 
          }}
          >Hello Friend</Typography>
          
          {/* Username */}
          <Typography 
          variant={variant}  
          // variant='h4'
          noWrap
          style={{ 
            backgroundImage: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)', 
            WebkitBackgroundClip: 'text', 
            WebkitTextFillColor: 'transparent' 
          }}
          >{currentUser}</Typography>


        {/* Continue Button */}
          <Fab variant="extended" size="medium"  
          onClick={()=>window.location.reload()}         
          sx={{
            width: 200, // Adjust the width
            borderRadius: 25, // Added a border radius for a more rounded look
            height: 50, // Adjust the height
            color: "white",
            fontFamily: "sans-serif",
            padding: '10px 20px', // Adjust the padding
            background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)',
            textTransform: 'none',
            boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.25)', // Added a subtle shadow for depth
          }}>
            <Typography variant="body1" sx={{ fontWeight: 'bold',color: "white"}} >Continue</Typography>
            <ArrowForwardIcon sx={{ ml:2}}/>
          </Fab>

        </Stack>

      </Grid>
    </div>
  )
}

const UpdateName = ({UID}) => {

  const [name,setName] = React.useState({
    FirstName: "",
    LastName: ""
  })

  // uddate buton
  const saveChanges = e => {
    e.preventDefault();

    updateName(UID, String(name.LastName + "," + name.FirstName));
  }
  
  return (
  <div div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
    <Grid
    container   
    direction="row"
    justifyContent="center"
    alignItems="center"
    spacing={1}
  
    style={{ 
      minHeight: "100vh"
    }}
    > 
      <Stack   
      direction="column"
      justifyContent="center"
      alignItems="center"     spacing={1}
  
     >

        <Typography 
          variant='h5'
          style={{ 
            backgroundImage: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)', 
            WebkitBackgroundClip: 'text', 
            WebkitTextFillColor: 'transparent' 
          }}
        >
          Please Update Your Name.
        </Typography>

        <Grid
        container   
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={1}
        paddingLeft={3}
        paddingRight={2}
        > 
          <Grid item xs={6} sm={3} md={6} xl={6}>
            <MobileTextbox 
            fullWidth 
            label="First Name" 
            placeholder='Enter your first name'
            value={name.FirstName}
            onChange={e=>{
              setName({...name, FirstName: e.target.value})
            }}
            />
          </Grid>

          <Grid item xs={6} sm={3} md={6} xl={6}>
            <MobileTextbox 
            fullWidth 
            label="Last Name"  
            placeholder='Enter your last name'
            value={name.LastName}
            onChange={e=>{
              setName({...name, LastName: e.target.value})
            }}
            />
          </Grid>

          <Grid item xs={8}>

            {/* Save Chanegs */}
            <Button 
            variant='contained' 
            fullWidth
            style={{
              // background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, #e7e5d6b5 100%)',
              marginBottom: '15px',
              background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
              textTransform: 'none',
              fontFamily: 'sans-serif',
              borderRadius: 25,
              boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.25)',
              fontWeight: 'bold',
              fontSize: '16px',
              transition: 'background-color 0.3s ease',
                  // Mobile-specific styles
              '@media (maxWidth: 300px)': {
                  fontSize: '14px',
                  padding: '10px 16px',
                },
              }}
            onClick={saveChanges}
            >Save Changes</Button>
          </Grid>

        </Grid>

        
               

      </Stack>
     
    </Grid>
  </div>
  )
}