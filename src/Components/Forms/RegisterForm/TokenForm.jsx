import React from 'react'

// import styles of this component
import styles from '../Forms.module.css'

// import other pkgs
import { Button, Col, Container, FloatingLabel, Form, Image, Row, Stack } from 'react-bootstrap'

import LOGO from '../../../Images/Arash.jpg'

const TokenForm = () => {
  return (
    <Container fluid className={`${styles.container} d-flex justify-content-center align-items-center px-5`}>
  
  {/* Token Form containers */}
    <Container className={`${styles.LoginContainer} d-flex justify-content-center align-items-center bg-white`}>
      <Container>
                
        <Row xs={12} className="justify-content-center align-items-center">

          {/* Title */}
          <Col xs={12} md={12}>
            <Stack gap={1} style={{ padding:"20px", marginTop:"80px"}} className={`d-flex justify-content-center align-items-center`}>
                            
              {/* Logo */}
              <Image 
              src={LOGO}
              style={{ width: '100px', height: '100px' }}
              roundedCircle />

              {/* Tutle */}
              <div className="h3" 
              style={{
                backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                WebkitBackgroundClip: 'text',
                color: 'transparent',
                display: 'inline',
                whiteSpace: "nowrap"
              }}>AIoT Smartlock</div>

              {/* Slogan */}
              <div className="blockquote" 
              style={{
                backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                WebkitBackgroundClip: 'text',
                color: 'transparent',
                display: 'inline',
                textAlign: "center"
              }}>Please enter your token code</div>

            </Stack> 
          </Col>
                            
          {/* Registration Form */}
          <Col xs={12} md={12}>     
            <Stack gap={2} className="col-md-10 mx-auto">

              {/* Email */}
              <FloatingLabel
              controlId="floatingInput"
              label="Token ID"
              className="mb-3">
                <Form.Control type="text" placeholder="EX: XXXXXX"/>
              </FloatingLabel>

            </Stack>
          </Col>

          {/* Login ?*/}
          <Col xs={12} md={12}>   
            <Stack gap={1} className={`d-flex justify-content-center align-items-center`}> 
              <div className="text" 
              style={{
                backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                WebkitBackgroundClip: 'text',
                color: 'transparent',
                display: 'inline',
                textAlign: "center"
              }}>Already have account ? <a className="text"  href='/'> <strong> Log in </strong></a></div>

            </Stack>  
          </Col>
                            
          {/* verify Token*/}
          <Col xs={12} md={11} style={{ marginTop:"10px", marginBottom:"100px"}} className='row row-cols-2 justify-content-center align-items-center'>
                            
            {/* Cancel Account */}
            <Col xs={12} md={5} sm={12} className='row row-cols-1 m-1'>
              <Button 
              variant="primary" 
              style={{
                background: 'white',
                color: 'rgb(61, 152, 154)',
                border: "2px solid rgb(61, 152, 154)",
                padding:"10px",
                borderRadius:"10px"
              }}>
                Verify Token
              </Button>
            </Col>

          </Col>

                            

        </Row>

        </Container>
    </Container>
    </Container>
  )
}

export default TokenForm