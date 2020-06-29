import React from 'react';
import logo from '../../assets/logo.svg';
import './Navbar.css';

import { NavLink, Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="Navbar">
            <div className="logo">
                <Link exact to="/" className="nav-title">
                    <img src={logo} className="Nav-logo" alt="logo" />
                    <p>FOOD Delivery</p>
                </Link>
            </div>
            <div className="menu-items">
                <ul>
                    <li><NavLink exact to="/" activeClassName="active" className="nav-item">Inicio</NavLink></li>
                    <li><NavLink activeClassName="active" className="nav-item" to="/menu">Menu</NavLink></li>
                    <li><NavLink activeClassName="active" className="nav-item" to="/contact">Contato</NavLink></li>
                    {/* <li><NavLink activeClassName="active" className="nav-item" to="#">Cadastre-se</NavLink></li> */}
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
