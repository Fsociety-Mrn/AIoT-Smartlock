import { 
  Card,
  Grid, 
  Typography,
  Button,
  Avatar,
  Stack,
  Slider
} from '@mui/material';
import React from 'react';



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

  return (
    <div 
    style={{  minHeight: "100vh" }} 
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

        <Grid item xs={12} md={3}>
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
              sx={{ width: '100px', height: '100px' }}
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
            </Stack>

          </Card>
        </Grid>

        <Grid item xs={12} md={6}>
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
              spacing={2}>

                <Slider defaultValue={0} aria-label="Default" valueLabelDisplay="auto" />
                <Button variant='contained' fullWidth>Generate face update OTP</Button>
                <Button variant='contained' fullWidth>change locker pin</Button>
              </Stack>

          </Card>
        </Grid>



      </Grid>
    </div>
  );
};

export default MyLocker;
