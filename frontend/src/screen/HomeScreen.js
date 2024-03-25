import React from "react";
import { Row, Col, Card } from "react-bootstrap";
import products from "../products";
import Product from "../components/Product";
import { propTypes } from "react-bootstrap/esm/Image";

function HomeScreen() {
  return (
    <div>
      <h1>Latest Products</h1>
      <Row>
        {products.map((product) => (
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
            <Product product={product} />
          </Col>
        ))}
      </Row>
    </div>
  );
}
export default HomeScreen;
