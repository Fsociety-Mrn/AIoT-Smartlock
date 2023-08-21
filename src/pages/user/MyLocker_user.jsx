import React from 'react'
import { LogoutSession } from '../../Authentication/Authentication';
import { Avatar, Grid, Stack } from '@mui/material';

const Homepage = () => {
  return (
    <div style={{height: '100vh'}}>


      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="flex-start"
      padding={2}
      >

        <Grid item xs={12}>

          <Stack
          direction="row"
          justifyContent="flex-end"
          alignItems="flex-start"
          spacing={2}
          >
            <Avatar sx={{ width: 56, height: 56, border: "2px solid rgb(61, 152, 154)"}}>A</Avatar>
          </Stack>

        </Grid>
        <h1>User</h1>
        <button onClick={(e)=>{
      LogoutSession();
      window.location.reload();
      }}>Logout</button>
      </Grid>    


    </div>
  )
}

export default Homepage