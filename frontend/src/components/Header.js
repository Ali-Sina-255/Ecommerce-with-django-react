import React from "react";
import { Navbar, Nav, Row, Container } from "react-bootstrap";

function Header() {
  return (
    <header>
      <Navbar bg="dark" variant="dark" data-bs-theme="light" collapseOnSelect>
        <Container>
          <Navbar.Brand href="/">ProShop</Navbar.Brand>
          <Nav className="mr-auto">
            <Nav.Link href="/"> <i className="fas fa-shopping-cart"></i>Cart</Nav.Link>
            <Nav.Link href="/login"><i className="fas fa-user"></i>Login</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;
