import { 
    Backdrop, 
    Box, 
    Fade, 
    Grid, 
    Modal, 
    Typography, 
    Button, 
    FormControlLabel,
    Checkbox
} from "@mui/material"
import { DesktopTextbox } from '../Textfield';
import React from "react"
import { createPIN,verifyPIN } from "../../firebase/Realtime_Db";
import { pinSchema,NewpinSchema, Password_validation } from "../../Authentication/Validation";
import { reauthentication } from "../../firebase/FirebaseConfig";
import { setUserStatus } from "../../firebase/Firestore";

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: "400px",
    bgcolor: 'background.paper',
    // border: '2px solid #000',
    boxShadow: 24,
    borderRadius: "10px",
    p: 4
};

export const CreatePassword = (props) => {

    const handleClose = () => props.setCreateModal(false);

    const [createPin,setCreatePIN] = React.useState({
        newPin: "",
        confirmPin: ""
    })

    const [error,setError] = React.useState({
        pin1: false,
        pin1Error: "",
    
        pin2: false,
        pin2Error: ""
    })

    const [isChangePasswordOpen, setIsChangePasswordOpen] = React.useState(false);

    
    // Function to handle form submission for 
    const handleSubmitCreate = async (event) => {
        event.preventDefault();
        try {

            await pinSchema.validate({ PIN: createPin.newPin, PIN2: createPin.confirmPin }, { abortEarly: false });
     
      
            createPIN(props.FullName,createPin.confirmPin, props.LockerNumber).then(e=>{
                setError({
                    pin1: false,
                    pin1Error: "",
      
                    pin2: false,
                    pin2Error: ""
                })
                alert("PIN Successfully Created! ✔️")
                handleClose()
                window.location.reload()
            })
        } catch (validationError) {

            // Extract specific error messages for email and password
            const emailError = validationError.inner.find((error) => error.path === 'PIN');
            const passwordError = validationError.inner.find((error) => error.path === 'PIN2');

            // If validation errors occur
            setError({
                pin1: !!emailError,
                pin1Error: emailError && emailError.message,

                pin2: !!passwordError,
                pin2Error: passwordError && passwordError.message
            });

        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setCreatePIN((prevUser) => ({
          ...prevUser,
          [name]: value,
        }));
    };

      // submit password
    const handlePasswordChange = e => {
        e.preventDefault();
        setIsChangePasswordOpen(!isChangePasswordOpen);
    };

    return (
        <div>  
            <Modal
            open={props.createModal}
            onClose={handleClose}
            closeAfterTransition
            slots={{ backdrop: Backdrop }}
            slotProps={{
                backdrop: {
                timeout: 500,
            },
            }}>
                <Fade in={props.createModal}>
                    <Box sx={style}>

                        <Typography variant='h5' color="#0F2C3D" fontWeight="BOLD" fontSize="1rem">
                        Create 4 digit pin code
                        </Typography>

                        <Grid container spacing={1} padding={2}
                        direction="row"
                        justifyContent="center"
                        alignItems="center">

                            <Grid item xs={12}>
                                <DesktopTextbox fullWidth             
                                id="newPin"
                                name="newPin"
                                placeholder='New PIN'
                                value={createPin.newPin}
                                onChange={handleInputChange}

                                error={error.pin1}
                                helperText={error.pin1Error}

                                type={isChangePasswordOpen ? "text" : "password"}
                                />
                            </Grid>

                            <Grid item xs={12}>
                                <DesktopTextbox fullWidth             
                                id="confirmPin"
                                name="confirmPin"

                                placeholder='Confirm PIN' 
                                onChange={handleInputChange}
                                value={createPin.confirmPin}

                                error={error.pin2}
                                helperText={error.pin2Error}

                                type={isChangePasswordOpen ? "text" : "password"}
                                />
                            
                            {/* Show Password */}
            <FormControlLabel
            control={
              <Checkbox checked={isChangePasswordOpen} onChange={handlePasswordChange} />
            }
            label="Show PIN code"
          />
                            </Grid>

            
                            <Grid item xs={10}>
                                <Button fullWidth 
                                onClick={handleSubmitCreate}
              
                                variant="contained">Create PIN</Button>
                            </Grid>

               
                        </Grid>
                    </Box>
                </Fade>
            </Modal>
        </div>
    )
}

export const ChangePassword = (props) => {

    const handleClose = () => props.setCreateModal(false);

    const [createPin,setCreatePIN] = React.useState({
        oldPin: "",
        newPin: ""
    })

    const [error,setError] = React.useState({
        pin1: false,
        pin1Error: "",
    
        pin2: false,
        pin2Error: ""
    })

    const [isChangePasswordOpen, setIsChangePasswordOpen] = React.useState(false);

    
    // Function to handle form submission for 
    const handleSubmitCreate = async (event) => {
        event.preventDefault();
        try {

            await NewpinSchema.validate({ PIN: createPin.oldPin, PIN2: createPin.newPin }, { abortEarly: false });
            
  
            verifyPIN(props.FullName, createPin.oldPin).then(result=>{
      
              // if pincode is verified
              result && createPIN(props.FullName,createPin.newPin, props.LockerNumber).then(result=> {     
                setError({
                  pin1: false,
                  pin1Error: "",
            
                  pin2: false,
                  pin2Error: ""
                })

                alert(
                    "PIN successfully change ✔️"
                )
      
                    
                handleClose()
                window.location.reload()
              })
      
              // if pincode is verified
              !result && setError({ pin1: false, pin1Error: "", pin2: true, pin2Error: "old pin is not verified" })
            })

        } catch (validationError) {

            // Extract specific error messages for email and password
            const emailError = validationError.inner.find((error) => error.path === 'PIN');
            const passwordError = validationError.inner.find((error) => error.path === 'PIN2');

            // If validation errors occur
            setError({
                pin1: !!emailError,
                pin1Error: emailError && emailError.message,

                pin2: !!passwordError,
                pin2Error: passwordError && passwordError.message
            });

        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setCreatePIN((prevUser) => ({
          ...prevUser,
          [name]: value,
        }));
    };

      // submit password
    const handlePasswordChange = e => {
        e.preventDefault();
        setIsChangePasswordOpen(!isChangePasswordOpen);
    };

    return (
        <div>  
            <Modal
            open={props.createModal}
            onClose={handleClose}
            closeAfterTransition
            slots={{ backdrop: Backdrop }}
            slotProps={{
                backdrop: {
                timeout: 500,
            },
            }}>
                <Fade in={props.createModal}>
                    <Box sx={style}>

                        <Typography variant='h5' color="#0F2C3D" fontWeight="BOLD" fontSize="1rem">
                        Input 4 digit pin code
                        </Typography>

                        <Grid container spacing={1} padding={2}
                        direction="row"
                        justifyContent="center"
                        alignItems="center">

                            <Grid item xs={12}>
                                <DesktopTextbox fullWidth             
                                id="oldPin"
                                name="oldPin"
                                placeholder='Old PIN'
                                value={createPin.oldPin}
                                onChange={handleInputChange}

                                error={error.pin1}
                                helperText={error.pin1Error}

                                type={isChangePasswordOpen ? "text" : "password"}
                                />
                            </Grid>

                            <Grid item xs={12}>
                                <DesktopTextbox fullWidth             
                                id="newPin"
                                name="newPin"

                                placeholder='New PIN' 
                                onChange={handleInputChange}
                                value={createPin.newPin}

                                error={error.pin2}
                                helperText={error.pin2Error}

                                type={isChangePasswordOpen ? "text" : "password"}
                                />
                            
                            {/* Show Password */}
            <FormControlLabel
            control={
              <Checkbox checked={isChangePasswordOpen} onChange={handlePasswordChange} />
            }
            label="Show Password"
          />
                            </Grid>

            
                            <Grid item xs={10}>
                                <Button fullWidth 
                                onClick={handleSubmitCreate}
              
                                variant="contained">Save Changes</Button>
                            </Grid>

               
                        </Grid>
                    </Box>
                </Fade>
            </Modal>
        </div>
    )
}

export const ConfirmPassword = (props) => {

    const [isChangePasswordOpen] = React.useState(false);
    const [error,setError] = React.useState({
        Password: false,
        PasswordMessage: ""
    })
    const [password,setPassword] = React.useState("")


    const handleClose = () => props.setCreateModal(false);

    // Function to handle form submission for 
    const handleSubmitCreate = async (event) => {
        event.preventDefault();
        try {

            await Password_validation.validate({ password: password }, { abortEarly: false });
     
            reauthentication(password)
            .then(data=>{
                setError(data)
                setUserStatus(props.data.id,props.data.status)
            })
            .catch(error=>setError(error))

        } catch (validationError) {

            // Extract specific error messages for email and password
            const passwordError = validationError.inner.find((error) => error.path === 'password');
  

            // If validation errors occur
            setError({
                Password: !!passwordError,
                PasswordMessage: passwordError && passwordError.message
            });

        }
    };


    return (
        <div>  
            <Modal
            open={props.createModal}
            onClose={handleClose}
            closeAfterTransition
            slots={{ backdrop: Backdrop }}
            slotProps={{
                backdrop: {
                timeout: 500,
            },
            }}>
                <Fade in={props.createModal}>
                    <Box sx={style}>

                        <Typography variant='h5' color="#0F2C3D" fontWeight="BOLD" fontSize="1rem">
                        please type your password before to proceed
                        </Typography>

                        <Grid container spacing={1} padding={2}
                        direction="row"
                        justifyContent="center"
                        alignItems="center">

                            <Grid item xs={12}>
                                <DesktopTextbox fullWidth             
                                id="password"
                                name="password"
                                placeholder='enter your password'
                                value={password}
                                onChange={e=>setPassword(e.target.value)}
                                type={isChangePasswordOpen ? "text" : "password"}
                                error={error.Password}
                                helperText={error.PasswordMessage}
                                />
                            </Grid>

                            <Grid item xs={6}>
                                <Button fullWidth 
                                onClick={handleSubmitCreate}
                                color="error"
                                variant="contained">Confirm</Button>
                            </Grid>
                            <Grid item xs={6}>
                                <Button fullWidth 
                                onClick={handleClose}
                                // color="warning"
                                variant="contained">cancel</Button>
                            </Grid>



                        </Grid>
                    </Box>
                </Fade>
            </Modal>
        </div>
    )
}