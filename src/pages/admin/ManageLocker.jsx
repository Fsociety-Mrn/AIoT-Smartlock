import { Fab, Grid, IconButton, Stack, TextField, Typography } from '@mui/material'
import React from 'react'


// icons
import PersonAddAltIcon from '@mui/icons-material/PersonAddAlt';

const ManageLocker = () => {
  return (
    <div style={{ overflowX: 'hidden' }} >    
    <Grid 
      container   
      direction="row"
      justifyContent="flex-start"
      alignItems="flex-start"
      spacing={2}
      style={{ 
        marginLeft: '30px', marginTop: '35px' 
      }}
      padding={5}

      >

      {/* Title page */}
      <Grid item xs={12} md={12}>
        <Typography variant='h4' sx={{
          background: 'linear-gradient(to right, rgb(12, 14, 36), rgb(61, 152, 154))',
          // backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
        }} >Manage Access & Users</Typography>
      </Grid>
      

      <Grid item xs={11} md={11} >

        <Stack
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={2}
        > 

          {/* Search Bard */}
          <TextField fullWidth placeholder='Search'/>

          {/* generate Tokens */}
          <Fab color="primary" aria-label="add">
            <PersonAddAltIcon />
          </Fab>

        </Stack>

      </Grid>
        
        
   
      
    </Grid>
    </div>
  )
}

export default ManageLocker