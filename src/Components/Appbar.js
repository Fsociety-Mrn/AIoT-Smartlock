import { AppBar, Drawer, IconButton, Typography } from '@mui/material'
import Toolbar from '@mui/material/Toolbar';
import React from 'react'
import MenuIcon from '@mui/icons-material/Menu';
import CssBaseline from '@mui/material/CssBaseline';


export const Appbar = () => {
  return (
    <div>
        <DesktopAppbar/>
    </div>
  )
}


const drawerWidth = 240;
const DesktopAppbar = () => {
    return (
        <div>
            <CssBaseline />
            <AppBar position="static"
            position="fixed"
            sx={{ 
                bgcolor: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                zIndex: (theme) => theme.zIndex.drawer + 1 
            }}
            >
                <Toolbar variant="regular">

                    <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" color="inherit" component="div">
                        AIoT Smartlock
                    </Typography>

                </Toolbar>
            </AppBar>



            <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
            }}
            ></Drawer>
        </div>
    )
}
