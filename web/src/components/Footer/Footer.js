import React from 'react';
import './Footer.css';

import { FaFacebookSquare, FaWhatsappSquare, FaPhoneSquare } from 'react-icons/fa';

function Footer() {
    const year = new Date().getFullYear();

    return (
        <footer>
            <p>&copy; {year} - FOOD Delivery - Simplificando a gestão de delivery</p>
            <p>Desenvolvido por <a href="https://leonelinformatica.com.br" target="_blank" rel="noopener noreferrer">Leonel Informática</a></p>
            <div className="social">
                <a href="https://google.com.br" target="_blank" rel="noopener noreferrer"> <FaFacebookSquare className="social-item" /> </a>
                <a href="https://google.com.br" target="_blank" rel="noopener noreferrer" > <FaWhatsappSquare className="social-item" /> </a>
                <a href="https://google.com.br" target="_blank" rel="noopener noreferrer" > <FaPhoneSquare className="social-item" /> </a>
            </div>

        </footer>
    );
}

export default Footer;
