import React, { useEffect, useState } from "react";
import {
  Col,
  Row,
  Image,
  ListGroup,
  Button,
  Card,
  ListGroupItem,
} from "react-bootstrap";
import { Link, matchPath, useParams } from "react-router-dom";
import Rating from "../components/Rating";
import axios from "axios";
import products from "../products";
function ProductScreen() {
  // const params = useParams();
  // const product = products.find((p) => p._id === params.id);

  const [product, setProduct] = useState([]);
  const params = useParams()

  useEffect(() => {
    async function fetchProduct(){
      const {data} = await axios.get(`/api/product/${params.id}`)

      setProduct(data)
    }
    console.log(params)

  fetchProduct();

    // we will get cors error
    // corse-orgin resource sahring

  }, []);

  return (
    <div>
      <Link to="/" className="btn btn-light my-3">
        Go Back
      </Link>
      <div>
        <Row>
          <Col md={6}>
            <Image src={product.image} alt={product.name} fluid />
          </Col>
          <Col md={3}>
            <ListGroup variant="flush">
              <ListGroupItem>
                <h3>{product.name}</h3>
              </ListGroupItem>

              <ListGroupItem>
                <Rating
                  value={product.rating}
                  text={`${product.numReviews} reviews`}
                  color={"#f8e825"}
                />
              </ListGroupItem>
              <ListGroupItem>
               Price : ${product.price}
              </ListGroupItem>
              <ListGroupItem>
               Description : {product.description}
              </ListGroupItem>
            </ListGroup>
          </Col>

          <Col md={3}>
            <Card>
              <ListGroup variant="Flush">

                <ListGroupItem>
                  <Row>
                    <Col> Price: </Col>
                    <Col><strong>$ {product.price}</strong></Col>
                  </Row>
                </ListGroupItem>


                <ListGroupItem>
                  <Row>
                    <Col> Status: </Col>
                    <Col>{product.countInStock > 0 ? 'In Stock' : "Out of Stock"}</Col>
                  </Row>
                </ListGroupItem>
                
              </ListGroup>
              <ListGroup>
                <Button className="btn-block" disabled={product.countInStock===0} type="button">Add to card</Button>
              </ListGroup>
            </Card>
          </Col>
        </Row>
      </div>
    </div>
  );
}

export default ProductScreen;
