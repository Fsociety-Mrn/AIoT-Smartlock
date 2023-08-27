import { 
    AppBar, 
    Avatar, 
    BottomNavigation, 
    BottomNavigationAction, 
    Box, 
    Divider, 
    IconButton, 
    List,
    Typography
} from '@mui/material'
import Toolbar from '@mui/material/Toolbar';
import React from 'react'
import { styled, useTheme } from '@mui/material/styles';


import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import MuiDrawer from '@mui/material/Drawer';
import MuiAppBar from '@mui/material/AppBar';
// import MuiBottomNavigationAction from "@mui/material/BottomNavigationAction";

// icons
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import LockPersonIcon from '@mui/icons-material/LockPerson';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PeopleIcon from '@mui/icons-material/People';
// import SettingsIcon from '@mui/icons-material/Settings';

import defaultImage from "../Images/logo512.png"
import { statusLogin } from '../firebase/FirebaseConfig'
import { getUserDetails } from '../firebase/Firestore'

// import { styled } from "@mui/material/styles";
import ICON from '../Images/logo512.png'

import { useNavigate } from 'react-router-dom';

// import { useTheme } from '@emotion/react';


// admin Appbar
export const Appbar = () => {

  // get windows screen
  const [state, setState] = React.useState(true);
  React.useEffect(()=>{
      const setResponsiveness = () => {
          return window.innerWidth < 700 ? setState(true) : setState(false);
      };
  
      setResponsiveness();
          window.addEventListener("resize", () => setResponsiveness());
      return () => {
          window.removeEventListener("resize", () => setResponsiveness());
      };
  },[])

  return (
    <div>

        {state ? <MobileAppbar />  : <DesktopAppbar />} 
    </div>
  )
}

// =========================== Mobile mode =========================== //

const MobileAppbar = () => {

    const [value, setValue] = React.useState(0);
    let navigate = useNavigate();

    // FOR ROUTE changes 
    const handleChange = (event, newValue) => {
        setValue(newValue);
        switch(newValue){
            case 0:
                navigate("/Admin/");
            break;
            case 1:
                navigate("/Admin/MyLocker");
            break;
            case 2:
                navigate("/Admin/ManageLockerAccess");
            break;
            case 3:
                navigate("/Admin/ProfileSettings");
            break;

            default:
                navigate("/Admin/");
            break;

         }
      };

    // for swipe
    return (
        <div>
            <AppBar position="fixed">

                {/* Title */}
                <Toolbar variant="regular"                
                sx={{ 
                    // display: 'flex',
                    // justifyContent: 'center',
                    backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
                    borderBottom: 'none', // Remove the bottom border
                }}>

                    <IconButton edge="start" color="inherit" aria-label="menu" 
                    sx={{ mr: 1, marginTop: 1.5}}
                    >
                        <Avatar alt="Remy Sharp"
                        sx={{
                            border: "2px solid rgb(61, 152, 154)",
                            width: 50, height: 50 
                        }}
                        src={ICON}
                        >S</Avatar>
                    </IconButton>

                    <Typography variant="h5" 
                    fontFamily={'sans-serif'}
                    color="inherit" 
                    sx={{ marginTop: 1.5}}
                    >
                        AIoT Smartlock
                    </Typography>

                </Toolbar>
                <Box sx={{ marginTop: -1 }}                 
                >
                    <BottomNavigation 
                    sx={{ backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
                        '& .Mui-selected': {
                            color: 'white', // Color when an item is clicked
                            '& .MuiSvgIcon-root': {
                                color: 'white', // Icon color when an item is clicked
                            },
                        }, 
                    }} 
                    value={value} 
                onChange={handleChange}  >
                        <BottomNavigationAction icon={<DashboardIcon />}  />
                        <BottomNavigationAction icon={<LockPersonIcon />} />
                        <BottomNavigationAction icon={<PeopleIcon />} />
                        <BottomNavigationAction icon={<ManageAccountsIcon />} />
                    </BottomNavigation>
                </Box>
         
            </AppBar>



        </div>
    )
}

// =========================== Desktop mode =========================== //

