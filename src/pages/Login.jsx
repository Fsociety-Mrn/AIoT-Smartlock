import React from 'react'

// components
import { 
  Avatar, 
  Box, 
  Button, 
  Divider, 
  Grid, 
  IconButton, 
  InputAdornment, 
  Link, 
  Paper, 
  Stack, 
  Typography,
  
} from '@mui/material'
import { MobileTextbox,DesktopTextbox } from '../Components/Textfield';

// import { isAdmin } from '../firebase/Firestore'

// validation
import {
  userSchema
} from '../Authentication/Validation'

// --- Temporary Login
import { LoginSession } from '../Authentication/Authentication';

// icons
// import GoogleIcon from '@mui/icons-material/Google';
import ICON from '../Images/logo512.png'
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';

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

  
  const [showPassword, setShowPassword] = React.useState(false);

  const [error, setError] = React.useState({
    email: false,
    emailError: "",
    password: false,
    passwordError: ""
  })


  // Login Details
  const Email = (e) => {
    setUser({...user, email: e.target.value})
  }

  const Password = (e) => {
    setUser({...user, password: e.target.value})
  }


  // validation
  const isValid = async (Email,Password) =>{
    try {
      await userSchema.validate({ email: Email, password: Password }, { abortEarly: false });
      

      LoginSession(user).then(result=>{
          console.log(result)
          
          setError({
            email: false,
            emailError: "",

            password: false,
            passwordError: ""
          });

      }).catch((error) => {
        console.log("error",error); // Error message

          setError({
            email: true,
            emailError: "",

            password: true,
            passwordError: error
          });

      });


    } catch (validationError) {

      // Extract specific error messages for email and password
      const emailError = validationError.inner.find((error) => error.path === 'email');
      const passwordError = validationError.inner.find((error) => error.path === 'password');

      // If validation errors occur
      setError({
        email: !!emailError,
        emailError: emailError && emailError.message,

        password: !!passwordError,
        passwordError: passwordError && passwordError.message
      });
      
    }

  }

  const Login = (e) =>{
    e.preventDefault();

    // check email and password validaty
    isValid(user.email,user.password)
  }
  

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };


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
            // backgroundColor: 'primary.dark',
            borderTopLeftRadius: '50px',
            // backgroundColor: "white",
            // background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
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
            paddingTop={4}
            >

              {/* Icons */}
              <Avatar
              sizes='40px'
              sx={{ 
                bgcolor: "#e7e5d6b5",
                height: '150px', width: '150px',
                border: "2px solid rgb(61, 152, 154)"
              }}
              
              src={ICON}>S</Avatar>


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
                error={error.email}
                helperText={error.emailError}
                />

          {/* password */}
                <MobileTextbox 
                margin='dense'  
                variant="outlined" 
                fullWidth  
                size='medium'
                placeholder='Password'
                value={user.password}
                onChange={Password}
                error={error.password}
                helperText={error.passwordError}
                type={showPassword ? 'text' : 'password'}
                InputProps={{
                  endAdornment: 
                    <InputAdornment position="end">
                      <IconButton
                      aria-label="toggle password visibility"
                      onClick={handleClickShowPassword}
                      onMouseDown={handleMouseDownPassword}
                    
                      >
                        {showPassword ? <VisibilityOff /> : <Visibility />}
                      </IconButton>
                    </InputAdornment>
                }}
                />
                
                <Link href="/ForgotPassword" 
                underline="always" 
                fontFamily={'sans-serif'}
                  style={{
                    // color: 'white',
                    marginTop:'15px',
                    marginBottom: '20px'
                  }} ><strong>Forgot Password</strong></Link>
                 
            {/* Login */}
                <Button 
                variant='contained' 
                fullWidth 
                style={{
                  // background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, #e7e5d6b5 100%)',
                  marginBottom: '15px',
                  background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                  textTransform: 'none',
                  fontFamily: 'sans-serif',
                  borderRadius: 25,
                  boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.25)',
                  fontWeight: 'bold',
                  fontSize: '16px',
                  transition: 'background-color 0.3s ease',
                  // Mobile-specific styles
                  '@media (maxWidth: 700px)': {
                    fontSize: '14px',
                    padding: '10px 16px',
                  },
                }}
                onClick={Login}
                >Login</Button>

                <Grid item xs={12}>
                  <Divider>
                    <Typography
                      fontFamily={'sans-serif'}
                      style={{
                      // color: '#FFFFFF'
                      }}>Don't have an account ?</Typography>
                    </Divider>
                </Grid>

                <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                spacing={2}
                marginTop={1}
                >
            

                  {/* Signup Account */}
                  <Typography noWrap>
                    <Link 
                  href="/otp"
                    style={{ cursor: 'pointer' }}> 
                      <strong> Sign up here!</strong>
                    </Link> 
                  </Typography>
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

  const [error, setError] = React.useState({
    email: false,
    emailError: "",
    password: false,
    passwordError: ""
  })



  // Login Details
  const Email = (e) => {
    setUser({...user, email: e.target.value})
  }

  const Password = (e) => {
    setUser({...user, password: e.target.value})
  }


  // validation
  const isValid = async (Email,Password) =>{
    try {
      await userSchema.validate({ email: Email, password: Password }, { abortEarly: false });
      

      LoginSession(user).then(result=>{
          console.log(result)
          
          setError({
            email: false,
            emailError: "",

            password: false,
            passwordError: ""
          });

      }).catch((error) => {
        console.log("error",error); // Error message

          setError({
            email: true,
            emailError: "",

            password: true,
            passwordError: error
          });

      });


    } catch (validationError) {

      // Extract specific error messages for email and password
      const emailError = validationError.inner.find((error) => error.path === 'email');
      const passwordError = validationError.inner.find((error) => error.path === 'password');

      // If validation errors occur
      setError({
        email: !!emailError,
        emailError: emailError && emailError.message,

        password: !!passwordError,
        passwordError: passwordError && passwordError.message
      });
      
    }

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
            }}
            src={ICON}
            >S</Avatar>
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

              {/* <Typography>Hello Friend!</Typography>
              <Typography>This is AIoT Smartlock where you manage you locker Online</Typography> */}

                {/* email */}
                <DesktopTextbox 
                type='email' 
                margin='dense' 
                // label='Email'
                placeholder='Email'
                InputLabelProps={{
                  shrink: true,
                  style: {
                    color: 'rgb(11, 131, 120)',
                  },
                }}
                variant="outlined" 
                fullWidth  
                size='medium'
                value={user.email}
                onChange={Email}
                error={error.email}
                helperText={error.emailError}
       
                />

                {/* password */}
                <DesktopTextbox 
                type='password' 
                margin='dense' 
                placeholder='Password' 
                // label='Password'
     
                InputLabelProps={{
                  shrink: true,
                  style: {
                    color: 'rgb(11, 131, 120)',
                  },
                }} 
                variant="outlined" 
                fullWidth  
                size='medium'
                value={user.password}
                onChange={Password}
                error={error.password}
                helperText={error.passwordError}
                />
                
                <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                padding={2}
                spacing={2}
                >
                  <Link href="/ForgotPassword" fontFamily={'sans-serif'} 
                  style={{
                    color: 'rgb(11, 131, 120)'
                  }} > <strong>Forgot Password</strong></Link>

                  {/* click Login */}
                  <Button variant='contained' fullWidth  
                  style={{
                    background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                    textTransform: 'none',
                    fontFamily: 'sans-serif',
                    borderRadius: 25,
                    color: 'white', // Added explicit color to ensure text is visible
                    boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.25)', // Added a subtle shadow for depth
                    fontWeight: 'bold', // Added bold font weight
                    fontSize: '16px', // Adjusted font size for better readability
                    padding: '10px', // Adjusted padding for more comfortable touch interaction
                    transition: 'background-color 0.3s ease', // Added a smooth transition for hover effect
                  }}
                  onClick={Login}
    
                  >Log In</Button>

                </Stack>

                <Divider orientation='horizontal' color='rgb(12, 14, 36)'>
                  <Typography
                  fontFamily={'sans-serif'} 
                  style={{
                    color: 'rgb(61, 152, 154)'
                  }}>Don't have an account ?</Typography>
                </Divider>

                <Stack
                direction="column"
                justifyContent="center"
                alignItems="center"
                paddingY={1}
                spacing={1}
                >
                    {/* Signup Account */}
                    <Typography noWrap>
                      <Link 
                      href="/otp"
                      style={{ cursor: 'pointer' }}>   
                       <strong>Sign up here!</strong>
                      </Link> 
                    </Typography>

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

