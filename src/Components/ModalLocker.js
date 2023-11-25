import { 
    Backdrop, 
    Box, 
    Fade, 
    Modal, 
    Typography,
    Button,
    Grid
 } from '@mui/material';
import React from 'react'


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


const ModalLocker = (props) => {

    const LockerNumber = ['20', '21'] 

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

                        <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">
                        choose the locker number or leave it behind
                        </Typography>

                        <Grid container spacing={1} padding={2}>
                            {LockerNumber.map((number) => (
                                <Grid item xs={3} key={number}> 
                                    <Button
                                    variant={props.LockerNumber === number ? 'contained' : 'outlined'}
                                    style={{
                                        width: '50px', // Adjust the width as needed
                                        height: '50px', // Adjust the height as needed
                                        fontSize: '16px', // Adjust the font size as needed
                                    }}
                                    >
                                        {number}
                                    </Button>
                                </Grid>
                            ))}
                        </Grid>
                    </Box>
                </Fade>
      </Modal>
    </div>
    )
}

export default ModalLocker