import React from 'react'
import { 
    Avatar, 
    Button, 
    Grid, 
    // Snackbar, 
    Stack, 
    Typography
} from '@mui/material'
import { DesktopTextbox } from '../Components/Textfield';
import { useNavigate } from 'react-router-dom';
import { Email_validation } from '../Authentication/Validation'
import { ForgotPasswords } from '../firebase/FirebaseConfig'

import ICON from '../Images/logo512.png'


const ForgotPassword = () => {
let navigate = useNavigate();

const [email,setEmail] = React.useState({
    emailValue: "",
    emailError : false,
    emailErrorText:""
})

// const [state, setState] = React.useState({
//     open: false,
//     vertical: 'top',
//     horizontal: 'center',
//   });

const sendeEmail = async e => {
    e.preventDefault();
    try{
        await Email_validation.validate({ email: email.emailValue }, { abortEarly: false });
        // console.log(ForgotPasswords(email.emailValue));
        ForgotPasswords(email.emailValue)
            .then((response) => {
                setEmail({...email,
                    emailError: response.error,
                    emailErrorText: response.message,
                });

                navigate("/");
        })
        .catch((error) => {
            setEmail({...email,
                emailError: error.error,
                emailErrorText: error.message,
            })
        });

    }catch(validationError){
      // Extract specific er ror messages for email and password
     const EmailEror = validationError.inner.find((error) => error.path === 'email');
      
      setEmail({...email,
            emailError: !!EmailEror,
            emailErrorText: EmailEror && EmailEror.message,
        })
    }

}

// const handleClose = () => {
//     setState({ ...state, open: false });
//   };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

    {/* <Snackbar
    anchorOrigin={{ state.vertical, state.horizontal }}
    open={state.open}
    onClose={handleClose}
    message={email.emailErrorText}
    key={vertical + horizontal}
    /> */}

        <Grid 
        container   
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={1}
        style={{ 
            minHeight: "100vh"
        }}
        padding={2}>

            <Grid item xs={12} md={5} sm={12}>

                <Stack   
                direction="column"
                justifyContent="center"
                alignItems="center" 
                spacing={2}>

                    {/* Icon */}
                    <Avatar
                    src={ICON}
                    sx={{ 
                        width: 150, 
                        height: 150,
                        border: "3px solid rgb(61, 152, 154)" }}
                    >A</Avatar>

                    <Typography  
                    variant='h5'
                    noWrap
                    style={{ 
                        backgroundImage: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)', 
                        WebkitBackgroundClip: 'text', 
                        WebkitTextFillColor: 'transparent' 
                    }}
                    >Forgot your password?</Typography>

                    <DesktopTextbox 
                    fullWidth 
                    label="Email" 
                    placeholder='please enter your email'
                    value={email.emailValue}
                    onChange={e=>{
                        setEmail({...email, emailValue: e.target.value})
                    }}
                    helperText={email.emailErrorText}
                    error={email.emailError}
                    />

                    <Stack   
                    direction="row"
                    justifyContent="center"
                    alignItems="center" 
                    spacing={2}>

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
                            onClick={e=>{
                                e.preventDefault();
                                navigate("/")
                            }}
                            >

                            Cancel
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

                        onClick={sendeEmail}
                        >send</Button>

                    </Stack>
                </Stack>
            </Grid>
            
        </Grid>
    
    </div>
  )
}

export default ForgotPassword