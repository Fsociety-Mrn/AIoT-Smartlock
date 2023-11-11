import { 
  Box,
  Grid, Typography 
} from '@mui/material'
import CardItem from "../../Components/Card"
import React from 'react'


import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";


import { DataGrid, GridActionsCellItem } from '@mui/x-data-grid';
import DeleteIcon from '@mui/icons-material/Delete';
import SecurityIcon from '@mui/icons-material/Security';
import FileCopyIcon from '@mui/icons-material/FileCopy';



const initialRows = [
  {
    id: 1,
    name: 'Damien',
    age: 25,

    isAdmin: true,
    country: 'Spain',
    discount: '',
  },
  {
    id: 2,
    name: 'Nicolas',
    age: 36,

    isAdmin: false,
    country: 'France',
    discount: '',
  },
  {
    id: 3,
    name: 'Kate',
    age: 19,

    isAdmin: false,
    country: 'Brazil',
    discount: 'junior',
  },
  {
    id: 3,
    name: 'Kate',
    age: 19,

    isAdmin: false,
    country: 'Brazil',
    discount: 'junior',
  },
  {
    id: 3,
    name: 'Kate',
    age: 19,

    isAdmin: false,
    country: 'Brazil',
    discount: 'junior',
  },
  {
    id: 3,
    name: 'Kate',
    age: 19,

    isAdmin: false,
    country: 'Brazil',
    discount: 'junior',
  },
  {
    id: 3,
    name: 'Kate',
    age: 19,

    isAdmin: false,
    country: 'Brazil',
    discount: 'junior',
  },
  {
    id: 3,
    name: 'Kate',
    age: 19,

    isAdmin: false,
    country: 'Brazil',
    discount: 'junior',
  },
];

const Dashboard = () => {
  const [paddinSize, setPaddingSize] = React.useState()


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


  const [rows, setRows] = React.useState(initialRows);

  const deleteUser = React.useCallback(
    (id) => () => {
      setTimeout(() => {
        setRows((prevRows) => prevRows.filter((row) => row.id !== id));
      });
    },
    [],
  );

  const toggleAdmin = React.useCallback(
    (id) => () => {
      setRows((prevRows) =>
        prevRows.map((row) =>
          row.id === id ? { ...row, isAdmin: !row.isAdmin } : row,
        ),
      );
    },
    [],
  );

  const duplicateUser = React.useCallback(
    (id) => () => {
      setRows((prevRows) => {
        const rowToDuplicate = prevRows.find((row) => row.id === id);
        return [...prevRows, { ...rowToDuplicate, id: Date.now() }];
      });
    },
    [],
  );

  const columns = React.useMemo(
    () => [
      { field: 'name', type: 'string' },
      { field: 'age', type: 'number' },
      { field: 'dateCreated', type: 'date', width: 130 },
      { field: 'lastLogin', type: 'dateTime', width: 180 },
      { field: 'isAdmin', type: 'boolean', width: 120 },
      {
        field: 'country',
        type: 'singleSelect',
        width: 120,
        valueOptions: [
          'Bulgaria',
          'Netherlands',
          'France',
          'United Kingdom',
          'Spain',
          'Brazil',
        ],
      },
      {
        field: 'discount',
        type: 'singleSelect',
        width: 120,
        editable: true,
        valueOptions: ({ row }) => {
          if (row === undefined) {
            return ['EU-resident', 'junior'];
          }
          const options = [];
          if (!['United Kingdom', 'Brazil'].includes(row.country)) {
            options.push('EU-resident');
          }
          if (row.age < 27) {
            options.push('junior');
          }
          return options;
        },
      },
      {
        field: 'actions',
        type: 'actions',
        width: 80,
        getActions: (params) => [
          <GridActionsCellItem
            icon={<DeleteIcon />}
            label="Delete"
            onClick={deleteUser(params.id)}
          />,
          <GridActionsCellItem
            icon={<SecurityIcon />}
            label="Toggle Admin"
            onClick={toggleAdmin(params.id)}
            showInMenu
          />,
          <GridActionsCellItem
            icon={<FileCopyIcon />}
            label="Duplicate User"
            onClick={duplicateUser(params.id)}
            showInMenu
          />,
        ],
      },
    ],
    [deleteUser, toggleAdmin, duplicateUser],
  );


  return (
    <div style={{
      minHeight: "100vh"
    }}>

      <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      marginTop={paddinSize}
      spacing={2}
      padding={2}>

        <Grid item xs={10}>
          <Typography variant='h5'> Welcome to Dashboard</Typography>
        </Grid>

        {/* Status */}
        <Grid item xs={10}>
          <Carousel 
          responsive={responsive}
          draggable={false}
          showDots={window.innerWidth < 800 ? true : false}
          removeArrowOnDeviceType={["desktop", "superLargeDesktop"]}
          transitionDuration={500}
          autoPlay={window.innerWidth < 800 ? true : false}
          autoPlaySpeed={1000}
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

        <Grid item xs={10}>
          <Typography variant='h4'>History</Typography>
        </Grid>

        <Grid item xs={10} >
          <Box style={{ height: 400, width: '100%', backgroundColor: "white", padding: "15px", borderRadius: "20px"}}>
            <DataGrid columns={columns} rows={rows} sx={{ borderRadius: "20px", padding: "15px", }} />
         </Box>
        </Grid>


      </Grid>
    </div>
  )
}


export default Dashboard