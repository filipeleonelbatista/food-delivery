import React from 'react';
import logo from '../../logo.svg';
import './index.css';

import Navbar from '../../components/Navbar/Navbar';
import Footer from '../../components/Footer/Footer';

import Navbar from '../../components/Navbar';

function Default() {
    const year = new Date().getFullYear();
    return (
        <>
            <Navbar />
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <p>
                        Em breve uma solução para agilizar seu negócio
                    </p>
                    <a
                        className="App-link"
                        href="https://leonelinformatica.com.br"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Saiba mais
                    </a>
                </header>
                <Footer />
            </div>
        </>
    );
}

export default Default;
