import React from 'react';
import './Footer.css';

import { FaFacebookSquare, FaWhatsappSquare, FaPhoneSquare } from 'react-icons/fa';

import { Link } from 'react-router-dom';

function Navbar() {
    const year = new Date().getFullYear();

    return (
        <footer>
            <p>&copy; {year} - FOOD Delivery - Simplificando a gestão de delivery</p>
            <p>Desenvolvido por <a href="#">Leonel Informática</a></p>
            <div className="social">
                <FaFacebookSquare className="social-item" />
                <FaWhatsappSquare className="social-item" />
                <FaPhoneSquare className="social-item" />
            </div>

        </footer>
    );
}

export default Navbar;
