import React, { useEffect, useState } from 'react';
import './index.css';

import api from '../../services/api';

import { FaPlus, FaMinus } from 'react-icons/fa';

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
                        <div className="plrb30 ">
                            <div className="row jcsb mb10">
                                <div className="title">{item.name}</div>
                                <div className="row aic">
                                    <div className="discount mlr10">R$ {item.value}</div>
                                    <div className="value">R$ {item.value}</div>
                                </div>
                            </div>
                            <div className="row mb10">
                                <div className="description">{item.description}</div>
                            </div>
                            <div className="col mtb20">
                                {opt.map(option => (
                                    <div className="row">
                                        <div className="item">
                                            <div className="col f1">
                                                <div className="item-title">
                                                    {option.name}
                                                </div>
                                                <div className="item-desc">
                                                    {option.description}
                                                </div>
                                            </div>
                                            <div className="row jcsb aic">
                                                <div className="item-value">
                                                    R$ {option.value}
                                                </div>
                                                <div className="item-select">
                                                    <button className="ripple"><FaPlus /></button>
                                                    <input type="text" value="0" />
                                                    <button className="ripple"><FaMinus /></button>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>

                        </div>
                        <div className="row aic jcc mb10">
                            <button className="add">Adicionad ao pedido</button>
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
