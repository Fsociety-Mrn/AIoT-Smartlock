import { 
  Alert,
  Grid, 
  Button, 
  Tab, 
  Tabs,
  Typography,
  Collapse
} from '@mui/material'
import ModalAlert from '../../Components/ModalAlert';

import CardItem from "../../Components/Card"
import React from 'react'

import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";

import Table from '../../Components/Table';

import { get_AIoT_unlock, remove_token_data } from '../../firebase/Realtime_Db';

const Dashboard = () => {
  const [paddinSize, setPaddingSize] = React.useState()
  const [value, setValue] = React.useState(0);
  const [open, setOpen] = React.useState(false);
  const [alert, setAlert] = React.useState();
  const [dataToken, setTokenData] = React.useState()

  const isExpired = (expirationDateTime) => {
    // Convert the expiration date string to a Date object
    const expirationDate = new Date(expirationDateTime.date + ' ' + expirationDateTime.time);
  
    // Get the current date and time
    const currentDate = new Date();
  
    // Compare the current date and time with the expiration date and time
    return currentDate.getTime() > expirationDate.getTime();
  }

  React.useEffect(()=>{

    let cleanup = true;

    if(cleanup){

    // check if AIoT Smartlock is Lock
    get_AIoT_unlock().then(data=>{

      // set alert
      setAlert(data.isLock)
      if (data.data){
        setTokenData(data.data)
        isExpired(data.data.expiration) === true && remove_token_data()
      }
    })
       
  }


    const setResponsiveness = () => {
        return window.innerWidth < 700 ? setPaddingSize(15) : setPaddingSize(0);
    };

    setResponsiveness();

    window.addEventListener("resize", () => setResponsiveness());

 

    return () => {
      cleanup = false
        window.removeEventListener("resize", () => setResponsiveness());
    };
  },[])
    
  const responsive = {
    superLargeDesktop: {
      // the naming can be any, depends on you.
      breakpoint: { max: 4000, min: 1024 },
      items: 5,
      slidesToSlide: 2,
    },
    desktop: {
      breakpoint: { max: 1024, min: 800 },
      items: 4,
    },
    tablet: {
      breakpoint: { max: 800, min: 464 },
      items: 2,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1,
    },
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div 
    style={{ minHeight: "100vh" }} >

      <ModalAlert setOpen={setOpen} open={open} data={dataToken}  />

      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      marginTop={paddinSize}
      spacing={2}
      padding={2}>

        {/* Alert for unlock */}
        <Grid item xs={12} md={10} sm={12}>

            <Collapse in={alert}>
            <Alert variant="filled" severity="error" sx={{ width: '100%' }} 
            action={(    
              <Button color="inherit"  variant="filled" size="small" fullWidth onClick={()=>setOpen(true)}>
              Unlock
              </Button>)}>

              <Typography noWrap color="white">AIoT Smartlock is Lock!</Typography>
            
            </Alert>
            </Collapse>
        </Grid>
      

        {/* Status */}
        <Grid item xs={10}>
          <Carousel 
          responsive={responsive}
          draggable={false}
          showDots={window.innerWidth < 800 ? true : false}
          removeArrowOnDeviceType={["desktop", "superLargeDesktop"]}
          transitionDuration={1000}
          autoPlay={window.innerWidth < 800 ? true : false}
          autoPlaySpeed={500}
          keyBoardControl={true}
          ssr={true} // means to render carousel on server-side.
          infinite={window.innerWidth < 800 ? true : false}
          >

            <CardItem 
            Title="Today Access"
            Number={0}
            />

            <CardItem 
            Title="Facial Login"
            Number={0}
            />

            <CardItem 
            Title="PIN Login"
            Number={0}
            />

            <CardItem 
            Title="IoT Login"
            Number={0}
            />

            <CardItem 
            Title="Access Denied"
            Number={0}
            />

          </Carousel>
        </Grid>

        {/* Tabs Header */}
        <Grid item xs={12} md={10} sm={12}>
          <Tabs value={value} onChange={handleChange}    
          variant="scrollable"
          scrollButtons
          allowScrollButtonsMobile
          >
            <Tab label="Today Access" />
            <Tab label="Facial Login" />
            <Tab label="PIN Login" />
            <Tab label="IoT Login" />
            <Tab label="Access Denied" />
          </Tabs>
        </Grid>

        {/* Tabs List */}
        <Grid item xs={12} md={10} sm={12}>

          {/* Today Access */}
          <Table 
          value={value}
          set={0}
          rows={rows}
          columns={columns}
          />

          {/* Facial Login */}
          <Table 
          value={value}
          set={1}
          rows={rows}
          columns={FacialLogin}
          />

          
          {/* PIN Login */}
          <Table 
          value={value}
          set={2}
          rows={rows}
          columns={PinLogin}
          />

          {/* IoT Login */}
          <Table 
          value={value}
          set={3}
          rows={rows}
          columns={IoTLogin}
          />

          {/* Access Denied */}
          <Table 
          value={value}
          set={4}
          rows={rows}
          columns={AccessDenied}
          />

        </Grid>

      </Grid>
    </div>
  )
}

const columns = [
  // { field: 'id', headerName: 'ID', width: 70 },
  { field: 'Name', headerName: 'Name', width: 230 },
  { field: 'Time', headerName: 'Time', width: 130 },
  { field: 'AccessType', headerName: 'Access Type', width: 160, sortable: false },
  { field: 'Percentage', headerName: 'Percentage', width: 130, sortable: false }
];

const rows = [
  { 
    id: 1,
    Name: 'ART LISBOA', 
    Time: '9:30 am', 
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 6,
    Name: 'FRANZ MANECLANG', 
    Time: '9:30 am', 
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 2,
    Name: 'REY CUMPA', 
    Time: '9:30 am', 
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 3,
    Name: 'ROGER GAJUNERA', 
    Time: '9:30 am', 
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 4,
    Name: 'IVAN FAMILARAN', 
    Time: '9:30 am', 
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 5,
    Name: 'KEYT LISBOA', 
    Time: '9:30 am', 
    AccessType: "Face Login",
    Percentage: "90%"
  },

];

const FacialLogin = [
  { field: 'Name', headerName: 'Name', width: 160 },
  { field: 'Time', headerName: 'Time', width: 130 },
  { field: 'Percentage', headerName: 'Percentage', width: 130, sortable: false }
]

const PinLogin = [
  { field: 'Name', headerName: 'Name', width: 160 },
  { field: 'Time', headerName: 'Time', width: 130 },
]
const IoTLogin = [
  { field: 'Name', headerName: 'Name', width: 160 },
  { field: 'Time', headerName: 'Time', width: 130 },
]

const AccessDenied = [
  { field: 'Time', headerName: 'Time', width: 130 },
  { field: 'AccessType', headerName: 'Access Type', width: 160, sortable: false },
  { field: 'Percentage', headerName: 'Percentage', width: 130, sortable: false }
]

export default Dashboard