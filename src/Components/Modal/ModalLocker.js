import { 
    Backdrop, 
    Box, 
    Fade, 
    Modal, 
    Typography,
    Button,
    Grid,
    Stack
 } from '@mui/material';
import { updateLocker } from '../../firebase/Firestore';
import { changeLockerNumber } from '../../firebase/Realtime_Db';
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
    const [selectedLocker, setSelectedLocker] = React.useState(null);

    const handleButtonClick = (number) => {
      setSelectedLocker(number === selectedLocker ? null : number);
    };


    const handleClose = () => props.setOpen(false);

    React.useEffect(() => {
        setSelectedLocker(props.LockerNumber);
    }, [props.LockerNumber]);
    
    const handleonsavechanges = async () => {
        updateLocker(props.UID, selectedLocker)
        await changeLockerNumber("LOCK",props.FullName,selectedLocker)
        // await changeLockerNumber("PIN",props.FullName,selectedLocker)
    }

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
                                <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="1rem">
                                This is your Locker Number: <strong> {selectedLocker} </strong>
                                </Typography>

                                <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">
                                choose the locker number or leave it behind
                                </Typography>
                            </Grid>

                            {LockerNumber.map((number) => (
                                <Grid item xs={3} key={number}> 
                                    <Button
                                    variant={selectedLocker === number ? 'contained' : 'outlined'}
                                    style={{
                                        width: '50px',
                                        height: '50px',
                                        fontSize: '16px',
                                    }}
                                    onClick={() => handleButtonClick(number)}
                                    >
                                        {number}
                                    </Button>
                                </Grid>
                            ))}

                            <Grid item xs={12}>
                                <Stack
                                direction="row"
                                justifyContent="center"
                                alignItems="center"
                                spacing={2}
                                paddingTop={2}
                                >
                                    <Button variant='contained' onClick={handleonsavechanges}>Save Changes</Button>
                                </Stack>
                                
                            </Grid>
                        </Grid>
                    </Box>
                </Fade>
            </Modal>
    </div>
    )
}

export default ModalLocker