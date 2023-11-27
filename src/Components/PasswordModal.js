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
import { DesktopTextbox } from './Textfield';
import React from "react"
import { createPIN } from "../firebase/Realtime_Db";
import { pinSchema } from "../Authentication/Validation";

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

export const ChangePassword = (props) => {

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
            label="Show Password"
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
