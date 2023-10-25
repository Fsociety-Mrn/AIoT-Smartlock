import React from 'react'

// import styles of this component
import styles from '../Forms.module.css'


// import other pkgs
import { Col, Container, Image, Row, Stack } from 'react-bootstrap'

import LOGO from '../../../Images/Arash.jpg'

const Loading = () => {
    return (
        <Container fluid className={`${styles.container} d-flex justify-content-center align-items-center`}>
            
   <Container>
                
                    <Row xs={12}>
                    
                        <Col xs={12} md={12} >
                            <Stack gap={1} style={{ padding:"20px", marginTop:"80px" }} className={`d-flex justify-content-center align-items-center`}>
                            
                            {/* Logo */}
                                <Image 
                                src={LOGO}
                                style={{ width: '100px', height: '100px' }}
                                roundedCircle />

                           </Stack> 
                        </Col>

                    </Row>


            </Container>
        </Container>
    )
}


export default Loading