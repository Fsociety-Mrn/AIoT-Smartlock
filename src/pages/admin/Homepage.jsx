import React, { useState } from 'react';
import styled from 'styled-components';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
// import PersonList from './Datas' ; // Import the PersonList data from the new file
import { Avatar, Grid } from '@mui/material';

// data
import { userData } from '../../firebase/Firestore'

//  user cards
const Card = ({ imgSrc, title, user, LockerNumber, isActive }) => {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <StyledCard>

      {isActive ? <StatusDot status="green" /> : <StatusDot status="red" />}


      {/* <CardImage src={imgSrc} alt={title} /> */}

      <Avatar
      alt={title}
      src={imgSrc}
      sx={{ width: 250, height: 250, border: "2px solid rgb(61, 152, 154)" }}
      >A</Avatar>

      <CardContent>
        <h4>{user}</h4>
        <BtnGroup>
          <Button onClick={handleClickOpen}>Details</Button>
        </BtnGroup>
      </CardContent>

      {/* when user is clicked details */}
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>{user}</DialogTitle>

        <DialogContent>
          <DialogContentText>{LockerNumber}</DialogContentText>

          <Avatar
          alt={title}
          src={imgSrc}
          sx={{ width: 250, height: 250, border: "2px solid rgb(61, 152, 154)" }}
          >A</Avatar>
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
  width: 300px;
  margin: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
`;

// const CardImage = styled.img`
//   max-width: 100%;
// `;

const CardContent = styled.div`
  margin-top: 10px;
`;

const BtnGroup = styled.div`
  height: 70px;
  display: flex;
  align-items: center;
`;

const StatusDot = styled.div`
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 5px;
  background-color: ${props => (props.status === 'green' ? 'green' : 'red')};
  display: inline-block;
`;

const homepage = () => {

      // get windows screen
  const [state, setState] = React.useState(true);
    React.useEffect(()=>{
      const setResponsiveness = () => {
        return window.innerWidth < 850 ? setState(true) : setState(false);
      };
      
      setResponsiveness();
      window.addEventListener("resize", () => setResponsiveness());
      return () => {
        window.removeEventListener("resize", () => setResponsiveness());
      };
    },[])

  return( 
    <div>
      {state ? <MobileView />  : <DesktopView />}
    </div>
  )
};

// Desktopview
const DesktopView = ()=>{

   // for data user
   const [dataUser, setDataUser] = React.useState([])

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
 
  
  
  return (
    <div>
      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      paddingLeft={12}
      paddingTop={10}>

        <Grid
        container
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={1}
        style={{ 
          minHeight: "100vh",
        }}>  

          {/* Person List  */}
          {dataUser.map((person, index) => (
            <Grid item key={index} xs={12} xl={4} md={4} sm={12}>

              <Card
              key={index}
              imgSrc={person.photoURL}
              user={person.user}
              LockerNumber={person.LockerNumber}
              isActive={person.isActive}/>

            </Grid>
          ))}


        </Grid>

      </Grid>
    </div>
  );
}

// Mobile View
const MobileView = () => {

   // for data user
   const [dataUser, setDataUser] = React.useState([])

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
 
  return(
    <div >
      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      paddingTop={20}
      // paddingRight={3}
      >

        {/* Person List  */}
        {dataUser.map((person, index) => (
          <Grid item key={index} md={12}>

            <Card
            key={index}
            imgSrc={person.photoURL}
            user={person.user}
            LockerNumber={person.LockerNumber}
            isActive={person.isActive}/>

          </Grid>
        ))}
      </Grid>
    </div>
  )
}
export default homepage;
