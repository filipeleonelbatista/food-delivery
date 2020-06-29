const express = require('express');

const HomeController = require('./controllers/HomeController');
const CategoryController = require('./controllers/CategoryController');
const OptionalController = require('./controllers/OptionalController');
const PaymentMethodController = require('./controllers/PaymentMethodController');
const ProductController = require('./controllers/ProductController');
const MenuController = require('./controllers/MenuController');

const routes = express.Router();

routes.get('/', HomeController.index);
routes.get('/category', CategoryController.index);
routes.get('/optional', OptionalController.index);
routes.get('/paymentMethod', PaymentMethodController.index);
routes.get('/product', ProductController.index);
routes.get('/product/:id', ProductController.show);
routes.get('/menu', MenuController.index);


module.exports = routes;