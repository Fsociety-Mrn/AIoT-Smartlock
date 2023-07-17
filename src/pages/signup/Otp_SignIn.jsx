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

    // create account
    const createAccounts = e =>{
        e.preventDefault();
        createAccount("test@rtu.edu.ph", "taylor123");
        // window.location.reload();
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
                        <DesktopTextbox fullWidth placeholder='please enter a valid email address'/>

                        {/* enter password */}
                        <Typography><strong>Create password</strong></Typography>
                        <DesktopTextbox fullWidth placeholder='create a password should be 6 char long'/>

                        {/* confirm password */}
                        <Typography><strong>Confirm password</strong></Typography>
                        <DesktopTextbox fullWidth placeholder='confirm your password'/>

     
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