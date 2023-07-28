import React from 'react'
import { Avatar, Fab, Grid, Stack, Typography } from '@mui/material';

import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ICON from '../Images/logo512.png'

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

export default ContinueToMain