import { Backdrop, Box, Fade, Grid, Modal, Stack, Typography,Button } from '@mui/material';
import React from 'react'
import { DesktopTextbox } from '../Textfield';
import { Password_validation } from "../../Authentication/Validation";
import { reauthentication } from "../../firebase/FirebaseConfig";

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    bgcolor: 'background.paper',
    width: "400px",
    boxShadow: 24,
    borderRadius: "10px",
    p: 4
};


const ModalConfirm = (props) => {   

    const [isChangePasswordOpen] = React.useState(false);
    const [error,setError] = React.useState({
        Password: false,
        PasswordMessage: ""
    })
    const [password,setPassword] = React.useState("")
    
    const handleClose = () => props.setOpen(false);


    // Function to handle form submission for 
    const handleSubmitCreate = async (event) => {
        event.preventDefault();
        try {

            await Password_validation.validate({ password: password }, { abortEarly: false });
     
            reauthentication(password)
            .then(data=>{
                setError(data)
                props.delete()
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
            open={props.open}
            onClose={handleClose}
            closeAfterTransition
            slots={{ backdrop: Backdrop }}
            slotProps={{
                backdrop: {
                timeout: 500,
            },
            }}>
            <Fade in={props.open}>
                <Box sx={style}>


                    <Grid container spacing={1}>
                    
                        <Grid item xs={12}>
                            <Stack
                            direction="column"
                            justifyContent="center"
                            alignItems="center"
                            spacing={0}
                            paddingTop={2}
                            >
                                <Typography variant='h5' color="#0F2C3D" fontWeight="lightweight" fontSize="1rem">
                                Are you sure you want to remove
                                </Typography>
                                <Typography variant='h5' color="#0F2C3D" fontWeight="lightweight" fontSize="1rem">
                                {props.name} ?
                                </Typography>
                            </Stack>
                        </Grid>

                        <Grid item xs={12}>
                            <DesktopTextbox fullWidth             
                            id="password"
                            name="password"
                            placeholder='enter your password first'
                            value={password}
                            onChange={e=>setPassword(e.target.value)}
                            type={isChangePasswordOpen ? "text" : "password"}
                            error={error.Password}
                            helperText={error.PasswordMessage}
                            />
                        </Grid>

                        <Grid item xs={12}>
                            <Stack
                            direction="row"
                            justifyContent="center"
                            alignItems="center"
                            spacing={2}
                            paddingTop={2}
                            >
                                <Button variant='contained' color='error' onClick={handleSubmitCreate}>Yes</Button>
                                <Button variant='outlined' onClick={handleClose}>No</Button>
                            </Stack>
                            
                        </Grid>
                    </Grid>
                </Box>
            </Fade>
            </Modal>
        </div>
    )
}

export default ModalConfirm