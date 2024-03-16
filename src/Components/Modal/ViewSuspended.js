import { 
    Box,
    Grid, 
    IconButton, 
    Modal, 
    Stack, 
    Typography } from '@mui/material';
// import Table from '../Table';
import React from 'react'

import DeleteOutlineOutlinedIcon from '@mui/icons-material/DeleteOutlineOutlined';

import CloseIcon from '@mui/icons-material/Close';
import { updateSuspended } from '../../firebase/Realtime_Db';

const ViewSuspended = (props) => {

    const handleClose = () => {
        props.setOpen(false)
    };

    return ( 
        <div>

            <Modal
            open={props.open}
            onClose={handleClose}
            >
                <Box 
                sx={
                    {
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
                    }
                }>

                    <Stack
                    direction="column"
                    justifyContent="center"
                    alignItems="center"
                    spacing={2}>

                        <IconButton
                        edge="start"
                        size='large'
                        onClick={handleClose}
                        aria-label="close"
                        sx={{ position: 'absolute', top: '8px', right: '8px' }}
                        color="#0F2C3D"
                        >
                            <CloseIcon fontSize='large' />
                        </IconButton>

                        <Typography id="modal-modal-title" variant="h6" component="h2">
                            Suspended profile
                        </Typography>

                        <Grid
                        container
                        direction="row"
                        justifyContent="center"
                        alignItems="center"
                        spacing={1}
                        >

                            <Grid item xs={12}>

                            {props.data && Object.values(props.data).some(data => data.status) ? (
                                Object.values(props.data).map((data, index) => {
     
            return (
                <Stack
                    key={index}
                    direction="row"
                    justifyContent="center"
                    alignItems="center"
                >
                    <Typography>{data.personID}</Typography>
                    <IconButton onClick={() => updateSuspended(data.personID).then(data=>handleClose())}>
                        <DeleteOutlineOutlinedIcon color='error' />
                    </IconButton>
                </Stack>
            );
     
    })
) : (
    <Stack
                 
                    direction="row"
                    justifyContent="center"
                    alignItems="center"
                >
    <Typography>No suspended data</Typography>
    </Stack>
)}

                            </Grid>

                        </Grid>

                    </Stack>
  
                </Box>
            </Modal>
        </div>
    )
}

export default ViewSuspended