const DesktopAppbar = () => {


    const drawerWidth = 260;

const openedMixin = (theme) => ({
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    overflowX: 'hidden',
  });
  
  const closedMixin = (theme) => ({
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    overflowX: 'hidden',
    width: `calc(${theme.spacing(7)} + 1px)`,
    [theme.breakpoints.up('sm')]: {
      width: `calc(${theme.spacing(8)} + 1px)`,
    },
  });



// Drawer Header
const DrawerHeaderCustom = styled('div')(({ theme }) => ({
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
  }));
  
  
  // Appbar
  const AppBarCustom = styled(MuiAppBar, {
    shouldForwardProp: (prop) => prop !== 'open',
  })(({ theme, open }) => ({
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    ...(open && {
      marginLeft: drawerWidth,
      width: `calc(100% - ${drawerWidth}px)`,
      transition: theme.transitions.create(['width', 'margin'], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
    }),
  }));
  
  // drawer
  const DrawerCustom = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
    ({ theme, open }) => ({
      width: drawerWidth,
      flexShrink: 0,
      whiteSpace: 'nowrap',
      boxSizing: 'border-box',
      ...(open && {
        ...openedMixin(theme),
        '& .MuiDrawer-paper': openedMixin(theme),
      }),
      ...(!open && {
        ...closedMixin(theme),
        '& .MuiDrawer-paper': closedMixin(theme),
      }),
    }),
  );


    let navigate = useNavigate()

    const theme = useTheme();
    const [open, setOpen] = React.useState(false);

    const handleDrawerOpen = () => {
        setOpen(true);
      };
    
    const handleDrawerClose = () => {
        setOpen(false);
      };

    const [colorClick, setColorClick] = React.useState({
        dashboard: "rgb(23, 44, 62)",
        myLocker: "rgb(61, 152, 154)",
        lockerAvail: "rgb(61, 152, 154)",
        manageLocker: "rgb(61, 152, 154)",
        profileSettings: "rgb(61, 152, 154)",
        settings: "rgb(61, 152, 154)"
    })


    // update profile
    const [image,setImage] = React.useState(defaultImage) //image

  React.useEffect(()=>{
    let isMounted = true;

    const fetchUserStatus = async () => {
      try {
        const user = await statusLogin();
        if (isMounted) {

          const details = await getUserDetails(user.uid)


          details.photoUrl ? setImage(details.photoUrl) : setImage(image)

        }
      } catch (error) {
        console.error('Error fetching user status:', error);
      }
    };

    fetchUserStatus();

        return () => {
            isMounted = false;
        };
    },[])

    return (
        <div>

            <AppBarCustom
            position="fixed"
            sx={{ 
                backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) ,rgb(12, 14, 36))',
                // zIndex: (theme) => theme.zIndex.drawer + 1 
            }}

            open={open}
            >
                <Toolbar variant="regular">
                         
                    <IconButton edge="start" color="inherit" 
                    onClick={handleDrawerOpen} 
                    sx={{ 
                        mr: 2, 
                        ...(open && { display: 'none' }) 
                    }}>

                    <Avatar alt="Remy Sharp"
                        sx={{
                            border: "2px solid rgb(61, 152, 154)",
                            height: '55px', width: '55px'
                        }}
                        src={ICON}
                        >S</Avatar>
                    </IconButton>
                    
                    <Typography variant="h6" color="inherit" component="div" sx={{ flexGrow: 1 }}>
                        AIoT Smartlock
                    </Typography>


                    {/* account button */}
                    <IconButton
                    size="large"
                    color="inherit"
                    > 
                        <Avatar alt="Remy Sharp"
                        src={image}
                        sx={{
                            border: "2px solid rgb(61, 152, 154)"
                        }}
                        >A</Avatar>
                    </IconButton> 

                </Toolbar>

            </AppBarCustom>



            <DrawerCustom
            variant="permanent"
            open={open}
            >

            <DrawerHeaderCustom>
                <IconButton onClick={handleDrawerClose}>
                {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
                </IconButton>
            </DrawerHeaderCustom>
            
            <Divider />



                    <List>

                     {/* Dashboard */}
                     <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(23, 44, 62)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }} 
                            onClick={()=>{
                                navigate("/Admin/");
                                setColorClick({
                                    dashboard: "rgb(23, 44, 62)", //DARK color
                                    myLocker: "rgb(61, 152, 154)",
                                    lockerAvail: "rgb(61, 152, 154)",
                                    manageLocker: "rgb(61, 152, 154)",
                                    profileSettings: "rgb(61, 152, 154)",
                                    settings: "rgb(61, 152, 154)"
                                });
                            }}
                            >
                  
                                <ListItemIcon
                                sx={{
                                    color: colorClick.dashboard,
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <DashboardIcon /> 
                                </ListItemIcon>

                                <ListItemText color='white' primary="Dashboard" sx={{ 
                                    opacity: open ? 1 : 0,
        
                                    }} />
                            </ListItemButton>
                        </ListItem>

                     {/* My locker */}
                        <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }} 
                            onClick={()=>{
                                navigate("/Admin/MyLocker");
                                setColorClick({
                                    dashboard: "rgb(61, 152, 154)",
                                    myLocker: "rgb(23, 44, 62)", //DARK color
                                    lockerAvail: "rgb(61, 152, 154)",
                                    manageLocker: "rgb(61, 152, 154)",
                                    profileSettings: "rgb(61, 152, 154)",
                                    settings: "rgb(61, 152, 154)"
                                });
                                }}
                            >
                  
                                <ListItemIcon
                                sx={{
                                color: colorClick.myLocker,
                                minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                            }}>
                                    <LockPersonIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="My locker" sx={{ opacity: open ? 1 : 0 }} />
                            </ListItemButton>
                        </ListItem>
                        
                  
                        {/* Manage Locker Access */}
                        <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }}
                            onClick={()=>{
                                navigate("/Admin/ManageLockerAccess");
                                setColorClick({
                                    dashboard: "rgb(61, 152, 154)",
                                    myLocker: "rgb(61, 152, 154)",
                                    lockerAvail: "rgb(61, 152, 154)", 
                                    manageLocker: "rgb(23, 44, 62)", //DARK color
                                    profileSettings: "rgb(61, 152, 154)", 
                                    settings: "rgb(61, 152, 154)"
                                });
                            }}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: colorClick.manageLocker,
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <PeopleIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Manage Locker Access" sx={{ opacity: open ? 1 : 0 }}/>
                            </ListItemButton>
                        </ListItem>

                        {/* Profile Settings */}
                        <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }}
                            onClick={()=>{
                                navigate("/Admin/ProfileSettings");
                                setColorClick({
                                    dashboard: "rgb(61, 152, 154)",
                                    myLocker: "rgb(61, 152, 154)",
                                    lockerAvail: "rgb(61, 152, 154)", 
                                    manageLocker: "rgb(61, 152, 154)",
                                    profileSettings: "rgb(23, 44, 62)", //DARK color
                                    settings: "rgb(61, 152, 154)",
                                });
                            }}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: colorClick.profileSettings,
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <ManageAccountsIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Profile Settings" sx={{ opacity: open ? 1 : 0 }}/>
                            </ListItemButton>
                        </ListItem>

                        {/* Smartlocker Settings */}
                        {/* <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }}
                            onClick={()=>{
                                navigate("/Admin/Settings");
                                setColorClick({
                                    dashboard: "rgb(61, 152, 154)",
                                    myLocker: "rgb(61, 152, 154)",
                                    lockerAvail: "rgb(61, 152, 154)", 
                                    manageLocker: "rgb(61, 152, 154)",
                                    profileSettings: "rgb(61, 152, 154)",
                                    settings: "rgb(23, 44, 62)", //DARK color
                                });
                            }}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: colorClick.settings,
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <SettingsIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Settings & Configuration" sx={{ opacity: open ? 1 : 0 }}/>
                            </ListItemButton>



                        </ListItem> */}


                    </List>
            
            </DrawerCustom>
        </div>
    )
}


