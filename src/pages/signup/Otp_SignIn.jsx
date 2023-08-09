import React, { useState, useEffect } from "react";

import {
  Avatar,
  Button,
  Grid,
  Stack,
  Typography,
  Link
} from '@mui/material';
import { DesktopTextbox } from '../../Components/Textfield';
import ICON from '../../Images/logo512.png';

// realtime database
import { verifyToken, generateToken } from '../../firebase/Realtime_Db';
import { createAccount } from '../../Authentication/Authentication';

// validation
import { SignUp_userSchema } from '../../Authentication/Validation';

const Otp_SignIn = () => {
  const [showEmail, setShowEmail] = React.useState(true);
  const [error, setError] = React.useState(false);
  const [tokenField, setTokenField] = React.useState('');

  // Expiration time state
  const [expirationTime, setExpirationTime] = React.useState(null);

  // token field
  const token = (e) => {
    setTokenField(e.target.value);
  };

  // verify button
  const verifyButton = (e) => {
    e.preventDefault();
    verifyToken(tokenField).then((e) => {
      setShowEmail(!e);
      setError(!e);
    });
  };

  // =============================== signup account

  const [user, setUser] = React.useState({
    email: '',
    password: '',
    confirmPassword: ''
  });

  const [errorSignUp, setErrorSignUp] = React.useState({
    email: false,
    emailError: '',
    password: false,
    passwordError: '',
    confirmPassword: false,
    confirmPasswordError: ''
  });

  // create account
  const createAccounts = (e) => {
    e.preventDefault();
    isValid(user.email, user.password, user.confirmPassword);
  };

  // validation
  const isValid = async (Email, Password, ConfirmPassword) => {
    try {
      // validate
      await SignUp_userSchema.validate(
        { email: Email, password: Password, confirmPassword: ConfirmPassword },
        { abortEarly: false }
      );

      createAccount(Email, ConfirmPassword)
        .then((res) => {
          console.log('Create Account Successful');
          setErrorSignUp({
            email: false,
            emailError: '',
            password: false,
            passwordError: '',
            confirmPassword: false,
            confirmPasswordError: ''
          });
        })
        .catch((err) => {
          setErrorSignUp({
            email: true,
            emailError: '',
            password: true,
            passwordError: '',
            confirmPassword: true,
            confirmPasswordError: err
          });
        });
    } catch (validationError) {
      // Extract specific error messages for email and password
      const emailError = validationError.inner.find((error) => error.path === 'email');
      const passwordError = validationError.inner.find((error) => error.path === 'password');
      const confirmPasswordError = validationError.inner.find(
        (error) => error.path === 'confirmPassword'
      );

      // If validation errors occur
      setErrorSignUp({
        email: !!emailError,
        emailError: emailError && emailError.message,
        password: !!passwordError,
        passwordError: passwordError && passwordError.message,
        confirmPassword: !!confirmPasswordError,
        confirmPasswordError: confirmPasswordError && confirmPasswordError.message
      });
    }
  };

  // Signup Details
  const Email = (e) => {
    setUser({ ...user, email: e.target.value });
  };

  const Password = (e) => {
    setUser({ ...user, password: e.target.value });
  };

  const ConfirmPassword = (e) => {
    setUser({ ...user, confirmPassword: e.target.value });
  };
  const MAX_ATTEMPTS = 3;

  const [otpGenerationCount, setOtpGenerationCount] = React.useState(0);
  const [expirationTimer, setExpirationTimer] = React.useState(null);

  // generate token
  const [temporaryToken, setTemporaryToken] = React.useState('');

  // Countdown Timer state
  const [countdown, setCountdown] = React.useState(0);
  const [MAXcountdown, setMAXCountdown] = React.useState(0);


  const generateOTP = () => {
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var otp = '';
    for (var i = 0; i < 6; i++) {
      var index = Math.floor(Math.random() * characters.length);
      otp += characters.charAt(index);
    }
    return otp;
  };

    // Current time state
    const [currentTime, setCurrentTime] = useState(new Date())
// Function to format time in "hh:mm:ss" format
const formatTime = (timeInSeconds) => {
  const hours = Math.floor(timeInSeconds / 3600);
  const minutes = Math.floor((timeInSeconds % 3600) / 60);
  const seconds = timeInSeconds % 60;
  return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
};

  // Function to generate a new OTP and set expiration time
  const handleGenerateToken = () => {
    if (otpGenerationCount < MAX_ATTEMPTS) {
      // Generate a new token
      const otp = generateOTP();
      setTokenField(otp);
  
      // Set expiration time (e.g., 10 seconds from now)
      const expirationTime = new Date();
      expirationTime.setSeconds(expirationTime.getSeconds() + 10);
      setExpirationTime(expirationTime);
  
      // Set temporaryToken
      setTemporaryToken(otp);
  
      // Increment otpGenerationCount
      setOtpGenerationCount((prevCount) => prevCount + 1);
  
      // Reset the countdown to show 10 seconds for the newly generated token
      setCountdown(10);
    } else {
      // If maximum attempts reached, check if enough time has passed
      const lastGeneratedTimestamp = localStorage.getItem("lastGeneratedTimestamp");
      if (lastGeneratedTimestamp) {
        const currentTime = new Date().getTime();
        const twentyFourHoursInMs = 24 * 60 * 60 * 1000;
        const difference = currentTime - parseInt(lastGeneratedTimestamp);
  
        if (difference < twentyFourHoursInMs) {
          // Disable the button and set the countdown for the remaining time
          const remainingTime = Math.floor((twentyFourHoursInMs - difference) / 1000);
          setCountdown(remainingTime);
          return;
        }
      }
  
      // If 24 hours have passed or it's the first attempt after 24 hours, generate a new token
      const otp = generateOTP();
      setTokenField(otp);
  
      // Set expiration time (e.g., 10 seconds from now)
      const expirationTime = new Date();
      expirationTime.setSeconds(expirationTime.getSeconds() + 10);
      setExpirationTime(expirationTime);
  
      // Set temporaryToken
      setTemporaryToken(otp);
  
      // Increment otpGenerationCount
      setOtpGenerationCount((prevCount) => prevCount + 1);
  
      // Save the current timestamp to localStorage
      localStorage.setItem("lastGeneratedTimestamp", new Date().getTime());
  
      // Reset the countdown to show 10 seconds for the newly generated token
      setCountdown(10);
    }
  };
 
  useEffect(() => {
    if (MAXcountdown > 0) {
      const MAXtimer = setInterval(() => {
        setMAXCountdown((prevCountdown) => prevCountdown - 1);
      }, 86400);

      // Clean up the interval when the component unmounts or the countdown reaches 0
      return () => clearInterval(MAXtimer);
    }
  }, [MAXcountdown]);


useEffect(() => {
    if (countdown > 0) {
      const timer = setInterval(() => {
        setCountdown((prevCountdown) => prevCountdown - 1);
      }, 1000);

      // Clean up the interval when the component unmounts or the countdown reaches 0
      return () => clearInterval(timer);
    }
  }, [countdown]);

  return (
    <>
      {showEmail ? (
        /* For verify email */
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <Grid
            container
            direction="row"
            justifyContent="center"
            alignItems="flex-start"
            spacing={0}
            style={{
              minHeight: '100vh'
            }}
            paddingTop={5}
          >
            <Grid item xs={12} xl={8} md={8} sm={5}>
              <Stack direction="column" justifyContent="center" alignItems="center" padding={2} spacing={2}>
                {/* Icons */}
                <Avatar
                  sizes="40px"
                  sx={{
                    bgcolor: '#e7e5d6b5',
                    height: '150px',
                    width: '150px',
                    border: '2px solid rgb(61, 152, 154)'
                  }}
                  src={ICON}
                >
                  S
                </Avatar>

                {/* OTP code textbox */}
                <DesktopTextbox
                  fullWidth
                  placeholder="Please type the OTP code"
                  value={tokenField}
                  onChange={token}
                  error={error}
                  helperText={error ? 'Invalid token' : ''}
                />

                {/* Buttons for verify cancel */}
                <Stack direction="row" justifyContent="center" alignItems="center" spacing={2}>
                  <Button
                    variant="outlined"
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
                        width: '100%'
                      },
                      width: '120px',
                      height: '50px'
                    }}
                  >
                    <Link href="/" sx={{ textDecoration: 'none' }}>
                      Cancel
                    </Link>
                  </Button>

                  <Button
                    variant="contained"
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
                        width: '100%'
                      },
                      width: '120px',
                      height: '50px'
                    }}
                    onClick={(e) => {
                      verifyButton(e);
                    }}
                  >
                    Verify
                  </Button>
                </Stack>

                <br />

                <Typography variant="h6">This token generator is temporary</Typography>
                <Typography>
                  <strong>{temporaryToken}</strong>
                </Typography>

                <Button
            variant="contained"
            onClick={handleGenerateToken}
            disabled={countdown > 0} 
          >
            Generate Token
          </Button>

                {/* Display expiration time */}
                {/*countdown > 0 && (
                  <Typography variant="body1">
                    Expiration Time: {expirationTime.toLocaleString()}
                  </Typography>
                  
                )*/}
                     {/* Display countdown timer */}
                     {countdown > 0 && (
                  <Typography variant="body2" color="error">
                  Expiration Time: {formatTime(countdown)}
                </Typography>
                    )}
                
                {otpGenerationCount >= MAX_ATTEMPTS && (
                <Typography variant="body1" color="error">
                  You have reached the maximum attempts for OTP generation. 
                  Please wait for 24 hrs to regenerate again. 
                </Typography>
              )}
             

           

              </Stack>
            </Grid>
          </Grid>
        </div>
      ) : (
        /* setup email and password */
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <Grid
            container
            direction="row"
            justifyContent="center"
            alignItems="flex-start"
            spacing={0}
            style={{
              minHeight: '100vh'
            }}
            paddingTop={5}
          >
          </Grid>
        </div>
      )}
    </>
  );
};

export default Otp_SignIn;
