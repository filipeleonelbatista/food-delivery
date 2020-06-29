import React, { useEffect, useState } from 'react';
import './index.css';

import api from '../../services/api';

import Navbar from '../../components/Navbar/Navbar';
import Footer from '../../components/Footer/Footer';

function Menu(request) {
    const [product, setProduct] = useState([])
    const [opt, setOpt] = useState([])

    useEffect(() => {
        api.get('product/' + request.match.params.id).then(response => {
            setProduct(response.data.prod);
            setOpt(response.data.opt);
        })
    }, [request.match.params.id]);

    return (
        <>
            <Navbar />
            <div className="body">
                {product.map(item => (

                    <div key={item.id} className="product">
                        <div className="product-image">
                            <img src={item.image} alt={item.name} />
                        </div>
                        <div className="row">
                            <div className="title">{item.name}</div>
                            <div className="value">R$ {item.value}</div>
                        </div>
                        <div className="row">
                            <div className="description">{item.description}</div>
                        </div>
                        <div className="col">
                            {opt.map(option => (
                                <div className="row">
                                    <div className="item">
                                        <div className="col">
                                            <div className="item-title">
                                                {option.name}
                                            </div>
                                            <div className="item-desc">
                                                {option.description}
                                            </div>
                                        </div>
                                        <div className="item-value">
                                            {option.value}
                                        </div>
                                        <div className="item-select">
                                            <input type="checkbox" />
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>

                    </div>
                )
                )}
            </div>
            <Footer />
        </>
    );
}

export default Menu;
