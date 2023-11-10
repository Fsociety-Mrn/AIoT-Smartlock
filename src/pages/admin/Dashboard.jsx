import { Grid } from '@mui/material'
import React from 'react'

const Dashboard = () => {
  const [paddinSize, setPaddingSize] = React.useState(10)

  React.useEffect(()=>{
    const setResponsiveness = () => {
        return window.innerWidth < 700 ? setPaddingSize(17) : setPaddingSize(10);
    };

    setResponsiveness();
        window.addEventListener("resize", () => setResponsiveness());
    return () => {
        window.removeEventListener("resize", () => setResponsiveness());
    };
  },[])
    
  return (
    <div 
    // style={{
    //   display: 'flex',  
    //   justifyContent:'center', 
    //   alignItems:'flex-start', 
    //   height: '100vh'
    // }}
    >
      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="flex-start"
      sx={{
        height: "100vh"
      }}
      marginTop={paddinSize}
      spacing={2}

      >
        <Grid item xs={2} md={2} sm={2}  sx={{
          backgroundColor: "red"
        }}>
          Total Access
        </Grid>
 
        <Grid item xs={2} md={2} sm={2} sx={{
          backgroundColor: "white"
        }}>
          Facial Login
        </Grid>

        <Grid item xs={2} md={2} sm={2}  sx={{
          backgroundColor: "GrayText"
        }}>
          PIN Login
        </Grid>

        <Grid item xs={2} md={2} sm={2} sx={{
          backgroundColor: "violet"
        }}>
          IoT Access
        </Grid>

        <Grid item xs={2} md={2} sm={2} sx={{
          backgroundColor: "gray"
        }}>
          Failure
        </Grid>





      </Grid>
    </div>
  )
}

export default Dashboard