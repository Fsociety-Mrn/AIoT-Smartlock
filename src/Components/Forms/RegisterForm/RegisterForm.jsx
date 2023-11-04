
// import styles of this component
import styles from '../Forms.module.css'

// import other pkgs
import { Button, Col, Container, FloatingLabel, Form, Image, Row, Stack } from 'react-bootstrap'

// validation
import { SignUp_userSchema } from "../../../utils/Validation/Validation"

// Create ACCOUNT
import { createAccount } from "../../../utils/Firebase/Authentication/Authentication"

import LOGO from '../../../Images/Arash.jpg'
import React from 'react'

// Token Account
import TokenForm from './TokenForm'
import { useNavigate } from 'react-router-dom'

const RegisterForm = () => {


    // ********* FOR SETTING UP THE TOKEN ********* //

    const [tokenShow,setTokenShow] = React.useState(false)

    // ********* cREATE ACCOUNT ********* //

    const navigate = useNavigate()

    const [userDetails,setUserDetails] = React.useState({
        FirstName: "",
        LastName: "",
        Email : "",
        NewPassword:""
    })

    const [error, setError] = React.useState({
        firstName: false,
        firstNameError: "",

        lastName: false,
        lastNameError: "",

        email: false,
        emailError: "",

        password: false,
        passwordError: ""
    })


    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUserDetails((prevUser) => ({
          ...prevUser,
          [name]: value,
        }));
    };

    const createAccountss = async (event) => {
        try {
            await SignUp_userSchema.validate({ 
                FirstName: userDetails.FirstName, 
                LastName: userDetails.LastName,
                Email: userDetails.Email, 
                NewPassword: userDetails.NewPassword 
            }, { abortEarly: false });


            createAccount(
                userDetails.Email, 
                userDetails.NewPassword, 
                userDetails.LastName, 
                userDetails.FirstName).then(result=>{
                    console.log(result)
                    setError(
                        {
                            firstName: false,
                            firstNameError: "",
                    
                            lastName: false,
                            lastNameError: "",
                    
                            email: false,
                            emailError: "",
                    
                            password: false,
                            passwordError: ""
                          }
                    )

                    window.location.reload()
                })
      


        } catch (validationError) {

            // Extract specific error messages for email and password
            const firstnameError = validationError.inner.find((error) => error.path === 'FirstName');
            const lastnameError = validationError.inner.find((error) => error.path === 'LastName');
            const emailError = validationError.inner.find((error) => error.path === 'Email');
            const passwordError = validationError.inner.find((error) => error.path === 'NewPassword');

      // If validation errors occur
            setError({

                firstName: !!firstnameError,
                firstNameError: firstnameError && firstnameError.message,
        
                lastName: !!lastnameError,
                lastNameError: lastnameError && lastnameError.message,

                email: !!emailError,
                emailError: emailError && emailError.message,

                password: !!passwordError,
                passwordError: passwordError && passwordError.message
            });
      
        }
    }
    return (
        <div>
            {!tokenShow && <TokenForm setTokenShow={setTokenShow} />}

            {tokenShow && 
                <Container fluid className={`${styles.container} d-flex justify-content-center align-items-center px-2.5`}>
                    
                    {/* Reg Form containers */}
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
                                        }}>Create Account</div>

                                    </Stack> 
                                </Col>
                                
                                {/* Registration Form */}
                                <Col xs={12} md={12}>     
                                    <Stack gap={2} className="col-md-10 mx-auto">

                                        {/* First Name */}
                                        <FloatingLabel
                                        controlId="floatingInput"
                                        label="First Name"
                                        >
                                            <Form.Control 
                                            type="Text" 
                                            placeholder="First Name"
                                            name="FirstName"
                                            value={userDetails.FirstName}
                                            onChange={handleInputChange}
                                            />
                                        </FloatingLabel>
                                        {error.firstName && <div className="text-danger mb-3">{error.firstNameError}</div>}

                                        {/* Last Name */}
                                        <FloatingLabel controlId="floatingPassword" label="Last Name" >
                                            <Form.Control 
                                            type="Text" 
                                            placeholder="Last Name" 
                                            name="LastName"
                                            value={userDetails.LastName}
                                            onChange={handleInputChange}    
                                            />
                                        </FloatingLabel>
                                        {error.lastName && <div className="text-danger mb-3">{error.lastNameError}</div>}

                                        {/* Email */}
                                        <FloatingLabel
                                        controlId="floatingInput"
                                        label="Email"
                            
                                        >
                                            <Form.Control 
                                            type="email" 
                                            placeholder="name@example.com"
                                            name="Email"
                                            value={userDetails.Email}
                                            onChange={handleInputChange}     
                                            />
                                        </FloatingLabel>
                                        {error.email && <div className="text-danger mb-3">{error.emailError}</div>}

                                        {/* New Password */}
                                        <FloatingLabel controlId="floatingPassword" label="New Password">
                                            <Form.Control 
                                            type="password" 
                                            placeholder="New Password" 
                                            name="NewPassword"
                                            value={userDetails.NewPassword}
                                            onChange={handleInputChange}   
                                            />
                                        </FloatingLabel>
                                        {error.password && <div className="text-danger mb-3">{error.passwordError}</div>}

                                    </Stack>
                                </Col>
                                
                                {/* Buttons */}
                                <Col xs={12} md={11} style={{ marginTop:"15px", marginBottom:"100px"}} className='row row-cols-2 justify-content-center align-items-center'>
                                
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
                                        }}
                                        onClick={()=>navigate("/")}>
                                            Cancel
                                        </Button>
                                    </Col>

                                    {/* Create Account */}
                                    <Col xs={12} md={5} sm={12} className='row row-cols-1'>
                                        <Button 
                                        variant="primary"
                                        style={{
                                            background: 'linear-gradient(to right, rgb(61, 152, 154) 0%, rgb(12, 14, 36) 100%)',
                                            color: 'white',
                                            padding:"10px",
                                            borderRadius:"10px"
                                        }}
                                        onClick={createAccountss}
                                        >
                                            Sign Up
                                        </Button>
                                    </Col>
                            
                                </Col>

                            </Row>

                        </Container>
                    </Container>
                </Container>
            }
        </div>
    )
}


export default RegisterForm