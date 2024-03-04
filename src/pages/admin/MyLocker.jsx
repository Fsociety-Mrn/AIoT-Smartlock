import { 
  Card,
  Grid, 
  Typography,
  Button,
  Avatar,
  Stack,
  IconButton,
  Slider
} from '@mui/material';
import React from 'react';

import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import LockOpenOutlinedIcon from '@mui/icons-material/LockOpenOutlined';

import { getUserDetails } from '../../firebase/Firestore'
import { statusLogin } from '../../firebase/FirebaseConfig'
import { 
  checkPin, 
  getLockerSensor, 
  openLocker, 
  pushHistory, 
  pushToken, 
  removeToken 
} from '../../firebase/Realtime_Db';

import FormatName from '../../Components/FormatName'
import ModalLocker from '../../Components/Modal/ModalLocker';
import { CreatePassword,ChangePassword } from '../../Components/Modal/PasswordModal'; 

import TokenGenerator from '../../Components/TokenGenerator'

import { withStyles } from '@mui/styles';

const IOSUnlockSlider = withStyles((theme) => ({
  root: {
    color: theme.palette.primary.main,
    height: 6,
    padding: '13px 0',
  },
  thumb: {
    height: 30,
    width: 30,
    backgroundColor: '#ffff',
    border: '2px solid currentColor',
    marginTop: 0, // Adjusted to center the thumb vertically
    marginLeft: -15,
    // boxShadow: '#ebebeb 0px 2px 2px',
    // '&:focus, &:hover, &$active': {
    //   boxShadow: '#ccc 0px 2px 3px 1px',
    // },
    '& .bar': {
      height: 9,
      width: 1,
      backgroundColor: 'currentColor',
      marginLeft: 1,
      marginRight: 1,
    },
  },
  active: {},
  valueLabel: {
    left: 'calc(-50% + 4px)',
    top: -22,
    '& *': {
      background: 'transparent',
      color: '#000',
    },
  },
  track: {
    height: 30, // Adjust height of the track
    borderRadius: 15,
  },
  rail: {
    height: 30, // Adjust height of the track
    borderRadius: 15,
  },
}))(Slider);


const MyLocker = () => {

  const [paddinSize, setPaddingSize] = React.useState()

  const [userDetails, setUserDetaisl] = React.useState({
    uid: "",
    profilePicture: "",
    Name: "",
    LockerNumber: ""
  })
  const [sliderValue,setSliderValue] = React.useState(false); 
  const [openModal,setOpenModal] = React.useState(false)
  const [createModal,setCreateModal] = React.useState(false)
  const [changeModal,setChangeModal] = React.useState(false)

  const [checkPIN, setCheckPIN] = React.useState(false);

  // for my slider
  const [value, setValue] = React.useState(10);
  const [disabled, setDisabled] = React.useState(false);
  const [count, setCount] = React.useState(0);

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

      // *************** for Locker *************** //
      if(count < 0){

        setValue(10)
        setCount(null)
  
        setDisabled(false)

        openLocker({
          FullName: userDetails.Name,
          value: false,
          number: userDetails.LockerNumber
        })
  
        return
      }


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

    const intervalId = setInterval(() => {
      setCount(count - 1);
    }, 1000);



    return () => {
      window.removeEventListener("resize", () => setResponsiveness());
      clearInterval(countdown);
      clearInterval(intervalId);
    };

  },[value,Timer, count,isDisable])

  React.useEffect(()=>{

    let isMounted = true;

    // Check Locker status
    getLockerSensor("_" + String(userDetails.LockerNumber)).then(result=>setSliderValue(result))

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

  // handle to generate Token for faces
  const handleToken = e => {

      e.preventDefault()
      const tokenCode = TokenGenerator()
  
      setToken(tokenCode)
      setIsdisable(true)
      setTimer(30)
  
      pushToken({ FullName: userDetails.Name, Code: tokenCode })
  
    }


  // Handle change for slider
  const handleChange = (event, newValue) => {

    if (newValue >= 95){
      setValue(100)
      setDisabled(true)
      openLocker({
        FullName: userDetails.Name,
        value: true,
        number: userDetails.LockerNumber
      }).then(result => pushHistory(userDetails.Name))


      setCount(5)
      // setStatus(`5 LEFT TO LOCK`)
    }
    else{
      setValue(newValue)
    }

  };

  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'center', 
      alignItems: 'center', 
      minHeight: "100vh" 
      }}

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

       

              <IconButton size="small" color='primary' >
                {sliderValue ? <LockOutlinedIcon fontSize='large' style={{ fontSize: 70 }} /> 
                : <LockOpenOutlinedIcon fontSize='large' style={{ fontSize: 70, color:'red' }} />}
              </IconButton>

              <Typography variant='h5' color="#0F2C3D" fontWeight="bold" fontSize="1rem">
                your locker is { sliderValue ? "close" : "open"}
              </Typography> 
           
              <IOSUnlockSlider
              value={value}
              min={0}
              max={100}
              onChange={handleChange}
              disabled={disabled}
              valueLabelDisplay="auto"
              onTouchStart={event=>event.preventDefault()}
              onTouchMove={event=>event.preventDefault()}
              onTouchEnd={event=>event.preventDefault()}
              />

              <Typography variant='h5' color="#0F2C3D" fontWeight="lighter" fontSize="0.9rem">slide to open your locker {count}</Typography>
              
            </Stack>
          </Card>
        </Grid>



      </Grid>
    </div>
  );
};

export default MyLocker;
