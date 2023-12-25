import { 
  Alert,
  Grid, 
  Button, 
  Tab, 
  Tabs,
  Typography,
  Collapse,
  MenuItem, 
  Menu

} from '@mui/material'
import { ExpandMore } from '@mui/icons-material';

import ModalAlert from '../../Components/Modal/ModalAlert';

import CardItem from "../../Components/Card"
import React from 'react'

import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";

import Table from '../../Components/Table';

import { get_AIoT_unlock, remove_token_data,getHistory } from '../../firebase/Realtime_Db';

// transform data
const transformDataToArray = (data) => {
  const result = [];

  Object.entries(data).forEach(([name, dates]) => {

    Object.entries(dates).forEach(([date, times]) => {
      Object.entries(times).forEach(([time, details]) => {

        const entry = {
          id: result.length + 1,
          Name: name,
          Time: time,
          Date: date,
          AccessType: details.Access_type,
          Percentage: details.Percentage ? `${details.Percentage}%` : null,
        };

        result.push(entry);
      });
    });
  });

  // Sort the result array based on Date and Time
  result.sort((a, b) => {
    return new Date(b.Date) - new Date(a.Date)
  });

  return result; // Add this line to return the sorted array
};

// extract the dates
const extractUniqueDates = (data) => {
  // Extract unique dates
  const uniqueDates = [...new Set(transformDataToArray(data).sort((a,b)=>new Date(b.Date) - new Date(a.Date)).map(entry => entry.Date))];
  
  return uniqueDates;
};

const filterDataByDateAndAccessType = (data,targetDate, targetAccessType) => {

  if (targetDate === 'Today Access'){
      return transformDataToArray(data).filter(entry => 
    entry.Date === getFormattedTodayDate() && 
    entry.AccessType === targetAccessType &&
    entry.Name !== 'No match detected'
  );
  }

  if (targetAccessType === "Access Denied"){

    return transformDataToArray(data).filter(entry => 
      entry.Date === targetDate && 
      entry.Name === 'No match detected'
    );
  }

  return transformDataToArray(data).filter(entry => 
    entry.Date === targetDate && 
    entry.AccessType === targetAccessType &&
    entry.Name !== 'No match detected'
  );
};

const getFormattedTodayDate = () => {
  const today = new Date();
  const options = { month: 'short', day: 'numeric', year: 'numeric' };
  const formattedDate = today.toLocaleDateString('en-US', options);
  return String(formattedDate).replace(',','');
};

