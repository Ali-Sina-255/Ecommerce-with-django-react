import React from 'react'
import { Container, Col, Row } from 'react-bootstrap'

function Footer() {
  return (
    <footer>
        <Container>
            <Row>
                <Col className='text-center'>
                Copyright &copy; Proshop
                </Col>
            </Row>
        </Container> 
    </footer>
  )
}

export default Footer