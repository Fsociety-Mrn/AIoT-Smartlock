import React from 'react'
import { Navigate, Route, Routes } from 'react-router'

import Panel from "../../Components/Panel/Panel"
import Loading from "../../Components/Forms/Loading"

const Mainmenu = (props) => {

  return (
    <React.Suspense fallback={<Loading/>}>
        <div>      
          <Routes>

            <Route path="/" element={<Panel email={props.email} UID={props.UID}/>}/>
            <Route path="*" element={<Navigate to="/"/>}/>

          </Routes> 

        </div>
      </React.Suspense>
  )
}

export default Mainmenu