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
      borderColor: 'rgb(11, 131, 120)'
    }
  }
  });