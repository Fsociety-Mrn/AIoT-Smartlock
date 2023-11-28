import { 
    Box,
    Button, 
    Grid, 
    IconButton, 
    Modal, 
    Stack, 
    Typography } from '@mui/material';
import Table from './Table';
import React from 'react'

import KeyOutlinedIcon from '@mui/icons-material/KeyOutlined';
import CloseIcon from '@mui/icons-material/Close';
import { generateToken } from '../firebase/Realtime_Db';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: "100%",
    bgcolor: 'background.paper',
    // border: '2px solid #000',
    boxShadow: 24,
    borderRadius: "10px",
    p: 4
};

const columns = [
    { field: 'OTP', headerName: 'OTP', width: 150 },
    { field: 'DATE', headerName: 'DATE', width: 120 },
    { field: 'TIME', headerName: 'TIME', width: 100 },
  ];

const rows = [
    { 
      id: 1,
      OTP: 'ABC123', 
      DATE: 'Nov 23 2023', 
      TIME: "9:40 AM"
    },
    { 
        id: 2,
        OTP: 'ABC123', 
        DATE: 'Nov 23 2023', 
        TIME: "9:40 AM"
    },
    { 
        id: 3,
        OTP: 'ABC123', 
        DATE: 'Nov 23 2023', 
        TIME: "9:40 AM"
    },
    { 
        id: 4,
        OTP: 'ABC123', 
        DATE: 'Nov 23 2023', 
        TIME: "9:40 AM"
    },
    { 
        id: 5,
        OTP: 'ABC123', 
        DATE: 'Nov 23 2023', 
        TIME: "9:40 AM"
    },
];

const GenerateTokenModal = (props) => {
    const handleClose = () => props.setOpen(false);
    return (
        <div>
            <Modal
            open={props.open}
            onClose={handleClose}
            >

                <Box sx={style}>

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
                        One-Time Password (OTP)
                        </Typography>

                        <Grid
                        container
                        direction="row"
                        justifyContent="center"
                        alignItems="center"
                        spacing={2}
                        >

                            <Grid item xs={12}>
                                <Table 
                                value={0}
                                set={0}
                                rows={rows}
                                columns={columns}
                                />

                            </Grid>

                            <Grid item xs={12} md={3} sm={6}>
                                <Button 
                                fullWidth
                                variant='contained'
                                startIcon={<KeyOutlinedIcon fontSize='large'/>}
                                style={{ borderRadius: "10px", padding: "8px" }}
                                onClick={()=>generateToken()}
                                >Generate Token</Button>
                            </Grid>
                        </Grid>

                    </Stack>
  
                </Box>
            </Modal>
        </div>
    )
}

export default GenerateTokenModal