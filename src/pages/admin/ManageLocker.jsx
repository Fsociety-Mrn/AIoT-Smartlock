import { 
  Avatar,
  Divider,
  Fab, 
  Grid, 
  IconButton, 
  InputAdornment, 
  Stack, 
  Typography 
} from '@mui/material'
import { DesktopTextboxManage } from '../../Components/Textfield'
import React from 'react'


// icons
import PersonAddAltIcon from '@mui/icons-material/PersonAddAlt';
import SearchIcon from '@mui/icons-material/Search';
import PendingActionsIcon from '@mui/icons-material/PendingActions';
import EditIcon from '@mui/icons-material/Edit';
import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import { Box } from '@mui/system';


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
        <Typography variant='h4' 
        sx={{
          background: 'linear-gradient(to left, rgb(61, 152, 154) 70%, rgb(12, 14, 36) 100%)',
          // backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
        }} >Manage Access & Users</Typography>
      </Grid>
      
      
      {/* for search and generate token button */}
      <Grid item xs={12} md={11} >

        <Stack
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={2}
        > 

          {/* Search Bar */}
          <DesktopTextboxManage fullWidth placeholder='Search'
          InputProps={{
            
            startAdornment: 
              <InputAdornment position="start" variant="standard">
                <SearchIcon fontSize='large' />
              </InputAdornment>,
          }}

          sx={{
            '& .MuiOutlinedInput-root': {
              borderRadius: '20px', // Adjust the border radius
            },
          }}
          />


          {/* generate Tokens */}
          <IconButton  color="primary" 
          sx={{
            border: "2px solid rgb(61, 152, 154)",
            padding: 1.5,
          }}
          >
            <PersonAddAltIcon fontSize='large' />
          </IconButton>

          {/* pending Tokens */}
          <IconButton variant='circular' color="primary" 
          sx={{
            border: "2px solid rgb(61, 152, 154)",
            padding: 1.5,
          }}
          >
            <PendingActionsIcon fontSize='large' />
          </IconButton>

        </Stack>

      </Grid>
      

{/* DATA GRID ITO */}
      {/* user List */}
      <Grid item xs={11} md={11} margin={2}
      >

        <Grid 
        container 
        overflow={'auto'} 
        maxHeight={370} 
        spacing={2}
        sx={{
          border:"3px solid rgb(61, 152, 154)",
          borderRadius:"25px",
          scrollbarWidth: 'thin', // Add this property
          '&::-webkit-scrollbar': {
            width: '0.4em',
            background: 'transparent',
          },
          '&::-webkit-scrollbar': {
            width: '0.4em',
            background: 'transparent',
          },
          '&::-webkit-scrollbar-thumb': {
            backgroundColor: 'transparent',
          },
          '&:hover': {
            '&::-webkit-scrollbar-thumb': {
              backgroundColor: 'grey.400',
            },
          },

        }}
        padding={1}
        >

          {['A', 'B', 'C', 'D', 'E', 'F', 'G'].map(letter=>(
          <Grid item xs={12} key={letter}   
          sx={{
            '&:hover': {
              background: 'white',
              boxShadow: '0px 2px 3px rgba(0, 0, 0, 0.2)',
              borderRadius: '50px',
            },
          }} padding={2}>
            <Stack
            direction="row"
            justifyContent="flex-start"
            alignItems="center"
            spacing={2}
            > 
              <Avatar  sx={{ width: 56, height: 56 , bgcolor: 'rgb(61, 152, 154)'}}>{letter} </Avatar>
              <Typography variant='h5' component="div" 
              sx={{ 
                flexGrow: 1,
                background: 'linear-gradient(to left, rgb(12, 14, 36) 80%, rgb(61, 152, 154) 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
              }}
              
             
              > Hello Friend</Typography>
              
              <Fab color='primary' size='medium'
                sx={{
                  boxShadow: 'none',    
                  '&:hover': {
                      boxShadow: 'none',
                     
                  },
                }} 
                > <EditIcon fontSize='medium' /></Fab>

              <Fab color='error' size='medium'
                sx={{
                  boxShadow: 'none',    
                  '&:hover': {
                      boxShadow: 'none',
                  },
                }} 
              > <DeleteForeverIcon fontSize='medium' /></Fab>

            </Stack>
          
          </Grid>
          ))}
          
   
          
    

      </Grid>

      </Grid>
        
   
      
    </Grid>
    </div>
  )
}

export default ManageLocker