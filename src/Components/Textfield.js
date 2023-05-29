import { TextField } from '@mui/material';

import { styled } from "@mui/material/styles";


const primaryColour = 'rgb(255, 255, 255)'; //Green
// const lightColour = '#6DA043';  //Light Green
// const secondaryColour = '#FFFFFF';
const lastColour = 'rgb(11, 131, 120)';

export const MobileTextbox = styled(TextField)({
    input: {
        color:'rgb(11, 131, 120)',
        borderRadius: '5px',
        background: primaryColour,
        '&::placeholder': {
            color: 'rgb(12, 14, 36) '
          }
    },

    "& label.Mui-focused": {
      color: primaryColour
    },
    "& .MuiInput-underline:after": {
      borderBottomColor: primaryColour
    },
    "& .MuiOutlinedInput-root": {
      "& fieldset": {
        borderColor: lastColour
      },
      "&:hover fieldset": {
        borderColor: lastColour
      },
      "&.Mui-focused fieldset": {
        borderColor: primaryColour
      }
    }
  });


export const DesktopTextbox = styled(TextField)({
  label:{
    color:'rgb(11, 131, 120)'
  },
  input: {
    color:'rgb(11, 131, 120)',
    borderRadius: '5px',
    background: primaryColour,
      '&::placeholder': {
          color: 'rgb(12, 14, 36) '
        }
  },

  "& label.Mui-focused": {
    color: primaryColour,
  },
  "& .MuiInput-underline:after": {
    borderBottomColor: primaryColour
  },
  "& .MuiOutlinedInput-root": {
    "& fieldset": {
      borderColor: lastColour
    },
    "&:hover fieldset": {
      borderColor: lastColour
    },
    "&.Mui-focused fieldset": {
      borderColor: 'rgb(11, 131, 120)'
    }
  }
  });


  export const DesktopTextboxManage = styled(TextField)({
    label:{
      color:'rgb(11, 131, 120)'
    },
    input: {
      color:'rgb(11, 131, 120)',
      borderRadius: '20px',
      background: primaryColour,
      '&::placeholder': {
        color: 'rgb(12, 14, 36) '
      },
      fontWeight: 550, // Adjust the font weight here
    },
  
    "& label.Mui-focused": {
      color: primaryColour,
    },
    "& .MuiInput-underline:after": {
      borderBottomColor: primaryColour
    },
    "& .MuiOutlinedInput-root": {
      backgroundColor: "white",
      "& fieldset": {
        borderColor: lastColour,
        borderWidth: '2px', // Adjust the border thickness here
      },
      "&:hover fieldset": {
        borderColor: lastColour
      },
      "&.Mui-focused fieldset": {
        borderColor: 'rgb(11, 131, 120)'
      }
    },
  
    });