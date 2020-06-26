import React from 'react';
import { Route, BrowserRouter } from 'react-router-dom';

import Home from './pages/Home/index';
import Contact from './pages/Contact/index';

function Routes() {
    return (
        <BrowserRouter>
            <Route component={Home} path="/" exact />            
            <Route component={Contact} path="/contact" />            
        </BrowserRouter>
    );
};

export default Routes;