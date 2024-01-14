import React, { useState } from 'react';
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
  Typography,
  Stack,
  IconButton, 
  Menu,
  MenuItem,
  ListItemIcon,
  Divider,
  FormControlLabel,
  Switch
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import FormatName from '../../Components/FormatName'; 

import { Avatar, Grid } from '@mui/material';

import GenerateTokenModal from '../../Components/Modal/GenerateTokenModal'
import ModalConfirm from '../../Components/Modal/ModalConfirm';

// data
import { userData,promoteAdmin, deleteUser,setUserStatus,updateLocker } from '../../firebase/Firestore'
import { TokenList, getHistory, removeUser } from '../../firebase/Realtime_Db';

// Icons
import SettingsIcon from '@mui/icons-material/Settings';
import KeyOutlinedIcon from '@mui/icons-material/KeyOutlined';
import AdminPanelSettingsIcon from '@mui/icons-material/AdminPanelSettings';
import PersonRemoveIcon from '@mui/icons-material/PersonRemove';
import LockResetIcon from '@mui/icons-material/LockReset';
import ModalLocker from '../../Components/Modal/ModalLocker';
import PersonOffIcon from '@mui/icons-material/PersonOff';
import KeyIcon from '@mui/icons-material/Key';
import PersonIcon from '@mui/icons-material/Person';

//  user s
const Card = ({ imgSrc, title, user, isActive, LockerNumber, Data, isAdmin, id  }) => {

  const [open, setOpen] = useState(false);
  const [expanded, setExpanded] = useState('');
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [openModal,setOpenModal] = React.useState(false)
  const [changeLocker,setChangeLocker] = React.useState(false)

  const openS = Boolean(anchorEl);

  const handleClickOpen = () => {
    setOpen(true);
  };
  
  const handleClose = () => {
    setOpen(false);
  };

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleCloseD = () => {
    setAnchorEl(null);
  };

  const removeAccount = async () =>{
    await removeUser("HISTORY", user)
    await removeUser("LOCK", user)
    await removeUser("PIN", user)
    await deleteUser(id)

    window.location.reload()
  }

  const resetPIN = async () =>{
    await removeUser("PIN", user)
    window.location.reload()
  }

  const changeuserStatus = async () =>{
    await removeUser("LOCK", user)
    await removeUser("PIN", user)
    setUserStatus(id,!isActive);
  

  }

  return (

    
    <StyledCard>

      <ModalLocker 
      open={changeLocker} 
      setOpen={setChangeLocker} 
      LockerNumber={LockerNumber}
      UID={id}
      FullName={user} 
      />

      <ModalConfirm
      open={openModal}
      setOpen={setOpenModal}
      name={user}
      delete={removeAccount}
      />

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

        <IconButton color='primary' 
        id="basic-button"
        aria-controls={open ? 'basic-menu' : undefined}
        aria-haspopup="true"
        aria-expanded={open ? 'true' : undefined}
        onClick={handleClick}>
          <SettingsIcon />
        </IconButton>

        <Menu
        id="basic-menu"
        anchorEl={anchorEl}
        open={openS}
        onClose={handleCloseD}
        MenuListProps={{
          'aria-labelledby': 'basic-button',
        }}
        >
          {!isAdmin && isActive &&
          <MenuItem onClick={()=>promoteAdmin(id,user)}>
          
            <ListItemIcon>
              <AdminPanelSettingsIcon fontSize="medium" color="primary" />
            </ListItemIcon>

            Promote Admin
          </MenuItem>
          }

          {isActive &&
          <MenuItem onClick={()=>setChangeLocker(true)}>
            <ListItemIcon>
              <LockResetIcon fontSize="medium" color="primary"/>
            </ListItemIcon>

            Change Locker
          </MenuItem>}
          
          {isActive &&
          <MenuItem onClick={()=>resetPIN()}>
            <ListItemIcon>
              <KeyIcon fontSize="medium" color="primary"/>
            </ListItemIcon>
            Reset pin
          </MenuItem>}

          {isActive && <Divider /> }
          
          {isActive &&
          <MenuItem onClick={()=>setUserStatus(id,!isActive)}>
            <ListItemIcon>
              <PersonOffIcon fontSize="medium" color="primary"/>
            </ListItemIcon>
            Deactivate Account
          </MenuItem>}

          {!isActive &&
          <MenuItem onClick={changeuserStatus}>
            <ListItemIcon>
              <PersonIcon fontSize="medium" color="primary"/>
            </ListItemIcon>
            Activate Account
          </MenuItem>}

          <MenuItem onClick={changeuserStatus}>
            <ListItemIcon>
              <PersonRemoveIcon fontSize="medium" color='error'/>
            </ListItemIcon>

            Delete Account
          </MenuItem>

      </Menu>

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

          {isAdmin && 
            <Typography 
            variant='h5' 
            color="#0F2C3D" 
            fontWeight="bold" 
            fontSize="0.7rem">
              admin
            </Typography>
          }
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
              {Data && Data[user] ?
                Object.keys(Data[user]).map((date, index) => (

                  <Accordion key={index} expanded={expanded === date} onChange={() => setExpanded(expanded === date ? '' : date)}>
                    <AccordionSummary expandIcon={<ExpandMoreIcon />} aria-controls={`panel${index}bh-content`} id={`panel${index}bh-header`}>
                      <Typography>{date}</Typography>
                    </AccordionSummary>

                    <AccordionDetails>

                      <div>
                        {Object.keys(Data[user][date]).map((time, idx) => (
                          <div key={idx}>
                            <p>Time: {time}</p>
                            <p>Access Type: {Data[user][date][time].Access_type}</p>

                            {Data[user][date][time].Percentage && (
                              <p>Percentage: {Data[user][date][time].Percentage}</p>
                            )}
                            <hr />
                          </div>
                        ))}
                      </div>
                    </AccordionDetails>

                  </Accordion>
              ))
              :
              (
                <p>No access history available for the user {user}.</p>
              )}
              
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
      {state ? <MobileView size={20} jc="center" /> : <DesktopView />}
    </div>
  )
}

