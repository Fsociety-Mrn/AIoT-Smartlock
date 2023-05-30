import { Backdrop, CircularProgress } from '@mui/material'
import React from 'react'

const Loading = () => {
  return (
    <div>    
    <Backdrop
    open={true}
    >
        <CircularProgress color="primary" />
    </Backdrop></div>
  )
}

export default Loading