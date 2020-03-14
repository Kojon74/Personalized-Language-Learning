import React, { Component } from 'react'
import { Navbar, Nav } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import './CustomNavbar.css'

export default class CustomNavbar extends Component {
  render() {
    return (
      <div className="navbar">
        <Navbar className="navbar-container">
          <Nav.Item>
            <Nav.Link className="URLearning" href="/" eventKey="1">URLearning</Nav.Link>
          </Nav.Item>
          <div className="link-container">
            <Link className="links" to="/about">About</Link>
            <Link className="links" to="/contact">Contact</Link>
          </div>
          <div className="burger" onClick={this.toggleClass}>
            <div className="line1"></div>
            <div className="line2"></div>
            <div className="line3"></div>
          </div>
        </Navbar>
      </div>
    )
  }
}
