import { Box, Grid, Stack, Typography } from '@mui/material'
import TodayIcon from '@mui/icons-material/Today';
import PinIcon from '@mui/icons-material/Pin';
import SentimentSatisfiedAltIcon from '@mui/icons-material/SentimentSatisfiedAlt';
import SmartphoneIcon from '@mui/icons-material/Smartphone';
import SmsFailedIcon from '@mui/icons-material/SmsFailed';

import React from 'react'

const Icon = ({ icon }) => {
    return (
        <>
            {icon === "Today Access" && <TodayIcon color='primary' fontSize='large' />}
            {icon === "Facial Login" && <SentimentSatisfiedAltIcon color='primary' fontSize='large' />}
            {icon === "PIN Login" && <PinIcon color='primary' fontSize='large' />}
            {icon === "IoT Login" && <SmartphoneIcon color='primary' fontSize='large' />}
            {icon === "Access Denied" && <SmsFailedIcon color='error' fontSize='large' />}
        </>
    );
};


const Card = (props) => {
    return (
        <Grid item xs={8} md={2} sm={3}>
          <Box
          padding={2}
          sx={{
            backgroundColor: "white",
            borderRadius: "20px",
            textAlign: "center", // Center the content
            alignItems: "flex-start"
          }}>
            
            <Stack
            direction="row"
            justifyContent="flex-start"
            alignItems="center"
            spacing={2}
            > 

              <Icon icon={props.Title} />
              
              <Stack
              direction="column"
              justifyContent="center"
              alignItems="center"
    
              >
                <Typography variant='body1' color="#0F2C3D" noWrap>{props.Title}</Typography>
                <Typography variant='h4' color="#0F2C3D" gutterBottom>{props.Number}</Typography>
              </Stack>

            </Stack>

         
          </Box>
        </Grid>
   
    )
}

export default Card