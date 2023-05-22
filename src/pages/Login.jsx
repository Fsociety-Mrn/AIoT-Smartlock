import React from 'react'

// components
import { 
  Avatar, 
  Box, 
  Button, 
  Divider, 
  Grid, 
  Link, 
  Paper, 
  Stack, 
  Typography  
} from '@mui/material'
import { MobileTextbox,DesktopTextbox } from '../Components/Textfield';

// validation
import {
  userSchema
} from '../Authentication/Validation'

  // --- Temporary Login
import { LoginSession } from '../Authentication/Authentication';

// icons
import GoogleIcon from '@mui/icons-material/Google';





const Login = () => {

  // get windows screen
const [state, setState] = React.useState(false);
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
    <>
      {state ? <Mobile />  : <Desktop />} 
    </>
  )
}

// Mobile view
const Mobile = () => {

  const [user, setUser] = React.useState({
    email: "",
    password: ""
  })

  const [error, setError] = React.useState(false)


  // Login Details
  const Email = (e) => {
    setUser({...user, email: e.target.value})
  }

  const Password = (e) => {
    setUser({...user, password: e.target.value})
  }


  // validation
  const isValid = async (Email,Password) =>{
    await userSchema.isValid({
      email: Email,
      password: Password
    }).then(result=>{
      setError(!result);
      console.log(result)

      if (result){
        LoginSession(user)
      }

    });

  }

  const Login = (e) =>{
    e.preventDefault();

    // check email and password validaty
    isValid(user.email,user.password)
  }
  

  return (
    <div style={{ 
    display: 'flex', 
    justifyContent: 'center', 
    alignItems: 'center' 
    }}>

      <Grid 
      container   
      direction="column"
      justifyContent="center"
      alignItems="center"
      style={{ 
        minHeight: "100vh"
      }}
      >

        <Grid item xs={8}>
          <Box
          sx={{
            width: '90vw',
            height: '80vh',
            backgroundColor: 'primary.dark',
            borderTopLeftRadius: '50px',
            background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
            // backgroundSize: '200% 200%',
            // backgroundPosition: 'left',
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center'
          }}
          >

            <Stack
            direction="column"
            justifyContent="center"
            alignItems="center"
            >

              {/* Icons */}
              <Avatar
              sizes='40px'
              sx={{ 
                bgcolor: "#e7e5d6b5",
                height: '150px', width: '150px'
              }}>S</Avatar>


              <Grid container       
              direction="row"
              justifyContent="center"
              alignItems="center" padding={2}>

          {/* email */}
                <MobileTextbox 
                type='email' 
                placeholder='Email'
                margin='dense' 
                variant="outlined" 
                fullWidth  
                size='medium'
                value={user.email}
                onChange={Email}
                error={error}
                />

          {/* password */}
                <MobileTextbox 
                type='password' 
                margin='dense'  
                variant="outlined" 
                fullWidth  
                size='medium'
                placeholder='Password'
                value={user.password}
                onChange={Password}
                error={error}
                />
                
                <Link href="#" 
                underline="always" 
                  style={{
                    color: 'white',
                    marginTop:'15px',
                    marginBottom: '20px'
                  }} >Forgot Password</Link>
                 
            {/* Login */}
                <Button 
                variant='contained' 
                fullWidth 
                style={{
                  // background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, #e7e5d6b5 100%)',
                  marginBottom: '15px',
                  background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)'
                  
                }}
                onClick={Login}
                >Login</Button>

                <Grid item xs={12}>
                  <Divider>
                    <Typography
                      style={{
                      color: '#FFFFFF'
                      }}>Or</Typography>
                    </Divider>
                </Grid>

                <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                spacing={2}
                marginTop={1}
                >
                  <Button variant='contained' fullWidth
                  startIcon={<GoogleIcon />}
                  style={{
                    color: 'rgb(11, 131, 120)',
                    backgroundColor: "white"
                  }}
                  >Login with Google</Button>
                </Stack>

              </Grid>

            </Stack>

          </Box>
        </Grid>

      </Grid>
    </div>
  )
}

