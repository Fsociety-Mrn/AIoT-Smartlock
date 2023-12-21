import { 
    Accordion,
    AccordionSummary,
    AccordionDetails,
    Box,
    Button, 
    Grid, 
    IconButton, 
    MenuItem, 
    Modal, 
    Stack, 
    TextField, 
    Typography } from '@mui/material';
// import Table from '../Table';
import React from 'react'

import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import KeyOutlinedIcon from '@mui/icons-material/KeyOutlined';
import CloseIcon from '@mui/icons-material/Close';
import { generateToken } from '../../firebase/Realtime_Db';

// const columns = [
//     { field: 'OTP', headerName: 'OTP', width: 150 },
//     { field: 'LOCKERNUMBER', headerName: 'LOCKER', width: 80 },
//     { field: 'TIME', headerName: 'EXPIRED TIME', width: 120 },
//     { field: 'DATE', headerName: 'EXPIRED DATE', width: 120 },
//   ];


// const rows = [
//     { 
//       id: 1,
//       OTP: 'ABC123', 
//       DATE: 'Nov 23 2023', 
//       TIME: "9:40 AM"
//     },
//     { 
//         id: 2,
//         OTP: 'ABC123', 
//         DATE: 'Nov 23 2023', 
//         TIME: "9:40 AM"
//     },
//     { 
//         id: 3,
//         OTP: 'ABC123', 
//         DATE: 'Nov 23 2023', 
//         TIME: "9:40 AM"
//     },
//     { 
//         id: 4,
//         OTP: 'ABC123', 
//         DATE: 'Nov 23 2023', 
//         TIME: "9:40 AM"
//     },
//     { 
//         id: 5,
//         OTP: 'ABC123', 
//         DATE: 'Nov 23 2023', 
//         TIME: "9:40 AM"
//     },
// ];

const ChildModal = (props) => {
    return(
        <div>
            <Modal
            open={props.open}
            onClose={props.handleClose}
            >
                <Box 
                sx={
                    {
                    position: 'absolute',
                    top: '50%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    width: "300px",
                    bgcolor: 'background.paper',
                    boxShadow: 24,
                    borderRadius: "10px",
                    p: 4
                    }
                }>

                    <Stack
                    direction="column"
                    justifyContent="center"
                    alignItems="center"
                    spacing={1}>



                        <Typography id="modal-modal-title" variant='h5' color="red" fontWeight="BOLD" fontSize="1.2rem"> 
                            "{props.OTP}"
                        </Typography>

                        <Typography  variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem"> 
                        <span role="img" />🎉 One-Time Password (OTP) for signing up has been generated! 🚀 
                        </Typography>
                        
                        <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem"> 
                        and will expire in 3 hours.
                        </Typography>

                    </Stack>
                </Box>
            </Modal>
    </div>
    )
}
const GenerateTokenModal = (props) => {

    const handleClose = () => {
        props.setOpen(false)
        setOpen(false)
    };

    const [open,setOpen] = React.useState()
    const [otp,setOtp] = React.useState()


    const [expanded, setExpanded] = React.useState('');


    const currencies = [
        { value: 21, label: 21 },
        { value: 20, label: 20 },
        { value: 16, label: 16 },
        { value: 12, label: 12 },
        { value: 7, label: 7 },
        { value: 8, label: 8 }
        // Add more currencies as needed
      ];
    
    // const [selectedCurrency, setSelectedCurrency] = React.useState('');
    // const [setToks,toks] = React.useState(true);
    
    // const handleCurrencyChange = (event) => {
    //     setSelectedCurrency(event.target.value);
    //     setToks(false);
    // };

    const [selectedCurrency, setSelectedCurrency] = React.useState('');
    const [toks, setToks] = React.useState(true);

    const handleCurrencyChange = (event) => {
        setSelectedCurrency(event.target.value);
        setToks(false);
    };


    
    return ( 
        <div>

            <ChildModal 
            open={open}
            handleClose={handleClose}
            OTP={otp}
            />

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

                                {props.tokenList ?
                                    <div>
                                {
                                    Object.values(props.tokenList)
                                    .map((data,key) => (
                                        <Accordion key={key} expanded={expanded === data.DATE} onChange={() => setExpanded(expanded === data.DATE ? '' : data.DATE)}>
                                            <AccordionSummary expandIcon={<ExpandMoreIcon />} aria-controls={`panel${key}bh-content`} id={`panel${key}bh-header`}>
                                                <Typography> <strong>{data.OTP} </strong> </Typography>
                                            </AccordionSummary>

                                            <AccordionDetails>
                                                <div>
                                                    <p>LOCKER NUMBER: <strong>{data.LOCKERNUMBER}</strong></p>
                                                    <p>EXPIRED DATE: <strong>{data.DATE}</strong></p>
                                                    <p>EXPIRED TIME: <strong>{data.TIME}</strong></p>
                                                </div>
                                            </AccordionDetails>
                                        </Accordion>
                                    ))
                                }
                                </div>
                                :
                                <Stack
                                direction="column"
                                justifyContent="center"
                                alignItems="center"
                                >
                                    <Typography>no token available</Typography>
                                </Stack>
                                }

                            </Grid>

                            <Grid item xs={12} md={10} sm={10}>

                                <Stack
                                direction="column"
                                justifyContent="center"
                                alignItems="center"
                                >

                                    <TextField
                                select
                                label="Locker Number"        
                                helperText="Pick locker number, generate token"
                                variant="outlined"
                                value={selectedCurrency}
                                onChange={handleCurrencyChange}
                                >
                                    {currencies.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                    </TextField>
                                
                                    <Button 
                                fullWidth
                                disabled={toks}
                                variant='contained'
                                startIcon={<KeyOutlinedIcon fontSize='large'/>}
                                style={{ borderRadius: "10px", padding: "8px" }}
                                onClick={()=>{
                                    generateToken(selectedCurrency)
                                    .then(otp=>{
                                        setOtp(otp)
                                        setOpen(!open)
                                        setToks(true)
                                        setSelectedCurrency('')
                                    })
                                    // handleClose()
                                    
                                }}
                                    >Generate Token</Button>
                                    
                                </Stack>
                            </Grid>
                          
                        </Grid>

                    </Stack>
  
                </Box>
            </Modal>
        </div>
    )
}

export default GenerateTokenModal