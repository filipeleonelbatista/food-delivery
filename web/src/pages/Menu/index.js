import React from 'react';
import './index.css';


import Navbar from '../../components/Navbar/Navbar';
import Footer from '../../components/Footer/Footer';

function Menu() {
    return (
        <>
            <Navbar />
            <div className="App">
                <header className="App-header">
                    <p>
                        Menu
                    </p>
                </header>
                <Footer />
            </div>
        </>
    );
}

export default Menu;
