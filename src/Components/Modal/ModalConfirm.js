import { Backdrop, Box, Fade, Grid, Modal, Stack, Typography,Button } from '@mui/material';
import React from 'react'


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
    
    const handleClose = () => props.setOpen(false);

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
                            <Stack
                            direction="row"
                            justifyContent="center"
                            alignItems="center"
                            spacing={2}
                            paddingTop={2}
                            >
                                <Button variant='contained' color='error' onClick={props.delete}>Yes</Button>
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