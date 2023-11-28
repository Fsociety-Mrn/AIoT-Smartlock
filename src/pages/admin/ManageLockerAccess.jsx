import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import { 
  Accordion, 
  AccordionDetails, 
  AccordionSummary, 
  FormControl, 
  MenuItem, 
  Select, 
  Typography,
  InputLabel,
  Stack,
  IconButton 
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import FormatName from '../../Components/FormatName'; 


import { Avatar, Grid } from '@mui/material';

// data
import { userData } from '../../firebase/Firestore'
import dummdata from './dummyData.json'; 

import SettingsIcon from '@mui/icons-material/Settings';


//  user cards
const Card = ({ imgSrc, title, user, isActive, LockerNumber  }) => {

  const [open, setOpen] = useState(false);
  const [expanded, setExpanded] = useState('');
 
  const handleClickOpen = () => {
    setOpen(true);
  };
  
  const handleClose = () => {
    setOpen(false);
  };
  

  return (
    
    <StyledCard>

      <Stack
      direction="row"
      justifyContent="space-between"
      alignItems="center"
      spacing={0}> 

        {isActive ? (
        <div>
          <StatusDot status="green" />
          <span>Active</span>
        </div>
        ) : (
          <div>
            <StatusDot status="red" />
            <span>Inactive</span>
          </div>
        )}

        <IconButton color='primary' onClick={()=>console.log(dummdata[user])}>
          <SettingsIcon />
        </IconButton>
      </Stack>
   
      <Stack
      direction="column"
      justifyContent="center"
      alignItems="center"
      spacing={2}
      >

        <Avatar
        alt={title}
        src={imgSrc}
        sx={{ width: 150, height: 150, border: "2px solid rgb(61, 152, 154)" }}
        >A</Avatar>

        <Stack
        direction="column"
        justifyContent="center"
        alignItems="center"
        spacing={0}> 

          <Typography 
          variant='h5' 
          color="#0F2C3D" 
          fontWeight="bold" 
          fontSize="1rem">
            {user}
          </Typography>

          <Typography 
          variant='h5' 
          color="#0F2C3D" 
          fontWeight="lighter" 
          fontSize="0.9rem">
            Locker Number: <strong>{LockerNumber}</strong>
          </Typography>

          <Button onClick={handleClickOpen}>Details</Button>
        </Stack>

      </Stack>

      {/* when user is clicked details */}
      <Dialog open={open} onClose={handleClose}
        PaperProps={{
          style: {
            minWidth: 400, // Adjust the minimum width as needed
            width: '50%', // Adjust the width as needed
          },
        }}
       >
        <DialogTitle color="#0F2C3D">{user}</DialogTitle>

        <DialogContent>
          <DialogContentText color="#0F2C3D">Locker Number: {LockerNumber}</DialogContentText>

          <br/>
      
          <div>
            <h2>History Access:</h2>
              {dummdata[user] &&
                Object.keys(dummdata[user]).map((date, index) => (

                  <Accordion key={index} expanded={expanded === date} onChange={() => setExpanded(expanded === date ? '' : date)}>
                    <AccordionSummary expandIcon={<ExpandMoreIcon />} aria-controls={`panel${index}bh-content`} id={`panel${index}bh-header`}>
                      <Typography>{date}</Typography>
                    </AccordionSummary>

                    <AccordionDetails>

                      <div>
                        {Object.keys(dummdata[user][date]).map((time, idx) => (
                          <div key={idx}>
                            <p>Time: {time}</p>
                            <p>Access Type: {dummdata[user][date][time].Access_type}</p>

                            {dummdata[user][date][time].Percentage && (
                              <p>Percentage: {dummdata[user][date][time].Percentage}</p>
                            )}
                            <hr />
                          </div>
                        ))}
                      </div>
                    </AccordionDetails>

                  </Accordion>
              ))}
          </div>
        </DialogContent>

        <DialogActions>
          <Button onClick={handleClose}>Close</Button>
        </DialogActions>

      </Dialog>

    </StyledCard>
  );
};

const StyledCard = styled.div`
  background-color: #f2f2f2;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  width: 250px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
`;


const StatusDot = styled.div`
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 5px;
  background-color: ${props => (props.status === 'green' ? 'green' : 'red')};
  display: inline-block;
`;

const ManageLockerAccess = () => {

  // get windows screen
  const [state, setState] = React.useState(true);

    React.useEffect(()=>{
      const setResponsiveness = () => {
        return window.innerWidth < 800 ? setState(true) : setState(false);
      };
      
      setResponsiveness();
      window.addEventListener("resize", () => setResponsiveness());
      return () => {
        window.removeEventListener("resize", () => setResponsiveness());
      };
    },[])

  return (
    <div>
      {state ? <MobileView size={20} /> : <DesktopView />}
    </div>
  )
}

// Desktopview
const DesktopView = ()=>{
  return (
    <div>
      <Grid
      container
      direction="column"
      justifyContent="center"
      alignItems="center"
      paddingLeft={12}
      >
        <MobileView />
      </Grid>
    </div>
  );
}

// Mobile View
const MobileView = (props) => {

  // for data user
  const [dataUser, setDataUser] = React.useState([])
  const [token, setToken] = useState();
  const [expiration, setExpiration] = useState(0);
  const [selectedLocker, setSelectedLocker] = useState(''); // State for selected locker

  React.useEffect(() => {
   let isMounted = true;
    // fetch the user List
    const fetchData = async () => {
      try {

       const data = await userData();

        if (isMounted) {
        data.forEach((item) => {
          setDataUser((prevData) => {
            // Check if the item already exists in the dataUser state
            if (!prevData.some((dataItem) => dataItem.id === item.id)) {
              return [...prevData, item]; // Add the item if it doesn't exist
            }
            return prevData; // Return the existing state if the item already exists
          });
        });
  
        }
      } catch (error) {
        console.error(error);
      }
    };
      fetchData();


   return () => {
     isMounted = false;
   };

  }, [dataUser]);

 // Function to handle the selection of the locker
 const handleLockerSelection = (event) => {
  setSelectedLocker(event.target.value);
};

 // Function to generate OTP for the user
 const generateToken = () => {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'; // Define the set of characters to choose from
  let generatedToken = '';
  const tokenLength = 4; // Set the desired token length

  for (let i = 0; i < tokenLength; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      generatedToken += characters[randomIndex];
  }

  const expirationTime = 60; // Set the expiration time
  setToken(generatedToken);
  setExpiration(expirationTime);

  // Store token and expiration in local storage
  const expirationMilliseconds = Date.now() + expirationTime * 1000;
  localStorage.setItem('token', generatedToken);
  localStorage.setItem('expiration', expirationMilliseconds); // Store expiration time in milliseconds
};



useEffect(() => {
  let storedToken = localStorage.getItem('token');
  let storedExpiration = localStorage.getItem('expiration');

  if (storedToken && storedExpiration) {
    storedExpiration = parseInt(storedExpiration);
    const remainingTime = storedExpiration - Date.now(); // Calculate the remaining time

    if (remainingTime > 0) {
      setToken(storedToken);
      setExpiration(Math.floor(remainingTime / 1000)); // Convert milliseconds to seconds
    } else {
      // Clear token and expiration from local storage if the token has expired
      localStorage.removeItem('token');
      localStorage.removeItem('expiration');
      setToken(''); // Reset token when expiration reaches 0
      setExpiration(0); // Reset expiration when expiration reaches 0
    }
  }
}, [token]);

// State for token expiration time

useEffect(() => {
  let interval;
  if (expiration > 0) {
    interval = setInterval(() => {
      setExpiration((prev) => prev - 1); // Decrease expiration time by 1 second
    }, 1000);
  } else {
    setToken(''); // Reset token when expiration reaches 0
  }

  return () => clearInterval(interval); // Clear interval on component unmount
}, [expiration]);


  return(

    <Grid
    container
    direction="row"
    justifyContent="center"
    alignItems="center"
    paddingTop={props.size}
    spacing={1}
    style={{ 
        minHeight: "100vh",
      }}
    >
    
      {/* Person List */}
      {dataUser.map((person, index) => (
        <Grid item key={index} xl={3} md={3} sm={4}>
          <Card
          key={index}
          imgSrc={person.photoUrl}
          user={FormatName(person.user)}
          LockerNumber={person.LockerNumber}
          isActive={person.isActive}
          />
        </Grid>
      ))}



    </Grid>

  )
}



export default ManageLockerAccess
