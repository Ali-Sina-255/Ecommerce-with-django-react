import React from "react";
import { Navbar, Nav, Row, Container } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

function Header() {
  return (
    <header>
      <Navbar bg="dark" variant="dark" data-bs-theme="light" collapseOnSelect>
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand>ProShop</Navbar.Brand>
          </LinkContainer>

          <Nav className="mr-auto">
            <LinkContainer to="/cart">
              <Nav.Link>
                <i className="fas fa-shopping-cart"></i>Login
              </Nav.Link>
            </LinkContainer>

            <LinkContainer to="/login">
              <Nav.Link>
                <i className="fas fa-user"></i>Login
              </Nav.Link>
            </LinkContainer>
          </Nav>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;
