import { 
    AppBar, 
    Avatar, 
    // BottomNavigation, 
    Box, 
    Drawer, 
    IconButton, 
    List, 
    Tab, 
    Tabs, 
    Typography
} from '@mui/material'
import Toolbar from '@mui/material/Toolbar';
import React from 'react'



import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import InboxIcon from '@mui/icons-material/MoveToInbox';
// import MuiBottomNavigationAction from "@mui/material/BottomNavigationAction";

// icons
// import SmartToyOutlinedIcon from '@mui/icons-material/SmartToyOutlined';
// import InfoIcon from '@mui/icons-material/Info';
// import MenuIcon from '@mui/icons-material/Menu';
import HomeRepairServiceIcon from '@mui/icons-material/HomeRepairService';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import HomeRoundedIcon from '@mui/icons-material/HomeRounded';

// import { styled } from "@mui/material/styles";
import ICON from '../Images/logo512.png'

import { useLocation, useNavigate, Route, Routes, Navigate } from 'react-router-dom';

import { useTheme } from '@emotion/react';

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


// Mobile mode

// for button custom button navigation
// const BottomNavigationAction = styled(MuiBottomNavigationAction)(`
//   color: rgb(12, 14, 36);
//   &.Mui-selected {
//     color: white;
//   }
// `);

const MobileAppbar = () => {
    const theme = useTheme();

    // const trigger = useScrollTrigger();
    const [value, setValue] = React.useState(0);

    const location = useLocation();
    let navigate = useNavigate();


    const getRoutePath = (index) => {
        // Define the route paths for each index
        const routePaths = [
          '/Admin/',
          '/Admin/LockerAvailable"',
          '/Admin/ManageLocker',
          '/Admin/MyAccount'
        ];
        return routePaths[index];
      };
    


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




// Desktop mode
const drawerWidth = 240;
const DesktopAppbar = () => {
    return (
        <div>

            <AppBar
            position="fixed"
            sx={{ 
                backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 50%, rgb(12, 14, 36) 100%)',
                zIndex: (theme) => theme.zIndex.drawer + 1 
            }}
            >
                <Toolbar variant="regular">
                         
                    <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
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


            </AppBar>



            <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
            }}
            >
                <Toolbar />

                <Box sx={{ overflow: 'auto' }}>

                    <List>

                     {/* My locker */}
                        <ListItem disablePadding>
                            <ListItemButton sx={{
                                color: "rgb(61, 152, 154)"
                            }}>
                  
                                <ListItemIcon
                                sx={{
                                color: "rgb(61, 152, 154)"
                            }}>
                                    <InboxIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="My locker" />
                            </ListItemButton>
                        </ListItem>
                        
                        {/* Locker availability */}
                        <ListItem disablePadding>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)"
                            }}>

                                <ListItemIcon 
                                sx={{
                                    color: "rgb(61, 152, 154)"
                                }}>
                                    <InboxIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Locker availability" />
                            </ListItemButton>
                        </ListItem>

                        {/* Locker availability */}
                        <ListItem disablePadding>
                            <ListItemButton 
                            sx={{
                                color: "rgb(61, 152, 154)"
                            }}>

                                <ListItemIcon 
                                sx={{
                                    color: "rgb(61, 152, 154)"
                                }}>
                                    <InboxIcon /> 
                                </ListItemIcon>

                                <ListItemText primary="Smartlocker Users" />
                            </ListItemButton>
                        </ListItem>



                    </List>
                </Box>
            </Drawer>
        </div>
    )
}
