import React, { useState } from 'react';
import styled from 'styled-components';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import PersonList from './Datas' ; // Import the PersonList data from the new file


const Card = ({ imgSrc, title, description, user, LockerNumber, isActive }) => {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <StyledCard>
      {isActive === 'active' && <StatusDot status="green" />}
      {isActive === 'inactive' && <StatusDot status="red" />}
      <CardImage src={imgSrc} alt={title} />
      <CardContent>
        <h4>{user}</h4>
        <BtnGroup>
          <Button onClick={handleClickOpen}>Details</Button>
        </BtnGroup>
      </CardContent>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>{user}</DialogTitle>
        <DialogContent>
          <DialogContentText>{LockerNumber}</DialogContentText>
          <CardImage src={imgSrc} alt={title} />
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

const CardImage = styled.img`
  max-width: 100%;
`;

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
  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', // Adjust columns and minimum width
        gap: '20px', // Space between cards
        justifyContent: 'flex-start', // Move cards to the left
        alignItems: 'flex-start', // Align cards at the top
        padding: '100px 20px', // Add padding to move content down and left
        minHeight: '100vh',
        paddingLeft: '100px', // Adjust this value based on your side app bar's width
      }}
    >
      {PersonList.map((person, index) => (
        <Card
          key={index}
          imgSrc={person.photoURL}
          user={person.user}
          LockerNumber={person.LockerNumber}
          isActive={person.isActive}
        />
      ))}
    </div>
  );
};

export default homepage;