// user Appbar
export const UserApbbar = () => {
    return (<div><DesktopAppbarUser/></div>)
}


// =========================== Desktop mode =========================== //

const DesktopAppbarUser = () => {

  // Appbar
  const AppBarCustom = styled(MuiAppBar, {
    shouldForwardProp: (prop) => prop !== 'open',
  })(({ theme }) => ({
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    })
  }));
  
 
    // update profile
    const [image,setImage] = React.useState(defaultImage) //image

    React.useEffect(()=>{
        let isMounted = true;

        const fetchUserStatus = async () => {
            try {
                const user = await statusLogin();
                    if (isMounted) {
                        const details = await getUserDetails(user.uid)
                        details.photoUrl ? setImage(details.photoUrl) : setImage(image)
                    }
                    } catch (error) {
                        console.error('Error fetching user status:', error);
                    }
        };

        fetchUserStatus();
        return () => {
            isMounted = false;
        };
    },[])

    return (
        <div>

            <AppBarCustom
            position="fixed"
            sx={{ 
                backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) ,rgb(12, 14, 36))'
            }}
            >
                <Toolbar variant="regular">
                         
                    <IconButton edge="start" color="inherit">

                    <Avatar alt="Remy Sharp"
                        sx={{
                            border: "2px solid rgb(61, 152, 154)",
                            height: '55px', width: '55px'
                        }}
                        src={ICON}
                        >S</Avatar>
                    </IconButton>
                    
                    <Typography variant="h6" color="inherit" component="div" sx={{ flexGrow: 1 }}>
                        AIoT Smartlock
                    </Typography>


                    {/* account button */}
                    <IconButton
                    size="large"
                    color="inherit"> 
                        <Avatar alt="Remy Sharp"
                        src={image}
                        sx={{
                            border: "2px solid rgb(61, 152, 154)",
                            height: '50px', width: '50px'
                        }}
                        >A</Avatar>
                    </IconButton> 

                </Toolbar>
            </AppBarCustom>
            
        </div>
    )
}