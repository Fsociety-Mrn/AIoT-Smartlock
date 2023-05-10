import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { BrowserRouter } from 'react-router-dom';

const theme = createTheme({
  palette: {
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
      disabled: '#000000',
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
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </ThemeProvider>
  </React.StrictMode>
);
// background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)'

