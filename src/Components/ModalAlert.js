import React from 'react'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { Button } from 'react-scroll';
import { Stack } from '@mui/material';
import TokenGenerator from './TokenGenerator';
import { AIoT_unlock, get_AIoT_unlock } from '../firebase/Realtime_Db'; 

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

const ModalAlert = (props) => {

    const [token,setToken] = React.useState({
        token: "",
        expiration: ""
    })


    const handleClose = () => props.setOpen(false);

    const createToken = () => {
        
        const Token = TokenGenerator()
        // Get the current date and time
        const currentDate = new Date();

        // Add 30 minutes to the current time
        const newDate = new Date(currentDate.getTime() + 30 * 60000); // 30 minutes in milliseconds

        const dateOptions = {
          month: 'short',
          day: 'numeric',
          year: 'numeric',
        };
  
        const timeOptions = {
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: true,
          };

        const formattedDate = String(currentDate.toLocaleString('en-US', dateOptions)).replace(",", "");
        const formattedTime = newDate.toLocaleString('en-US', timeOptions);

        AIoT_unlock({
            token: Token,
            expiration: {
                date: formattedDate,
                time: formattedTime
            }
        }).then(e=>{

            // Update state with formatted date and time
            setToken({
                token: Token,
                expiration: {
                    date: formattedDate,
                    time: formattedTime
                }
            })
        })

    }

    React.useEffect(()=>{
            // check if AIoT Smartlock is Lock
    get_AIoT_unlock().then(data=>{
        data.data && setToken(data.data)
  
      })
    },[])
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

                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        Generate token to unlock locker
                    </Typography>

                    {token.token !== "" &&
                        <>
                            <Typography variant='h5' color="#0F2C3D" fontWeight="bold" fontSize="1.3rem">
                                <strong>{token.token}</strong>
                            </Typography>

                            <Typography fontWeight="lighter" fontSize="0.9rem">
                                this token expire at {token.expiration.time}
                            </Typography>
                        </>
                    }
                    <Button
                    fullWidth
                    variant="contained"
                    color="" // You can adjust the color based on your design
                    style={{
                        borderRadius: '10px', // Add rounded corners for a modern look
                    }}
                    onClick={createToken}
               
                    >
                        generate Token
                    </Button>

                </Stack>
  
            </Box>
        </Modal>
    </div>
  )
}

export default ModalAlert