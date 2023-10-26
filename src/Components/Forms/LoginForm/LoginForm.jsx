import React from 'react'

// import styles of this component
import styles from '../Forms.module.css'

// validation
import { userSchema } from "../../../utils/Validation/Validation"

// import other pkgs
import { Button, Col, Container, FloatingLabel, Form, Image, Row, Stack } from 'react-bootstrap'

import LOGO from '../../../Images/Arash.jpg'

const LoginForm = () => {
    const [user, setUser] = React.useState({
        email: "",
        password: ""
      })

      const [error, setError] = React.useState({
        email: false,
        emailError: "",
        password: false,
        passwordError: ""
      })

// ****************** Login Details ****************** //
    const Email = (e) => {
        setUser({...user, email: e.target.value})
    }

    const Password = (e) => {
        setUser({...user, password: e.target.value})
    }

// ****************** LOGIN BUTTON ****************** //
    const Login = async () =>{
        try {
            await userSchema.validate({ email: user.email, password: user.password }, { abortEarly: false });
      
        
    //   LoginSession(user).then(result=>{
    //       console.log(result)
          
          setError({
            email: false,
            emailError: "",

            password: false,
            passwordError: ""
          });

    //   }).catch((error) => {
    //     console.log("error",error); // Error message

    //       setError({
    //         email: true,
    //         emailError: "",

    //         password: true,
    //         passwordError: error
    //       });

    //   });


        } catch (validationError) {

            // Extract specific error messages for email and password
            const emailError = validationError.inner.find((error) => error.path === 'email');
            const passwordError = validationError.inner.find((error) => error.path === 'password');

      // If validation errors occur
            setError({
                email: !!emailError,
                emailError: emailError && emailError.message,

                password: !!passwordError,
                passwordError: passwordError && passwordError.message
            });
      
        }

  }


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
                                className="">
                                    <Form.Control type="email" className={error.email && "text-danger"} placeholder="name@example.com" value={user.email} onChange={Email} />
                                </FloatingLabel>
                                {error.email && <div className="text-danger mb-3">{error.emailError}</div>}
                                
                            {/* Password */}
                                <FloatingLabel controlId="floatingPassword" label="Password">
                                    <Form.Control type="password" className={error.email && "text-danger"} placeholder="Password" value={user.password} onChange={Password} />
                                </FloatingLabel>
                     
                                <Form.Check // prettier-ignore
                                type="checkbox"
                                id="Show Password"
                                label="Show Password"
                                style={{ color: "rgb(61, 152, 154)", borderColor: "rgb(12, 14, 36)"}}
                                />

                                {error.password && <div className="text-danger">{error.passwordError}</div>}

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
                                }} 
                                onClick={Login}
                                >
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