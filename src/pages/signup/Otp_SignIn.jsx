import React from 'react'
import { 
    Avatar,
    Button,
    Grid, 
    Stack, 
    Typography,
    Link
} from '@mui/material'


import { DesktopTextbox } from '../../Components/Textfield';
import ICON from '../../Images/logo512.png'

// realtime database
import { verifyToken } from '../../firebase/Realtime_Db'
import { createAccount } from '../../Authentication/Authentication'

// validation
import { SignUp_userSchema } from '../../Authentication/Validation'
const Otp_SignIn = () => {
    const [showEmail, setShowEmail] = React.useState(false);
    const [error, setError] = React.useState(false);
    const [tokenField, setTokenField] = React.useState("");



    // token field 
    const token = e =>{
        setTokenField(e.target.value)
    }

    // verify button
    const verifyButton = e =>{
        e.preventDefault();
        // setShowEmail(false);
        verifyToken(tokenField)
        .then(e=>{
                setShowEmail(!e);
                setError(!e);
            }
        );
    }


    // =============================== signup account


    const [user, setUser] = React.useState({
        email: "",
        password: "",
        confirmPassword: ""
      })
    
      const [errorSignUp, setErrorSignUp] = React.useState({
        email: false,
        emailError: "",
        password: false,
        passwordError: "",
        confirmPassword: false,
        confirmPasswordError: ""
      })
    
    // create account
    const createAccounts = e =>{
        e.preventDefault();

        isValid(user.email,user.password,user.confirmPassword);

        // createAccount("test@rtu.edu.ph", "taylor123");
        // window.location.reload();
    }

    // validation
    const isValid = async(Email,Password,ConfirmPassword) =>{
        try{

            // validate
            await SignUp_userSchema.validate({ email: Email, password: Password , confirmPassword: ConfirmPassword}, { abortEarly: false });
            
            createAccount(Email, ConfirmPassword)
            .then(res=>{

                console.log("Create Account Succesfull");
                setErrorSignUp({
                    email: false,
                    emailError: "",
        
                    password: false,
                    passwordError: "",
        
                    confirmPassword: false,
                    confirmPasswordError: "",
                });
            })
            .catch(err=>{
                setErrorSignUp({
                    email: true,
                    emailError: "",
        
                    password: true,
                    passwordError: "",

                    confirmPassword: true,
                    confirmPasswordError: err,
                  });
            })


        }catch(validationError){

            // Extract specific er ror messages for email and password
            const emailError = validationError.inner.find((error) => error.path === 'email');
            const passwordError = validationError.inner.find((error) => error.path === 'password');
            const confirmPasswordError = validationError.inner.find((error) => error.path === 'confirmPassword');

            // If validation errors occur
            setErrorSignUp({
                email: !!emailError,
                emailError: emailError && emailError.message,

                password: !!passwordError,
                passwordError: passwordError && passwordError.message,

                confirmPassword: !!confirmPasswordError,
                confirmPasswordError: confirmPasswordError && confirmPasswordError.message,
            });
        }
    }

    // Signup Details
    const Email = (e) => {
        setUser({...user, email: e.target.value})
    }

    const Password = (e) => {
        setUser({...user, password: e.target.value})
    }

    const ConfirmPassword = (e) => {
        setUser({...user, confirmPassword: e.target.value})
    }


  return (
    <>
    {showEmail ? 

    /* For verify email */
        (<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <Grid 
            container   
            direction="row"
            justifyContent="center"
            alignItems="flex-start"
            spacing={0}
            style={{ 
                minHeight: "100vh"
            }}
            paddingTop={5}
            >   
                <Grid item xs={12} xl={8} md={8} sm={5}>

                    <Stack
                    direction="column"
                    justifyContent="center"
                    alignItems="center"
                    padding={2}
                    spacing={2}
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
                        
                        {/* OTP code textbox */}
                        <DesktopTextbox 
                        fullWidth 
                        placeholder='Please type the OTP code'
                        value={tokenField}
                        onChange={token}
                        error={error}
                        helperText={error ? "invalid token" : ""}
                        />

                        {/* Buttons for verify cancel */}
                        <Stack
                        direction="row"
                        justifyContent="center"
                        alignItems="center"

                        spacing={2}
                        >
                            <Button
                            variant='outlined' 
                            style={{
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
                                    width: '100%',
                                },
                                width: '120px',
                                height: '50px',
                               
                            }}
                            >
                            <Link href="/" sx={{
                                textDecoration: 'none'
                            }}>
                                Cancel
                            </Link>
                            
                            </Button>

                            <Button 
                            
                            variant='contained' 
                            style={{
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
                                    width: '100%',
                                },
                                width: '120px',
                                height: '50px',
                            }}
                            onClick={e=>{verifyButton(e)}}
                            >Verify</Button>

                            
                        </Stack>

                    </Stack>
                </Grid>

         

            </Grid>
        </div>) : 

        /* setup email and password */
        (<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <Grid 
            container   
            direction="row"
            justifyContent="center"
            alignItems="flex-start"
            spacing={0}
            style={{ 
                minHeight: "100vh"
            }}
            paddingTop={5}
            >
                <Grid item xs={12} xl={8} md={8} sm={12}>

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
                            height: '150px', width: '150px',
                            border: "2px solid rgb(61, 152, 154)"
                        }}
                        src={ICON}>S</Avatar>

                    </Stack>  
                </Grid>

                <Grid item xs={12} xl={8} md={8} sm={12}>
                    <Stack
                    direction="column"
                    justifyContent="center"
                    alignItems="flex-start"
                    padding={2}
                    spacing={2}
                    >

                        {/* Email */}
                        <Typography> <strong>Email</strong></Typography>
                        <DesktopTextbox 
                        fullWidth 
                        type='email' 
                        placeholder='please enter a valid email address'

                        value={user.email}
                        onChange={Email}

                        error={errorSignUp.email}
                        helperText={errorSignUp.emailError}
                        />

                        {/* enter password */}
                        <Typography><strong>Create password</strong></Typography>
                        <DesktopTextbox 
                        fullWidth 
                        type='password' 
                        placeholder='create a password should be 6 char long'

                        value={user.password}
                        onChange={Password}
 
                        error={errorSignUp.password}
                        helperText={errorSignUp.passwordError}
                        />

                        {/* confirm password */}
                        <Typography><strong>Confirm password</strong></Typography>
                        <DesktopTextbox 
                        fullWidth 
                        type='password' 
                        placeholder='confirm your password'

                        value={user.confirmPassword}
                        onChange={ConfirmPassword}    

                        error={errorSignUp.confirmPassword}
                        helperText={errorSignUp.confirmPasswordError}
                        />

     
                    </Stack>
                </Grid>

                <Grid item  xs={12} xl={8} md={8} sm={12}>
                   {/* Buttons for create and cancel */}
                   <Stack
                        direction="row"
                        justifyContent="center"
                        alignItems="center"
                        paddingBottom={20}
                        spacing={2}
                        >
                            <Button
                            variant='outlined' 
                            style={{
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
                                    width: '100%',
                                },
                                width: '120px',
                                height: '50px',
                               
                            }}
                            > 
                            <Link href="/" sx={{
                                textDecoration: 'none'
                            }}>
                                Cancel
                            </Link></Button>

                            <Button 
                            
                            variant='contained' 
                            style={{
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
                                    width: '100%',
                                },
                                width: '120px',
                                height: '50px',
                            }}
                            onClick={e=>createAccounts(e)}
                            >Create</Button>

                            
                        </Stack>
                </Grid>

            </Grid>
        </div>)}
    </>
  )
}






export default Otp_SignIn