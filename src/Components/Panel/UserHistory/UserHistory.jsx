import Titles from "../../Titles/Titles";
import Table from 'react-bootstrap/Table';
import React, { useState } from "react"; // Import React and useState
import { Button } from "react-bootstrap";
// import { DatePicker } from 'react-responsive-datepicker'
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
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 6;
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data?.slice(indexOfFirstItem, indexOfLastItem);

  const totalPages = Math.ceil(data.length / itemsPerPage);

  // ***************** datetime now ***************** //

  const options = { month: 'long', day: 'numeric', year: 'numeric' };
  const [isOpen, setIsOpen] = React.useState(false)
  // const [date, setDate] = React.useState()

  // ***************** Get Data ***************** //

  const transformData = (rawData) => {
    return Object.entries(rawData)?.flatMap(([date, timeData]) =>
      Object.entries(timeData).map(([time, accessType]) => {
        const formattedDate = new Date(`${date} ${time}`);
        return {
          date: formattedDate.toISOString().split('T')[0],
          time: formattedDate.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
          accessType,
        };
      })
    );
  };

  React.useEffect(()=>{



    const FullName = String(props.props.firstName + " " + props.props.lastName).toUpperCase()

    const getHistoryData = async () => {


      const data = await getHistory(FullName)

      if (data) {
        // date&& console.log(new Date(date).toISOString().split('T')[0])
        // const today = date ? new Date(date).toISOString().split('T')[0] : new Date().toISOString().split('T')[0]; // Get today's date
        // Filter data for today's date
        const todayData = transformData(data)
                        ?.sort((a, b) => {
                          const timeA = new Date(a.date + ' ' + a.time);
                          const timeB = new Date(b.date+ ' ' + b.time);

                          return timeB - timeA;
                        });
  
        setData(todayData);
      }
    }

    return () => getHistoryData()
  },[ props.props.firstName, props.props.lastName])

  // ***************** preview and next ***************** //



  const handleNext = () => {
    setCurrentPage(currentPage + 1);
    console.log(currentItems.length)
  };

  const handlePrev = () => {
    setCurrentPage(currentPage - 1);
  };



  return (
    <>
      <Titles
      title="Activity History 📈"
      text="View your AIoT Smartlock activity log"
      className="text-center "
      />


      {/* date time picker */}
     <div className="d-flex justify-content-between mt-4 mb-2">

        <Button variant="light" className="p-0" onClick={()=>setIsOpen(true)}>
          <CalendarEdit size="22" color="#000000"/>
        </Button>

        <h6>{new Date().toLocaleDateString(undefined,options)}</h6>


      </div>

 {/* 
      <DatePicker
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        defaultValue={date}
        onChange={(date)=>{
          setDate(new Date(date).toLocaleString(undefined,options))
          console.log(new Date(date).toLocaleString(undefined,options))
          setData(data?.filter((value,key)=>console.log(value.date === "2023-10-27")))
        }}
        minDate={new Date(2022, 0, 0)}
        maxDate={new Date(2033, 0, 0)}
        headerFormat='MM dd, DD'
      /> */}

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
          {currentItems.length !== 0? currentItems?.map((item, index) => (
            <tr key={index}>
            <td>{new Date(item.date).toLocaleString(undefined,options)}</td>
              <td>{item.time}</td>
              <td>{item.accessType}</td>
            </tr>
          )) : 
          <tr>
            <td></td>
            <td colspan="3">No activity Today</td>
          </tr>
          }
        </tbody>
      </Table>

      {/* Left and Right Button */}
      {!false &&   
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
