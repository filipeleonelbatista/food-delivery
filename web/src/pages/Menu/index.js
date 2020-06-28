import React, { useEffect, useState } from 'react';
import './index.css';

import api from '../../services/api';

import Navbar from '../../components/Navbar/Navbar';
import Footer from '../../components/Footer/Footer';

function Menu() {
    const [items, setItems] = useState([])
    useEffect(() => {
        api.get('product').then(response => {
            console.log(response.data);
            setItems(response.data);
        })
    }, []);


    return (
        <>
            <Navbar />
            <div className="body">
                <div className="categories">
                    <div className="categories-group">

                        <div className="category-item">
                            <div className="category-title">
                                Tudo
                            </div>
                        </div>

                        <div className="category-item">
                            <div className="category-title">
                                Item
                            </div>
                        </div>

                        <div className="category-item">
                            <div className="category-title">
                                Item
                            </div>
                        </div>

                        <div className="category-item">
                            <div className="category-title">
                                Item
                            </div>
                        </div>

                        <div className="category-item">
                            <div className="category-title">
                                Item
                            </div>
                        </div>

                    </div>
                </div>
                <div className="cards mt-10">

                    <div className="card-item ac">
                        <div className="card-item-image">
                            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1202&q=80" alt="" srcset="" />
                        </div>
                        <div className="card-item-col">
                            <div className="card-item-row ai jc-space ml-10">
                                <div className="card-item-title">
                                    Comida 1
                                </div>
                                <div className="card-item-value">
                                    R$ 10,00
                                </div>
                            </div>
                            <div className="card-item-description ml-10">
                                Hamburguer com tudo o que se pode desejar de mais gostoso neste mundo...
                                </div>
                        </div>
                    </div>

                    <div className="card-item ac">
                        <div className="card-item-image">
                            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1202&q=80" alt="" srcset="" />
                        </div>
                        <div className="card-item-col">
                            <div className="card-item-row ai jc-space ml-10">
                                <div className="card-item-title">
                                    Comida 1
                                </div>
                                <div className="card-item-value">
                                    R$ 10,00
                                </div>
                            </div>
                            <div className="card-item-description ml-10">
                                Hamburguer com tudo o que se pode desejar de mais gostoso neste mundo...
                                </div>
                        </div>
                    </div>

                    <div className="card-item ac">
                        <div className="card-item-image">
                            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1202&q=80" alt="" srcset="" />
                        </div>
                        <div className="card-item-col">
                            <div className="card-item-row ai jc-space ml-10">
                                <div className="card-item-title">
                                    Comida 1
                                </div>
                                <div className="card-item-value">
                                    R$ 10,00
                                </div>
                            </div>
                            <div className="card-item-description ml-10">
                                Hamburguer com tudo o que se pode desejar de mais gostoso neste mundo...
                                </div>
                        </div>
                    </div>

                    <div className="card-item ac">
                        <div className="card-item-image">
                            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1202&q=80" alt="" srcset="" />
                        </div>
                        <div className="card-item-col">
                            <div className="card-item-row ai jc-space ml-10">
                                <div className="card-item-title">
                                    Comida 1
                                </div>
                                <div className="card-item-value">
                                    R$ 10,00
                                </div>
                            </div>
                            <div className="card-item-description ml-10">
                                Hamburguer com tudo o que se pode desejar de mais gostoso neste mundo...
                                </div>
                        </div>
                    </div>

                    <div className="card-item ac">
                        <div className="card-item-image">
                            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1202&q=80" alt="" srcset="" />
                        </div>
                        <div className="card-item-col">
                            <div className="card-item-row ai jc-space ml-10">
                                <div className="card-item-title">
                                    Comida 1
                                </div>
                                <div className="card-item-value">
                                    R$ 10,00
                                </div>
                            </div>
                            <div className="card-item-description ml-10">
                                Hamburguer com tudo o que se pode desejar de mais gostoso neste mundo...
                                </div>
                        </div>
                    </div>

                </div>
            </div>
            <Footer />
        </>
    );
}

export default Menu;
