import { 
    AppBar, 
    Avatar, 
    // BottomNavigation, 
    Box, 
    Divider, 

    IconButton, 
    List, 
    Tab, 
    Tabs, 
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
// import SmartToyOutlinedIcon from '@mui/icons-material/SmartToyOutlined';
// import InfoIcon from '@mui/icons-material/Info';
// import MenuIcon from '@mui/icons-material/Menu';
import HomeRepairServiceIcon from '@mui/icons-material/HomeRepairService';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import HomeRoundedIcon from '@mui/icons-material/HomeRounded';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import ChecklistRtlIcon from '@mui/icons-material/ChecklistRtl';
import LockPersonIcon from '@mui/icons-material/LockPerson';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PeopleIcon from '@mui/icons-material/People';
import SettingsIcon from '@mui/icons-material/Settings';



// import { styled } from "@mui/material/styles";
import ICON from '../Images/logo512.png'

import { useNavigate } from 'react-router-dom';

// import { useTheme } from '@emotion/react';

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
        {/* <DesktopAppbar /> */}
    </div>
  )
}


// Mobile mode

// for button custom button navigation
// const BottomNavigationAction = styled(MuiBottomNavigationAction)(`
//   color: rgb(12, 14, 36);
//   &.Mui-selected {
//     color: white;
//   }
// `);

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
                navigate("/Admin/LockerAvailable");
            break;
            case 2:
                navigate("/Admin/ManageLocker");
            break;
            case 3:
                navigate("/Admin/MyAccount");
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
                <Box sx={{ marginTop: -1 }}>
                <Tabs 
                value={value} 
                onChange={handleChange}        
                indicatorColor='secondary'  
                textColor='inherit'
                sx={{ 
                    backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
                    border: 'none', // Remove the bottom border
                }}
                centered>

      
                    <Tab icon={<HomeRoundedIcon />} />
                    <Tab icon={<AccountCircleIcon />}  />
                    <Tab icon={<HomeRepairServiceIcon />}  />
                    <Tab icon={<AccountCircleIcon />}  />
 
                </Tabs>
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
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }} 
                            onClick={()=>navigate("/Admin/")}
                            >
                  
                                <ListItemIcon
                                sx={{
                                color: "rgb(61, 152, 154)",
                                minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                            }}>
                                    <DashboardIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Dashboard" sx={{ opacity: open ? 1 : 0 }} />
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
                            onClick={()=>navigate("/Admin/MyLocker")}
                            >
                  
                                <ListItemIcon
                                sx={{
                                color: "rgb(61, 152, 154)",
                                minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                            }}>
                                    <LockPersonIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="My locker" sx={{ opacity: open ? 1 : 0 }} />
                            </ListItemButton>
                        </ListItem>
                        
                        {/* Locker availability */}
                        <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }}
                            onClick={()=>navigate("/Admin/LockerAvailable")}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: "rgb(61, 152, 154)",
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <ChecklistRtlIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Locker availability" sx={{ opacity: open ? 1 : 0 }} />
                            </ListItemButton>
                        </ListItem>

                        {/* Smartlocker Users */}
                        <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }}
                            onClick={()=>navigate("/Admin/ManageLocker")}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: "rgb(61, 152, 154)",
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <PeopleIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Manage Access & Users" sx={{ opacity: open ? 1 : 0 }}/>
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
                            onClick={()=>navigate("/Admin/ProfileSettings")}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: "rgb(61, 152, 154)",
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
                        <ListItem disablePadding sx={{ display: 'block' }}>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)",
                                minHeight: 48,
                                justifyContent: open ? 'initial' : 'center',
                                px: 2.5,
                            }}
                            onClick={()=>navigate("/Admin/Settings")}
                            >

                                <ListItemIcon 
                                sx={{
                                    color: "rgb(61, 152, 154)",
                                    minWidth: 0,
                                    mr: open ? 3 : 'auto',
                                    justifyContent: 'center',
                                }}>
                                    <SettingsIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Settings & Configuration" sx={{ opacity: open ? 1 : 0 }}/>
                            </ListItemButton>



                        </ListItem>


                    </List>
            
            </DrawerCustom>
        </div>
    )
}
