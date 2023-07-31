import React from 'react'

import { LogoutSession } from '../../Authentication/Authentication';
import { Button, Grid, Stack, Typography } from '@mui/material';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '../../firebase/FirebaseConfig';
import { getUserName } from '../../firebase/Firestore';
import { generateToken_Facial } from '../../firebase/Realtime_Db'

const Homepage = () => {
  const [name, setName] = React.useState("");

  // generate token
  const [temporaryToken, setTemporarytoken] = React.useState("")

  const generateOTP = () => {
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var otp = '';
    for (var i = 0; i < 6; i++) {
        var index = Math.floor(Math.random() * characters.length);
        otp += characters.charAt(index);
    }
    return otp;
}

  const unsubscribe = onAuthStateChanged(auth, (user) => {
    if (user) {

      getUserName(user.uid)
      .then(result=>{ 

        setName(result);
  
      })
      .catch(err=>alert(err));
   
    }

    // Clean up the listener when the component unmounts
    return () => unsubscribe();
    }, []);


  return (
    <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>    
    <Grid
    container
    direction="column"
    justifyContent="center"
    alignItems="center"
    spacing={2}
    >
      <Grid item xs={12}>
        <Typography variant='h6'>{name}</Typography>
      </Grid>

      <Grid item xs={12}>
        <Button variant='outlined' 
        onClick={(e)=>{
          LogoutSession();
          window.location.reload();
        }}>Logout</Button>
      </Grid>
      
      <Grid item xs={12}>
        <Stack
        direction="column"
        justifyContent="center"
        alignItems="center"
        spacing={2}
        >
          <Typography variant='h6'>This token generator is temporary for facial Update</Typography>
          <Typography><strong>{temporaryToken}</strong></Typography>

          <Button 
          variant="contained" 
          onClick={e=>{
            e.preventDefault();

            const tokens = generateOTP();
            setTemporarytoken(tokens);
            generateToken_Facial(name, tokens);

          }}>Generate Token</Button>

        </Stack>
      </Grid>
      
      


  </Grid>
    </div>
  )
}

export default Homepage