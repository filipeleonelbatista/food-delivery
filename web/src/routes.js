import React from 'react';
import { Route, BrowserRouter } from 'react-router-dom';

import Home from './pages/Home/index';
import Contact from './pages/Contact/index';
import Menu from './pages/Menu/index';
import Product from './pages/Product/index';

function Routes() {
    return (
        <BrowserRouter>
            <Route component={Home} path="/" exact />            
            <Route component={Menu} path="/menu" />            
            <Route component={Product} path="/product/:id" />            
            <Route component={Contact} path="/contact" />            
        </BrowserRouter>
    );
};

export default Routes;