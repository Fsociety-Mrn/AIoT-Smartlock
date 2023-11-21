import { Paper, Typography } from '@mui/material'
import { Box } from '@mui/system'
import { DataGrid } from '@mui/x-data-grid'
import React from 'react'

const Table = (props) => {
  return (
    <div>
       {props.value === props.set &&
        <Paper sx={{ padding: "20px", borderRadius: "20px" }}> 
              
            <Box sx={{ height: 400, width: '100%',padding: "10px" }}>

                <DataGrid
                rows={props.rows}
                columns={props.columns}
                initialState={{
                pagination: {
                    paginationModel: { page: 0, pageSize: 5 },
                },
                }}
                pageSizeOptions={[5, 10]}
                />
                
              </Box>
        </Paper>}
    </div>
  )
}

export default Table