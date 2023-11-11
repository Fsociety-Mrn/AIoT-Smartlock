import { Box, Divider, Grid, Paper, Stack, Typography } from '@mui/material'
import Card from "../../Components/Card"
import React from 'react'
import styled from 'styled-components'
import TodayIcon from '@mui/icons-material/Today';
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";


const Dashboard = () => {
  const [paddinSize, setPaddingSize] = React.useState()
  const carouselRef = React.useRef(null);

  React.useEffect(()=>{
    const setResponsiveness = () => {
        return window.innerWidth < 700 ? setPaddingSize(15) : setPaddingSize(0);
    };

    setResponsiveness();
        window.addEventListener("resize", () => setResponsiveness());
    return () => {
        window.removeEventListener("resize", () => setResponsiveness());
    };
  },[])
    
  return (
    <div style={{
      minHeight: "100vh"
    }}>

      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="flex-start"
      marginTop={paddinSize}
      spacing={2}
      padding={2}
      sx={{ overflowX: 'auto' }} // Add this style
      >


        <Card 
        Title="Today Access"
        Number={0}
        />

        <Card 
        Title="Facial Login"
        Number={0}
        />

        <Card 
        Title="PIN Login"
        Number={0}
        />

        <Card 
        Title="IoT Login"
        Number={0}
        />

        <Card 
        Title="Access Denied"
        Number={0}
        />

        
<Card 
        Title="IoT Login"
        Number={0}
        />

        <Card 
        Title="Access Denied"
        Number={0}
        />


      </Grid>
    </div>
  )
}


// Components
const Item = styled(Paper)(() => ({
  backgroundColor: "#fff",
  padding: "20px",
  textAlign: 'center',
  color: "black",
  borderRadius: "30px"
}));

export default Dashboard