const Dashboard = () => {
  const [data,setData] = React.useState({})
  const [paddinSize, setPaddingSize] = React.useState()
  const [value, setValue] = React.useState(0);
  const [open, setOpen] = React.useState(false);
  const [alert, setAlert] = React.useState();
  const [dataToken, setTokenData] = React.useState()
  const [selectedSort, setSelectedSort] = React.useState(''); 
  const [anchorEl, setAnchorEl] = React.useState(null); // To manage Menu anchor
  
  const [ totalAccess, setTotalAccess] = React.useState({
                                          TodayAccess: 0,
                                          FacialLogin: 0,
                                          PINLogin: 0,
                                          IoTLogin: 0,
                                          AccessDenied: 0
                                        })
  const [dataFrom,setDataFrom] = React.useState({});

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

    if(cleanup)
    {

      // Get data from firebase
      getHistory()
        .then(data=>{
          // set data
          const Data = data;
          console.log(Data)
          setData(Data);
          setDataFrom(filterDataByDateAndAccessType(Data,getFormattedTodayDate(),'Facial Login'))

          setTotalAccess({
            TodayAccess: transformDataToArray(Data)
                        .filter(entry => entry.Date === getFormattedTodayDate()).length,
            FacialLogin: filterDataByDateAndAccessType(Data,getFormattedTodayDate(),'Facial Login').length,
            PINLogin: filterDataByDateAndAccessType(Data,getFormattedTodayDate(),'PIN Login').length,
            IoTLogin: filterDataByDateAndAccessType(Data,getFormattedTodayDate(),'IoT Access').length,
            AccessDenied: filterDataByDateAndAccessType(Data,getFormattedTodayDate(),'Access Denied').length
          })

        })
        .catch(error=>setData({}))


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

  // Tab Change
  const handleChange = (event, newValue) => {
    setValue(newValue);
    switch (newValue){
      case 0:
        setDataFrom(filterDataByDateAndAccessType(data,selectedSort,'Facial Login'))
      break;
      case 1:
        setDataFrom(filterDataByDateAndAccessType(data,selectedSort,'PIN Login'))
      break;
      case 2:
        console.log("IoT Access: ", data)
        setDataFrom(filterDataByDateAndAccessType(data,selectedSort,'IoT Access'))
      break;
      case 3:
        setDataFrom(filterDataByDateAndAccessType(data,selectedSort,'Access Denied'))
      break;
      default:
        setDataFrom(filterDataByDateAndAccessType(data,selectedSort,'Facial Login'))
      break;
    }
  };

  // drop down click changes
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleSort = (sortType) => {

    setSelectedSort(sortType); // Set selected sort option

    setDataFrom(filterDataByDateAndAccessType(data, sortType,'Facial Login'))
    setTotalAccess(
      {
        TodayAccess: transformDataToArray(data)
                    .filter(entry => entry.Date === sortType).length,
    
        FacialLogin: filterDataByDateAndAccessType(data,sortType,'Facial Login').length,
        PINLogin: filterDataByDateAndAccessType(data,sortType,'PIN Login').length,
        IoTLogin: filterDataByDateAndAccessType(data,sortType,'IoT Access').length,
        AccessDenied: filterDataByDateAndAccessType(data,sortType,'Access Denied').length
      }
    )

    setValue(0);
    // handleSortTodayAccess(sortType); // Perform sorting
    setAnchorEl(null); // Close the dropdown menu
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
            Number={totalAccess.TodayAccess}
            />

            <CardItem 
            Title="Facial Login"
            Number={totalAccess.FacialLogin}
            />

            <CardItem 
            Title="PIN Login"
            Number={totalAccess.PINLogin}
            />

            <CardItem 
            Title="IoT Login"
            Number={totalAccess.IoTLogin}
            />

            <CardItem 
            Title="Access Denied"
            Number={totalAccess.AccessDenied}
            />

          </Carousel>

        </Grid>

      {/* Modern Button acting as dropdown */}
      <Grid item xs={12} md={10} sm={12}>

        <Button
        variant="contained"
        endIcon={<ExpandMore />} // Add the dropdown icon to the end of the button
        onClick={handleClick}
        >
          {selectedSort ? selectedSort : 'Today Access'}
        </Button>

        <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={() => setAnchorEl(null)}
        >
          <MenuItem onClick={() => handleSort('Today Access')}>Today Access</MenuItem>

          {extractUniqueDates(data)
            .filter(date=> date !== getFormattedTodayDate())
            .map((date,index)=>(          
              <MenuItem key={index} onClick={() => handleSort(String(date))}>{date}</MenuItem>
            ))
          }

        </Menu>

      </Grid>


      
        {/* Tabs Header */}
        <Grid item xs={12} md={10} sm={12}>
          <Tabs value={value} 
          onChange={handleChange}    
          variant="scrollable"
          scrollButtons
          allowScrollButtonsMobile
          >
            <Tab label="Facial Login" />
            <Tab label="PIN Login" />
            <Tab label="IoT Login" />
            <Tab label="Access Denied" />
          </Tabs>
        </Grid>

        {/* Tabs List */}
        <Grid item xs={12} md={10} sm={12}>

          {/* Facial Login */}
          <Table 
          value={value}
          set={0}
          rows={dataFrom} 
          columns={FacialLogin}
          />

          
          {/* PIN Login */}
          <Table 
          value={value}
          set={1}
          rows={dataFrom} 
          columns={PinLogin}
          />

          {/* IoT Login */}
          <Table 
          value={value}
          set={2}
          rows={dataFrom} 
          columns={IoTLogin}
          />

          {/* Access Denied */}
          <Table 
          value={value}
          set={3}
          rows={dataFrom} 
          columns={AccessDenied}
          />

        </Grid>

      </Grid>
    </div>
  )
}


const FacialLogin = [
  { field: 'Name', headerName: 'Name', width: 160 },
  { field: 'Percentage', headerName: 'Percentage', width: 130, sortable: false },
  { field: 'Time', headerName: 'Time', width: 130 }
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
