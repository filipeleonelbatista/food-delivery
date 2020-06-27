import React from 'react';
import logo from '../../assets/logo.svg';
import './Navbar.css';

import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="Navbar">
            <div className="logo">
                <Link className="nav-title" to="/">
                    <img src={logo} className="Nav-logo" alt="logo" />
                    <p>FOOD Delivery</p>
                </Link>
            </div>
            <div className="menu-items">
                <ul>
                    <li><Link className="nav-item" to="/">Inicio</Link></li>
                    <li><Link className="nav-item" to="/menu">Menu</Link></li>
                    <li><Link className="nav-item" to="/contact">Contato</Link></li>
                    <li><Link className="nav-item" to="#">Cadastre-se</Link></li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