// Desktop view
const Desktop = () => {

  const [user, setUser] = React.useState({
    email: "",
    password: ""
  })

  const [error, setError] = React.useState(false)


  // Login Details
  const Email = (e) => {
    setUser({...user, email: e.target.value})
  }

  const Password = (e) => {
    setUser({...user, password: e.target.value})
  }


  // validation
  const isValid = async (Email,Password) =>{

   await userSchema.isValid({
    email: Email,
    password: Password
   }).then(result=>{
      setError(!result)
   });

  }

  const Login = (e) =>{
    e.preventDefault();

    // Check if validation
    console.log(isValid(user.email,user.password))
    
  }

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
    
      <Grid 
      container   
      direction="row"
      justifyContent="center"
      alignItems="center"
      spacing={0}
      style={{ 
        minHeight: "100vh"
      }}
      >

        <Grid item>
          <Box
            sx={{
              
              width: 380,
              height: 530,
              backgroundColor: 'primary.dark',
              borderTopLeftRadius: '50px',
              background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
              // backgroundSize: '200% 200%',
              // backgroundPosition: 'left',
              display: 'flex', 
              justifyContent: 'center', 
              alignItems: 'center'
            }}
          >

            <Stack
            direction="row"
            justifyContent="center"
            alignItems="center"
            marginBottom={10}
            >
            <Avatar
            sizes='40px'
             sx={{ 
              bgcolor: "#e7e5d6b5",
              height: '280px', width: '280px'
            }}>S</Avatar>
            </Stack>
          
          </Box>

        </Grid>

        <Grid item>
          <Box
          sx={{
            width: 340,
            height: 530,
            backgroundColor: 'white',
            borderBottomRightRadius: '50px',
            display: 'flex', justifyContent: 'center', alignItems: 'center'
          }}
          >
            <Stack
            direction="column"
            justifyContent="center"
            alignItems="center"
            marginX={2}
            marginTop={5}
            >
            
              <Paper
              elevation={0}
              >
                {/* email */}
                <DesktopTextbox 
                type='email' 
                margin='dense' 
                placeholder='email' 
                variant="outlined" 
                fullWidth  
                size='medium'
                value={user.email}
                onChange={Email}
                error={error}
                />

                {/* password */}
                <DesktopTextbox 
                type='password' 
                margin='dense' 
                placeholder='password'  
                variant="outlined" 
                fullWidth  
                size='medium'
                value={user.password}
                onChange={Password}
                helperText={!error ? "" : "Please check email and password,password should contain min 6 char long"}
                error={error}
                />
                
                <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                padding={3}
                spacing={1}
                >
                  <Link href="#" style={{
                    color: 'rgb(11, 131, 120)'
                  }} >Forgot Password</Link>

                  {/* click Login */}
                  <Button variant='contained' fullWidth style={{
                    background:'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                    //background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%),'
                    textTransform: 'none' 
                  }}
                  onClick={Login}
       
                  >Login</Button>

                </Stack>

                <Divider orientation='horizontal' color='rgb(12, 14, 36)'>
                  <Typography
                  style={{
                    color: 'rgb(61, 152, 154)'
                  }}>Or</Typography>
                </Divider>

                <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                padding={3}
                spacing={1}
                >
                  <Button variant='contained' fullWidth
                  startIcon={<GoogleIcon />}
                  style={{
                    color: 'rgb(61, 152, 154)',
                    border: 'solid 2px rgb(61, 152, 154)',
                    backgroundColor: "white",
                    textTransform: 'none' 
                  }}
                  >Login with Google</Button>
                </Stack>

              </Paper>

            </Stack>

          </Box>
        </Grid>

      </Grid>

    </div>
  )
}



export default Login

