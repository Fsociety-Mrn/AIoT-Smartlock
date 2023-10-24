
// import styles of this component
import styles from '../Forms.module.css'

// import other pkgs
import { Button, Col, Container, FloatingLabel, Form, Image, Row, Stack } from 'react-bootstrap'

import LOGO from '../../../Images/Arash.jpg'

const RegisterForm = () => {
    return (
        <div>
            <Container fluid className={`${styles.container} d-flex justify-content-center align-items-center px-5`}>
                        {/* Login Form containers */}
                        <Container className={`${styles.LoginContainer} d-flex justify-content-center align-items-center bg-white`}>
                <Container>
                
                    <Row xs={12}>
                    
                        <Col xs={12} md={12} >
                            <Stack gap={1} style={{ padding:"20px" }} className={`d-flex justify-content-center align-items-center`}>
                            
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
                            <Stack gap={2}  className="col-md-10 mx-auto">

                                {/* Email */}
                                <FloatingLabel
                                controlId="floatingInput"
                                label="Email"
                                >
                                    <Form.Control type="email" placeholder="name@example.com"/>
                                </FloatingLabel>

                                {/* New Password */}
                                <FloatingLabel controlId="floatingPassword" label="New Password">
                                    <Form.Control type="password" placeholder="New Password" />
                                </FloatingLabel>

                                {/* Confirm Password */}
                                <FloatingLabel controlId="floatingPassword" label="Confirm Password">
                                    <Form.Control type="password" placeholder="Confirm Password" />
                                </FloatingLabel>

                            </Stack>
                        </Col>

                        <Row className="justify-content-center">
{/* Create Account */}
<Col xs={12} md={6} className="d-flex justify-content-center">

    <Button variant="primary"
      style={{
        background: 'white',
        color: 'rgb(61, 152, 154)',
        border: "2px solid rgb(61, 152, 154)",
        
      }}>
      Cancel
    </Button>


</Col>

{/* Create Account */}
<Col xs={12} md={6} className="d-flex justify-content-center">
<Button variant="primary"
      style={{
        background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
        color: 'white',
     
      }}>
      Create account
    </Button>

</Col>

               </Row>         
                        {/* Signup */}
                        <Col xs={12} md={12}>   
                            <Stack gap={1} style={{ padding:"20px" }} className={`d-flex justify-content-center align-items-center`}> 
               
                                <div className="text" 
                                style={{
                                    backgroundImage: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                                    WebkitBackgroundClip: 'text',
                                    color: 'transparent',
                                    display: 'inline',
                                    textAlign: "center",
                                    whiteSpace: "nowrap"
                                }}>Dont have a account ? </div>

                                <a className="text"  href='/'> <strong> Create now! </strong></a>
                            
                            </Stack>  
                        </Col>

                    </Row>

                </Container>
            </Container>
            </Container>
        </div>
    )
}


export default RegisterForm