import { 
  Card,
  Grid, 
  Typography,
  Button,
  Avatar,
  Stack,
  IconButton
} from '@mui/material';
import React from 'react';

import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import LockOpenOutlinedIcon from '@mui/icons-material/LockOpenOutlined';

import { getUserDetails } from '../../firebase/Firestore'
import { statusLogin } from '../../firebase/FirebaseConfig'
import { 
  checkPin, 
  openLocker, 
  pushToken, 
  removeToken 
} from '../../firebase/Realtime_Db';

import FormatName from '../../Components/FormatName'
import ModalLocker from '../../Components/Modal/ModalLocker';
import { CreatePassword,ChangePassword } from '../../Components/Modal/PasswordModal'; 

import TokenGenerator from '../../Components/TokenGenerator'

const MyLocker = () => {
  const [paddinSize, setPaddingSize] = React.useState()

  const [userDetails, setUserDetaisl] = React.useState({
    uid: "",
    profilePicture: "",
    Name: "",
    LockerNumber: ""
  })
  const [sliderValue, setSliderValue] = React.useState(false); 
  const [openModal,setOpenModal] = React.useState(false)
  const [createModal,setCreateModal] = React.useState(false)
  const [changeModal,setChangeModal] = React.useState(false)

  const [checkPIN, setCheckPIN] = React.useState(false);

  // State for the Update Faces
  const [Token,setToken] = React.useState()
  const [isDisable,setIsdisable] = React.useState(false)
  const [Timer,setTimer] = React.useState()

  //  check pin  
  const checkpin = async (Name) => {
    const pinStatus = await checkPin(Name)
    setCheckPIN(pinStatus)
  }


  React.useEffect(()=>{
    const setResponsiveness = () => {
        return window.innerWidth < 700 ? setPaddingSize(15) : setPaddingSize(0);
    };

    // Set openModal to false after 3 seconds
    const timeoutId = setTimeout(() => {
      setSliderValue(false);
    }, 2000);


 

  // 30 SECONDS COUNTDOWN
  let countdown;
  if (isDisable && Timer > 0) {
    countdown = setInterval(() => {
      setTimer((prev) => prev - 1);
    }, 1000);
  } else {
    removeToken(userDetails.Name)
      clearInterval(countdown);
      setTimer(0);
      setIsdisable(false);
 
  }
    

    setResponsiveness();



    window.addEventListener("resize", () => setResponsiveness());
    return () => {

        window.removeEventListener("resize", () => setResponsiveness());
        clearTimeout(timeoutId);
        clearInterval(countdown);
    };
  },[sliderValue,Timer, isDisable])

  React.useEffect(()=>{

    let isMounted = true;


  // make this one time call
    statusLogin().then(uid=>{

      if (isMounted){
        getUserDetails(uid.uid).then(data=>{

          const name = FormatName(data.user)


  
          checkpin(name);

          setUserDetaisl({
            uid: uid.uid,
            profilePicture: data.photoUrl,
            Name: name,
            LockerNumber: data.LockerNumber
          })
  
        })
      }
  
    })
   
    // Cleanup function
    return () => {
      // Set the isMounted variable to false when the component unmounts
      isMounted = false;
      // Perform any cleanup here if needed
    };

  },[])



  // To OPEN THE LOCKER
  const handleClick = () => {
    setSliderValue(!sliderValue)

    openLocker({
      FullName: userDetails.Name,
      value: !sliderValue,
      number: userDetails.LockerNumber
    })

  };

  // handle to generate Token for faces
  const handleToken = e => {

      e.preventDefault()
      const tokenCode = TokenGenerator()
  
      setToken(tokenCode)
      setIsdisable(true)
      setTimer(30)
  
      pushToken({ FullName: userDetails.Name, Code: tokenCode })
  
    }


  return (
    <div 
    style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: "100vh" }} 
    >

      <ModalLocker 
      open={openModal} 
      setOpen={setOpenModal} 
      LockerNumber={userDetails.LockerNumber}
      UID={userDetails.uid}
      FullName={userDetails.Name} 
      />

      <CreatePassword 
      createModal={createModal} 
      setCreateModal={setCreateModal} 
      FullName={userDetails.Name} 
      LockerNumber={userDetails.LockerNumber}
      />

      <ChangePassword 
      createModal={changeModal} 
      setCreateModal={setChangeModal} 
      FullName={userDetails.Name} 
      LockerNumber={userDetails.LockerNumber}
      />

      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      marginTop={paddinSize}
      spacing={2}
      padding={2}
      >
        {/* <Grid item xs={10}>
          <Typography variant='h4' >My locker</Typography>
        </Grid> */}

        <Grid item xs={12} md={4}>
          <Card
          sx={{
            backgroundColor: "white",
            borderRadius: "20px",
            padding: "20px",
            margin: "10px"
          }}>
            
            <Stack
            direction="column"
            justifyContent="center"
            alignItems="center"
            spacing={1}>
            
              <Avatar 
              sx={{ width: '100px', height: '100px', border: '2px solid rgb(61, 152, 154)' }}
              src={userDetails.profilePicture}
              >
                A
              </Avatar>

              <Stack
              direction="column"
              justifyContent="center"
              alignItems="center"
              spacing={0}>
                <Typography variant='h5' color="#0F2C3D" fontWeight="bold" fontSize="1.3rem">{userDetails.Name}</Typography>
                <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">Your Locker Number: <strong>{userDetails.LockerNumber}</strong></Typography>
              </Stack>

              {/* For Open the Locker */}
              <Button onClick={()=>setOpenModal(!openModal)}>  Change your Locker Number </Button>

              {/* For Face OTP */}
              {isDisable && 
              <Typography variant='h6' color="#c71e1e" fontWeight="bold" fontSize="1rem">
                <strong>{Token}</strong>
              </Typography>}
              {isDisable &&
              <Typography variant='h6' color="#0F2C3D" fontWeight="bold" fontSize="0.9rem">
                this is your OTP code and it expires at <strong> {Timer} </strong>
              </Typography>}

              <Button 
              variant='contained' 
              fullWidth
              disabled={isDisable}
              onClick={handleToken}
              >Generate face update OTP</Button>

              {/* Change Locker PiIN */}
              {checkPIN ?      
                <Button variant='contained' color="error" fullWidth onClick={()=> setCreateModal(!createModal)}>Create your PIN </Button>
                : 
                <Button variant='contained' fullWidth onClick={()=> setChangeModal(!changeModal)}>change locker pin</Button>
              }

            </Stack>

          </Card>
        </Grid>

        <Grid item xs={12} md={5}>
          <Card
          sx={{
            backgroundColor: "white",
            borderRadius: "20px",
            textAlign: "center", // Center the content
            alignItems: "center",
            padding: "40px",
            margin: "10px"
          }}>
            <Stack
            direction="column"
            justifyContent="center"
            alignItems="center"
            spacing={1}>

              <Typography variant='h5' color="#0F2C3D" fontWeight="bold" fontSize="1.3rem">
                Your locker is { !sliderValue ? "close" : "open"}
              </Typography>  

              <IconButton size="large" onClick={handleClick} color='primary' >
                {!sliderValue ? <LockOutlinedIcon fontSize='large'   style={{ fontSize: 100 }} /> 
                : <LockOpenOutlinedIcon fontSize='large'   style={{ fontSize: 100 }} />}
              </IconButton>

              <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">click to open your locker</Typography>
              
            </Stack>
          </Card>
        </Grid>



      </Grid>
    </div>
  );
};

export default MyLocker;
