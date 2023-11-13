import { 
  Card,
  Grid, 
  Typography,
  Button,
  Avatar,
  Stack,
  IconButton
} from '@mui/material';
import React from 'react';

import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import LockOpenOutlinedIcon from '@mui/icons-material/LockOpenOutlined';

const MyLocker = () => {
  const [paddinSize, setPaddingSize] = React.useState()

  React.useEffect(()=>{
    const setResponsiveness = () => {
        return window.innerWidth < 700 ? setPaddingSize(15) : setPaddingSize(0);
    };

    setResponsiveness();
    window.addEventListener("resize", () => setResponsiveness());
    return () => {
        window.removeEventListener("resize", () => setResponsiveness());
    };
  },[])

    const [sliderValue, setSliderValue] = React.useState(false);

  const handleClick = () => {
    setSliderValue(!sliderValue)
  };

  return (
    <div 
    style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: "100vh" }} 
    >

      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      marginTop={paddinSize}
      spacing={2}
      padding={2}
      >
        {/* <Grid item xs={10}>
          <Typography variant='h4' >My locker</Typography>
        </Grid> */}

        <Grid item xs={12} md={4}>
          <Card
          sx={{
            backgroundColor: "white",
            borderRadius: "20px",
            padding: "20px",
            margin: "10px"
          }}>
            
            <Stack
            direction="column"
            justifyContent="center"
            alignItems="center"
            spacing={1}>
            
              <Avatar 
              sx={{ width: '100px', height: '100px', border: '2px solid rgb(61, 152, 154)' }}
              >
                A
              </Avatar>

              <Stack
              direction="column"
              justifyContent="center"
              alignItems="center"
              spacing={0}>
                <Typography variant='h5' color="#0F2C3D" fontWeight="bold" fontSize="1.3rem">HELLO FRIEND</Typography>
                <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">Your Locker Number: 15</Typography>
              </Stack>

              <Button> Change your Locker Number </Button>
              <Button variant='contained' fullWidth>Generate face update OTP</Button>
              <Button variant='contained' fullWidth >change locker pin</Button>
            </Stack>

          </Card>
        </Grid>

        <Grid item xs={12} md={5}>
          <Card
          sx={{
            backgroundColor: "white",
            borderRadius: "20px",
            textAlign: "center", // Center the content
            alignItems: "center",
            padding: "40px",
            margin: "10px"
          }}>
            <Stack
            direction="column"
            justifyContent="center"
            alignItems="center"
            spacing={1}>

              <Typography variant='h5' color="#0F2C3D" fontWeight="bold" fontSize="1.3rem">
                Your locker is { !sliderValue ? "close" : "open"}
              </Typography>  

              <IconButton size="large" onClick={handleClick} color='primary' >
                {!sliderValue ? <LockOutlinedIcon fontSize='large'   style={{ fontSize: 100 }} /> 
                : <LockOpenOutlinedIcon fontSize='large'   style={{ fontSize: 100 }} />}
              </IconButton>

              <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">click to open your locker</Typography>
              
            </Stack>
          </Card>
        </Grid>



      </Grid>
    </div>
  );
};

export default MyLocker;
