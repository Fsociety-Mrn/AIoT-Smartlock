import Titles from "../../Titles/Titles";
import Table from 'react-bootstrap/Table';
import React, { useState } from "react"; // Import React and useState
import { Button } from "react-bootstrap";
import { DatePicker } from 'react-responsive-datepicker'
import 'react-responsive-datepicker/dist/index.css'

import {
  ArrowLeft2,
  ArrowRight2,
  CalendarEdit,
} from "iconsax-react";

// Database
import { getHistory } from "../../../utils/Firebase/Database/Database"

const UserDashboard = (props) => {
  const [data,setData] = useState([])
  const [secondData,setSecondData] = useState([])
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 6;
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data?.slice(indexOfFirstItem, indexOfLastItem);

  const totalPages = Math.ceil(data.length / itemsPerPage);

  // ***************** datetime now ***************** //

  const options = { month: 'long', day: 'numeric', year: 'numeric' };
  const [isOpen, setIsOpen] = React.useState(false)
  const [date, setDate] = React.useState() 
  

  // ***************** Get Data ***************** //

  const transformData = (rawData) => {
    return Object.entries(rawData)?.flatMap(([date, timeData]) =>
      Object.entries(timeData).map(([time, accessType]) => {
        const formattedDate = new Date(`${date} ${time}`);
        return {
          date: formattedDate.toISOString().split('T')[0],
          time: formattedDate.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
          accessType: accessType.Access_type,
        };
      })
    );
  };

  React.useEffect(()=>{

    let isMounted = true;

    const FullName = String(props.props.firstName + " " + props.props.lastName).toUpperCase()

    const getHistoryData = async () => {

      const datasss = await getHistory(FullName)

      if (isMounted && datasss) {


        // Filter data for today's date
        const todayData = transformData(datasss)
                        ?.sort((a, b) => {
                          const timeA = new Date(a.date + ' ' + a.time);
                          const timeB = new Date(b.date+ ' ' + b.time);

                          return timeB - timeA;
                        });

        console.log(todayData)

        setSecondData(todayData)

        setData(todayData.filter(value=> {
          return new Date(value.date).toLocaleString(undefined, options) === new Date().toLocaleString(undefined,options)
        }));

        
      }
    }

    if (isMounted){
      getHistoryData();
    }

    return () => {
      isMounted = false
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  },[props.props.firstName, props.props.lastName])

  // ***************** preview and next ***************** //



  const handleNext = () => {
    setCurrentPage(currentPage + 1);
  };

  const handlePrev = () => {
    setCurrentPage(currentPage - 1);
  };



  return (
    <>
<Titles
  title="Activity History 📈"
  text="View your Locker Access Activity Log"
  className="text-center"
/>



      {/* date time picker */}
     <div className="d-flex justify-content-between mt-4 mb-2">

        <h6>{date ? date : new Date().toLocaleString(undefined,options)}</h6>

        <Button variant="light" className="p-0" 
        onClick={()=>setIsOpen(true)}
        >
          <CalendarEdit size="22" color="#000000"/>
        </Button>


      </div>

 
      <DatePicker
        isOpen={isOpen}
        
        onClose={() => {
          setIsOpen(false)
          setData(secondData?.filter((value, key) => { return new Date(value.date).toLocaleString(undefined, options) === new Date(date).toLocaleString(undefined,options)}))
        }}
        defaultValue={date}
        onChange={(datesss)=>setDate(new Date(datesss).toLocaleString(undefined,options))}
        minDate={new Date(2022, 0, 0)}
        maxDate={new Date(2033, 0, 0)}
        headerFormat='MM dd, DD'
      />

      {/* Table  */}
      <Table hover size="sm">
        <thead>
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th>Access type</th>
          </tr>
        </thead>

        <tbody>
          {currentItems?.map((item, index) => (
            <tr key={index}>
            <td>{new Date(item.date).toLocaleString(undefined,options)}</td>
              <td>{item.time}</td>
              <td>{item.accessType}</td>
            </tr>
          )) }
        </tbody>
      </Table>

      {/* Left and Right Button */}
      {!isOpen &&   
        <div className="d-flex justify-content-between">

          <Button
          variant="light" className="p-0" 
          onClick={handlePrev}
          disabled={currentPage === 1}>
            <ArrowLeft2 size="32" color="#000000"/>
          </Button>

          <Button
          variant="light" className="p-0" 
          onClick={handleNext}
          disabled={currentPage === totalPages}>
            <ArrowRight2 size="32" color="#000000"/>
          </Button>

        </div>}
    </>
  );
};


export default UserDashboard;
