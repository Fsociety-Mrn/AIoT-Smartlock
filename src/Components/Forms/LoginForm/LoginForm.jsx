import React from 'react'

// import styles of this component
import styles from '../Forms.module.css'


// import other pkgs
import { Button, Col, Container, FloatingLabel, Form, Image, Row, Stack } from 'react-bootstrap'

import LOGO from '../../../Images/Arash.jpg'

const LoginForm = () => {
    return (
        <Container fluid className={`${styles.container} d-flex justify-content-center align-items-center`}>
            
            {/* Login Form containers */}
            <Container className={`${styles.LoginContainer} d-flex justify-content-center align-items-center bg-white`}>
                <Container>
                
                    <Row xs={12}>
                    
                        <Col xs={12} md={12} >
                            <Stack gap={1} style={{ padding:"20px", marginTop:"80px" }} className={`d-flex justify-content-center align-items-center`}>
                            
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
                                }}>Unlocking Tomorrow's Security, Today</div>

                           </Stack> 
                        </Col>

                        <Col xs={12} md={12}>      
                            <Stack gap={2} className="col-md-10 mx-auto">

                            {/* Email */}
                                <FloatingLabel
                                controlId="floatingInput"
                                label="Email"
                                className="mb-3">
                                    <Form.Control type="email" placeholder="name@example.com"/>
                                </FloatingLabel>

                            {/* Password */}
                                <FloatingLabel controlId="floatingPassword" label="Password">
                                    <Form.Control type="password" placeholder="Password" />
                                </FloatingLabel>

                            {/* Forgot Password */}
                                <Form.Text href="youtube.com" className="text-muted">
                                    <a href="/" color='rgb(61, 152, 154)'>
                                        Forgot Password?
                                    </a>
                                </Form.Text>

                            </Stack>
                        </Col>


                        {/* Login */}
                        <Col xs={12} md={12} style={{ marginTop:"20px",padding:"20px",justifyingContent:"center" }}>   
                            <Stack gap={2} className="col-md-9 mx-auto">     
                                <Button variant="primary" 
                                style={{
                                    background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                                    color: 'white' // Set the text color
                                }} >
                                    Login
                                </Button>
                            </Stack>  
                        </Col>
                        
                        {/* Signup */}
                        <Col xs={12} md={12}>   
                            <Stack gap={1} style={{ padding:"20px", marginBottom:"20px" }} className={`d-flex justify-content-center align-items-center`}> 
               
                                <div className="text" 
                                style={{
                                    backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                                    WebkitBackgroundClip: 'text',
                                    color: 'transparent',
                                    display: 'inline',
                                    textAlign: "center",
                                    whiteSpace: "nowrap"
                                }}>Dont have a account ? </div>

                                <a className="text"  href='/Signup'> <strong> Create now! </strong></a>
                            
                            </Stack>  
                        </Col>

                    </Row>

                </Container>
            </Container>
        </Container>
    )
}


export default LoginForm