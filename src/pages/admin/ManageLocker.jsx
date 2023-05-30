import { 
  Avatar,
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

// data
import { userData } from '../../firebase/Firestore'

const ManageLocker = () => {
    // get windows screen
    const [state, setState] = React.useState(true);
    React.useEffect(()=>{
        const setResponsiveness = () => {
            return window.innerWidth < 700 ? setState(true) : setState(false);
        };
    
        setResponsiveness();
            window.addEventListener("resize", () => setResponsiveness());
        return () => {
            window.removeEventListener("resize", () => setResponsiveness());
        };
    },[])

  return (

    <div>
      {state ? <Mobile />  : <Desktop />}
    </div>
     

  )
}

const Desktop = () =>{

  // for data user
  const [dataUser, setDataUser] = React.useState([])

  React.useEffect(() => {

    // fetch the user List
    const fetchData = async () => {
      try {
        const data = await userData();
  
        data.forEach((item) => {
          setDataUser((prevData) => {
            // Check if the item already exists in the dataUser state
            if (!prevData.some((dataItem) => dataItem.id === item.id)) {
              return [...prevData, item]; // Add the item if it doesn't exist
            }
            return prevData; // Return the existing state if the item already exists
          });
        });
  

      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
    console.log(dataUser)
  }, [dataUser]);

  return(
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

        {dataUser.map(data=>(
        <Grid item xs={12} key={data.id}   
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

            {/* Profile */}
            <Avatar  sx={{ width: 56, height: 56 , bgcolor: 'rgb(61, 152, 154)'}} src={data.photoUrl}>A</Avatar>
            
            {/* Name */}
            <Typography variant='h5' component="div" 
            sx={{ 
              flexGrow: 1,
              background: 'linear-gradient(to left, rgb(61, 152, 154) 80%, rgb(12, 14, 36) 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
            }}
            
           
            > {data.user}</Typography>
          

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

const Mobile = () =>{
  const [dataUser, setDataUser] = React.useState([])

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await userData();
  
        data.forEach((item) => {
          setDataUser((prevData) => {
            // Check if the item already exists in the dataUser state
            if (!prevData.some((dataItem) => dataItem.id === item.id)) {
              return [...prevData, item]; // Add the item if it doesn't exist
            }
            return prevData; // Return the existing state if the item already exists
          });
        });
  

      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
    console.log(dataUser)
  }, [dataUser]);

  return(
  <div>
 
    <Grid 
    container   
    direction="row"
    justifyContent="flex-start"
    alignItems="flex-start"
    spacing={2}
    style={{ 
      marginTop: '100px' 
    }}
    padding={2}
    >
      {/* Title page */}
      <Grid item xs={12} md={12}>
        <Typography variant='h4' 
        sx={{
          background: 'linear-gradient(to left, rgb(61, 152, 154) , rgb(12, 14, 36) )',
        // backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
        }} >Manage Access & Users</Typography>
      </Grid>

      {/* Generate Token and Pending Token */}
      <Grid item xs={12}>
        <Stack
        direction="row"
        justifyContent="flex-end"
        alignItems="center"
        spacing={1}
        > 
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

      
      {/* Search bar */}
      <Grid item xs={12}>

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
      </Grid>

      {/* user List */}
      <Grid item xs={12} marginY={2} marginLeft={2}
      >
        <Grid 
        container 
        overflow={'auto'} 
        maxHeight={400} 
        spacing={2}
        sx={{
          border:"3px solid rgb(61, 152, 154)",
          borderRadius:"25px",
          scrollbarWidth: 'thin', // Add this property
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
          
          {dataUser.map(data=>(
          <Grid item xs={12} key={data.id}   
            sx={{
            '&:hover': {
              background: 'white',
              boxShadow: '0px 2px 3px rgba(0, 0, 0, 0.2)',
              borderRadius: '50px',
            },
            }} 
          padding={2}>

            <Stack
            direction="row"
            justifyContent="flex-start"
            alignItems="center"
            spacing={2}
            > 

              {/* Profile */}
              <Avatar  sx={{ width: 50, height: 50 , bgcolor: 'rgb(61, 152, 154)'}}>{data.photoUrl} </Avatar>

              {/* Name */}
              <Typography variant='h6' component="div" 
              sx={{ 
                flexGrow: 1,
                background: 'linear-gradient(to left, rgb(61, 152, 154) 30%, rgb(12, 14, 36) 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
              }}
              >{data.user}</Typography>

              <Fab color='error' size='small'
                sx={{
                  boxShadow: 'none',    
                  '&:hover': {
                    boxShadow: 'none',
                  },
                }} 
              > <DeleteForeverIcon fontSize='small' /></Fab>

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