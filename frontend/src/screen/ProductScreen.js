import React from 'react'
import { Col, Row, Image, ListGroup, Button, Card } from 'react-bootstrap'
import { Link, useParams } from 'react-router-dom'
import Rating from '../components/Rating'
import products from '../products'

function ProductScreen () {
    
  return (
    <div>
      <Link to='/' className='btn btn-light my-3'>
        Go Back
      </Link>
      <div>
       {products.name}
      </div>
    </div>

  )
}

export default ProductScreen
