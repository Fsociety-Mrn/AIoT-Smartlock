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

import { get_AIoT_unlock, remove_token_data } from '../../firebase/Realtime_Db';

import dummyData from "./dummdata.json"

const data = dummyData

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
const extractUniqueDates = () => {
  // Extract unique dates
  const uniqueDates = [...new Set(transformDataToArray(data).sort((a,b)=>new Date(b.Date) - new Date(a.Date)).map(entry => entry.Date))];
  
  return uniqueDates;
};

// filter dates
const filterDataByDateAndAccessType = (targetDate, targetAccessType) => {
  return transformDataToArray(data).filter(entry => entry.Date === targetDate && entry.AccessType === targetAccessType);
};

const getFormattedTodayDate = () => {
  const today = new Date();
  const options = { month: 'short', day: 'numeric', year: 'numeric' };
  const formattedDate = today.toLocaleDateString('en-US', options);
  console.log("Date: ", String(formattedDate).replace(',',''))
  return formattedDate;
};

const Dashboard = () => {
  const [paddinSize, setPaddingSize] = React.useState()
  const [value, setValue] = React.useState(0);
  const [open, setOpen] = React.useState(false);
  const [alert, setAlert] = React.useState();
  const [dataToken, setTokenData] = React.useState()
  const [selectedSort, setSelectedSort] = React.useState(''); 
  const [anchorEl, setAnchorEl] = React.useState(null); // To manage Menu anchor

  const [tabStatus,setTabStatus] = React.useState('Facial Login')
  const [dataFrom,setDataFrom] = React.useState(filterDataByDateAndAccessType(getFormattedTodayDate(),tabStatus));

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
        setDataFrom(filterDataByDateAndAccessType(selectedSort,'Facial Login'))
      break;
      case 1:
        setDataFrom(filterDataByDateAndAccessType(selectedSort,'PIN Login'))
      break;
      case 2:
        setDataFrom(filterDataByDateAndAccessType(selectedSort,'IoT Access'))
      break;
      case 3:
        setDataFrom(filterDataByDateAndAccessType(selectedSort,'Access Denied'))
      break;
    }
  };

  const sortByName = (dataToSort) => {
    const sortedData = [...dataToSort].sort((a, b) => {
      if (a.Name < b.Name) return -1;
      if (a.Name > b.Name) return 1;
      return 0;
    });
    return sortedData;
  };

  // Function to sort table data by time/date
  const sortByTime = (dataToSort) => {
    const sortedData = [...dataToSort].sort((a, b) => {
      // Convert time/date strings to Date objects for comparison
      const dateA = new Date(a.Time);
      const dateB = new Date(b.Time);
      return dateA - dateB;
    });
    return sortedData;
  };

  const sortByDate = (dataToSort) => {
    const sortedData = [...dataToSort].sort((a, b) => {
      return new Date(a.Date).getTime() - new Date(b.Date).getTime();
    });
    return sortedData;
  };
  
  
  // State to hold the sorted data for "Today Access" table
  const [sortedTodayAccessData, setSortedTodayAccessData] = React.useState(rows);

  const handleSortTodayAccess = (sortType) => {
    let sortedTableData;
  
    switch (sortType) {
      case 'name':
        sortedTableData = sortByName(rows);
        setSortedTodayAccessData(sortedTableData);
        break;
      case 'time':
        sortedTableData = sortByTime(rows);
        setSortedTodayAccessData(sortedTableData);
        break;
        case 'date':
          sortedTableData = sortByDate(rows); // or sortedTodayAccessData if necessary
          setSortedTodayAccessData(sortedTableData);
          break;
        default:
          break;
    }
  };
  
  
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
    console.log(extractUniqueDates())
  };


  const handleSort = (sortType) => {
    // console.log(dataFrom)
    setSelectedSort(sortType); // Set selected sort option
    console.log(sortType)
    setDataFrom(filterDataByDateAndAccessType(sortType,'Facial Login'))
    
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

          {extractUniqueDates().map((date,index)=>(          
            <MenuItem key={index} onClick={() => handleSort(String(date))}>{date}</MenuItem>
          ))}

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


const rows = [
  { 
    id: 1,
    Name: 'ART LISBOA', 
    Time: '9:30 am', 
    Date: '2020-07-06',
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 6,
    Name: 'FRANZ MANECLANG', 
    Time: '10:30 am', 
    Date: '2019-06-05',
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 2,
    Name: 'REY CUMPA', 
    Time: '11:30 am', 
    Date: '2019-01-04',
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 3,
    Name: 'ROGER GAJUNERA', 
    Time: '12:30 am', 
    Date: '2019-02-03',
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 4,
    Name: 'IVAN FAMILARAN', 
    Time: '1:30 pm', 
    Date: '2019-09-02',
    AccessType: "IoT Login",
    Percentage: "90%"
  },
  { 
    id: 5,
    Name: 'KEYT LISBOA', 
    Time: '9:30 am', 
    Date: '2010-06-01',
    AccessType: "Face Login",
    Percentage: "90%"
  },

];

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
