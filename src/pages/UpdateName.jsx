import React from 'react'
import { updateName } from '../firebase/Firestore';

import { MobileTextbox } from '../Components/Textfield';
import { Button, Grid, Stack, Typography } from '@mui/material';

import { Name_Schema } from '../Authentication/Validation'

const UpdateName = ({UID}) => {

    const [name,setName] = React.useState({
      FirstName: "",
      LastName: ""
    })

    const [error,setError] = React.useState({
        Firstname: "",
        FirstName_Error: false,
        Lastname: "",
        LastName_Error: false,
    })

    // validataion name
    const isValid = async() =>{
        try{
            await Name_Schema.validate({firstName: name.FirstName, lastName: name.LastName}, { abortEarly: false });
            
            updateName(UID, String(name.LastName + "," + name.FirstName));
 
            setError({
                Firstname: "",
                FirstName_Error: false,
                Lastname: "",
                LastName_Error: false,
            });

        }catch(validationError){

            // Extract specific er ror messages for email and password
            const FirstName = validationError.inner.find((error) => error.path === 'firstName');
            const LastName = validationError.inner.find((error) => error.path === 'lastName');

            validationError.inner.find((error) => console.log(error))

            setError({

              Firstname: !!FirstName,
              FirstName_Error: FirstName && FirstName.message,
              Lastname: !!LastName,
              LastName_Error: LastName && LastName.message,
          })
        }

    }
  
    // uddate buton
    const saveChanges = e => {
        e.preventDefault();
        isValid();

    }
    
    return (
    <div div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Grid
      container   
      direction="row"
      justifyContent="center"
      alignItems="center"
      spacing={1}
    
      style={{ 
        minHeight: "100vh"
      }}
      > 
        <Stack   
        direction="column"
        justifyContent="center"
        alignItems="center"     spacing={1}
    
       >
  
          <Typography 
            variant='h5'
            style={{ 
              backgroundImage: 'linear-gradient(to right, rgb(11, 131, 120) 0%, rgb(85, 98, 112) 100%)', 
              WebkitBackgroundClip: 'text', 
              WebkitTextFillColor: 'transparent' 
            }}
          >
            Please Update Your Name.
          </Typography>
  
          <Grid
          container   
          direction="row"
          justifyContent="center"
          alignItems="center"
          spacing={1}
          paddingLeft={3}
          paddingRight={2}
          > 
            <Grid item xs={6} sm={3} md={6} xl={6}>
              <MobileTextbox 
              fullWidth 
              label="First Name" 
              placeholder='Enter your first name'
              value={name.FirstName}
              onChange={e=>{
                setName({...name, FirstName: e.target.value})
              }}

              helperText={error.FirstName_Error}
              error={error.Firstname}
              />
            </Grid>
  
            <Grid item xs={6} sm={3} md={6} xl={6}>
              <MobileTextbox 
              fullWidth 
              label="Last Name"  
              placeholder='Enter your last name'
              value={name.LastName}
              onChange={e=>{
                setName({...name, LastName: e.target.value})
              }}

              helperText={error.LastName_Error}
              error={error.Lastname}
              />
            </Grid>
  
            <Grid item xs={8}>
  
              {/* Save Chanegs */}
              <Button 
              variant='contained' 
              fullWidth
              style={{
                // background: 'linear-gradient(to right, rgb(11, 131, 120) 0%, #e7e5d6b5 100%)',
                marginBottom: '15px',
                background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                textTransform: 'none',
                fontFamily: 'sans-serif',
                borderRadius: 25,
                boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.25)',
                fontWeight: 'bold',
                fontSize: '16px',
                transition: 'background-color 0.3s ease',
                    // Mobile-specific styles
                '@media (maxWidth: 300px)': {
                    fontSize: '14px',
                    padding: '10px 16px',
                  },
                }}
              onClick={saveChanges}
              >Save Changes</Button>
            </Grid>
  
          </Grid>
  
          
                 
  
        </Stack>
       
      </Grid>
    </div>
    )
  }

export default UpdateName