// Desktop view
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
        <MobileView size={2} jc="flex-start"/>
      </Grid>
    </div>
  );
}

// Mobile View
const MobileView = (props) => {

  // for data user
  const [dataUser, setDataUser] = React.useState([])
  const [Data,setData] = React.useState()
  const [openModal,setOpenModal] = React.useState(false)
  const [listTokens, setListTokesn] = React.useState("")
  const [checked, setChecked] = React.useState(true);

  const handleChangeSwitch = (event) => {
    setChecked(event.target.checked);
  };

  // Function to sort the data by date
  const sortDataByDate = (data) => {
    const sortedData = {};
  
    // Iterate over each user
    Object.keys(data).forEach((user) => {

      // console.log("NAME: ", user)

      // Sort the dates for each user
      const sortedDates = Object.keys(data[user]).sort((a, b) => new Date(b) - new Date(a))

      // console.log("SORTED: ",sortedDates)
  
      // Create a new object with sorted dates
      sortedData[user] = sortedDates.reduce((acc, date) => {
        acc[date] = data[user][date];
        return acc;
      }, {});
    });

    return sortedData;
  }

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


    // Get History List
    getHistory()
      .then(data=>
        {
          if (data){
            const sortedData = sortDataByDate(data)
            setData(sortedData)
       
          }
        })

   return () => {
     isMounted = false;
   };

  }, [dataUser]);

  return(
    <>
      <GenerateTokenModal 
      open={openModal} 
      setOpen={setOpenModal} 
      tokenList={listTokens}
      />

    <Grid
    container
    direction="row"
    justifyContent={props.jc}
    alignItems="center"
    paddingTop={props.size}
    spacing={1}
    style={{ 
      minHeight: "100vh",
    }}
    >

  

      <Grid item xs={7} md={3} sm={7}>


        
        <Stack
        direction="column"
        justifyContent="center"
        alignItems="center"
        spacing={2}
        >
     

        <Button variant='contained' fullWidth startIcon={<KeyOutlinedIcon fontSize='large'/>}
        style={{ borderRadius: "10px", padding: "8px" }}
        onClick={()=>{


        TokenList()
        .then(tokenList => {

          const formattedTokenList = tokenList.map((token, index) => {
            const expirationDate = new Date(`${token.EXPIRATION.date} ${token.EXPIRATION.time}`);
            return {
              id: index + 1, // Assuming you want 1-based index
              OTP: token.OTP,
              LOCKERNUMBER: token.LockerNumber,
              DATE: expirationDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
              TIME: expirationDate.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true }),
            };
          });

          setListTokesn(formattedTokenList); 
   
        })
        .catch(error => {
          console.error(error);
        });

        setOpenModal(!openModal);
        }}>Generate OTP </Button>

          <FormControlLabel
          value="end"
          control={<Switch color="primary" checked={checked} onChange={handleChangeSwitch}/>}
          label={checked ? "Active User" : "Inactive User"}
          labelPlacement="end"
          />

        </Stack>
      </Grid>

      

      <Grid item xs={12} sm={12} />



      {/* Person List */}
      {dataUser.filter(person => person.isActive === checked).map((person, index) => (
        
        <Grid item key={index} xl={3} md={3} sm={4}>

          <Card
          key={index}
          imgSrc={person.photoUrl}
          user={FormatName(person.user)}
          LockerNumber={person.LockerNumber}
          isActive={person.isActive}
          Data={Data}
          isAdmin={person.isAdmin}
          id={person.id}
          />

        </Grid>
      ))}



    </Grid>
   </>
  )
}
export default ManageLockerAccess
