import { Box, Grid  } from '@mui/material'
import React from 'react'

const Login = () => {
  return (
    <div>
    
      <Grid 
      container   
      direction="row"
      justifyContent="center"
      alignItems="center"
      spacing={0}
      style={{ 
        minHeight: "90vh"
      }}
      >

      {/* lineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                  "    color:rgba(255, 255, 255, 210) */}
        <Grid item>
          
          <Box
            sx={{
              width: 280,
              height: 430,
              backgroundColor: 'primary.dark',
              borderTopLeftRadius: '50px',
              background: 'linear-gradient(to right, rgba(11, 131, 120, 0.86) 0%, rgba(85, 98, 112, 0.89) 100%)' 

            }}
          />

        </Grid>

        <Grid item>
          <Box
            sx={{
              width: 240,
              height: 430,
              backgroundColor: 'white',
              borderBottomRightRadius: '50px'
            }}
          />
        </Grid>

      </Grid>

    </div>
  )
}

export default Login

