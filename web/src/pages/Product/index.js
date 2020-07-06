import React, { useEffect, useState } from 'react';
import './index.css';

import { Link } from 'react-router-dom';

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
    function addprod() {
        const item = document.getElementById("product-qtd");
        item.value = parseInt(item.value) + 1;
    }
    function removeprod() {
        const item = document.getElementById("product-qtd");
        if (parseInt(item.value) === 0) {
            item.value = 0;
        }
        if (parseInt(item.value) > 0) {
            item.value = parseInt(item.value) - 1;
        }
    }

    function addqtd(event) {
        const item = document.getElementById("opt-qtd-" + event.target.id);
        item.value = parseInt(item.value) + 1;
    }
    function removeqtd(event) {
        const item = document.getElementById("opt-qtd-" + event.target.id);
        if (parseInt(item.value) === 0) {
            item.value = 0;
        }
        if (parseInt(item.value) > 0) {
            item.value = parseInt(item.value) - 1;
        }
    }
    function handleAddToList(event) {
        let p = {
            id: product[0].id,
            id_category: product[0].id_category,
            image: product[0].image,
            name: product[0].name,
            value: product[0].value,
            description: product[0].description,
            quantity: document.getElementById("product-qtd").value
        }
        let o = {}


        for (var i = 0; i < opt.length; i++) {
            o[i] = {
                id: opt[i].id,
                id_product: opt[i].id_product,
                name: opt[i].name,
                value: opt[i].value,
                description: opt[i].description,
                quantity: document.getElementById("opt-qtd-" + opt[i].id).value
            }
        }


        let item = {
            p,
            o
        }

        console.log(item);
    }
    return (
        <>
            <Navbar />
            <div className="body">
                {product.map(item => (

                    <div key={item.id} className="product">
                        <div className="product-image">
                            <img src={item.image} alt={item.name} />
                        </div>
                        <div className="plrb30 mt10">
                            <div className="row jcsb mb10">
                                <div className="col">
                                    <div className="row mb10">
                                        <div className="title">{item.name}</div>
                                    </div>
                                    <div className="row mb10">
                                        <div className="description">{item.description}</div>
                                    </div>
                                </div>
                                <div className="col aic">
                                    <div className="row aic">
                                        <div className="discount mlr10">R$ {item.value}</div>
                                        <div className="value">R$ {item.value}</div>
                                    </div>

                                    <div className="item-select">
                                        <button onClick={addprod} className="ripple"><FaPlus /></button>
                                        <input id="product-qtd" type="text" value="1" />
                                        <button onClick={removeprod} className="ripple"><FaMinus /></button>

                                    </div>
                                </div>
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
                                                    <button id={option.id} onClick={addqtd} className="ripple"><FaPlus /></button>
                                                    <input id={"opt-qtd-" + option.id} type="text" value="0" />
                                                    <button id={option.id} onClick={removeqtd} className="ripple"><FaMinus /></button>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>

                        </div>
                        <div className="row aic jcc mb10">
                            <Link className="button-link" to="/menu">
                                <button onClick={handleAddToList} className="add">
                                    Adicionar ao pedido
                                </button>
                            </Link>
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
