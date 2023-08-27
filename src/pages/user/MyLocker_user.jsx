import React from 'react'
import { LogoutSession } from '../../Authentication/Authentication';
import {  Button, Grid, Stack } from '@mui/material';

// ICONS 
import LockRoundedIcon from '@mui/icons-material/LockRounded';
import LockOpenRoundedIcon from '@mui/icons-material/LockOpenRounded';

const Homepage = () => {
  return (
  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>

      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      padding={2}
      >

        {/* My Locker */}
        <Grid item xs={12} md={7} padding={2}>

          <Stack
          direction="column"
          justifyContent="center"
          alignItems="center"
          spacing={2}>

              <LockRoundedIcon sx={{ fontSize: 100 }} />

              <Button variant="outlined" startIcon={<LockOpenRoundedIcon />}>
                unlock facial
              </Button>

              <Button variant="outlined" startIcon={<LockOpenRoundedIcon />}>
                Change pin code
              </Button>

              <Button variant="outlined" startIcon={<LockOpenRoundedIcon />}>
              Update Facial
              </Button>


          </Stack>
        </Grid>


        {/* History */}
        <Grid item xs={12} md={5}>
          <h1>History of Login User</h1>
          <button onClick={(e)=>{
            LogoutSession();
            window.location.reload();
            }}>Logout</button>

        </Grid>



      </Grid>    


    </div>
  )
}

export default Homepage