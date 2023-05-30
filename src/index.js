import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { BrowserRouter } from 'react-router-dom';
import CssBaseline from '@mui/material/CssBaseline';
import { Box } from '@mui/material';
import './Index.css'

const theme = createTheme({
  typography: {
    "fontFamily": 'sans-serif',
    "fontSize": 14,
    "fontWeightLight": 300,
    "fontWeightRegular": 400,
    "fontWeightMedium": 500,
    allVariants: {
      color: 'rgb(61, 152, 154)'
    }
  },

  palette: {
    background: {
      default: '#e7e5d6b5', // Set your desired background color here
    },
    
    primary: {
      main: 'rgb(61, 152, 154)',
    },
    secondary: {
      main: '#FFFFFF',
    },

    info: {
      main: '#F7C873',
    },
    text:{
      primary: "rgb(61, 152, 154)",
      disabled: 'rgb(12, 14, 36)',
    },
    error:{
      main: '#c71e1e',
    },
    warning:{
      main: '#ff8c00'
    },
    success:{
      main: '#32cd32'
    },
  },
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <CssBaseline />
    <ThemeProvider theme={theme}>
      <BrowserRouter>
      <Box sx={{ backgroundColor: '#e7e5d6b5', minHeight: '100vh' }}>
        <App />
        </Box>
      </BrowserRouter>
    </ThemeProvider>
  </React.StrictMode>
);
// background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)'

