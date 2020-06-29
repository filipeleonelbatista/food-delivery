import React, { useEffect, useState } from 'react';
import './index.css';

import { Link } from 'react-router-dom';

import api from '../../services/api';

import Navbar from '../../components/Navbar/Navbar';
import Footer from '../../components/Footer/Footer';

function Menu() {
    const [categories, setCategories] = useState([])
    const [items, setItems] = useState([])

    useEffect(() => {
        api.get('category').then(response => {
            setCategories(response.data);
        })
    }, []);

    useEffect(() => {
        api.get('product').then(response => {
            setItems(response.data);
        })
    }, []);
    
    return (
        <>
            <Navbar />
            <div className="body">
                <div className="categories">
                    <div className="categories-group">
                        {categories.map(cat => {
                            return (
                                <div key={cat.id} className="category-item">
                                    <div className="category-title">
                                        {cat.name}
                                    </div>
                                </div>
                            )
                        })}

                    </div>
                </div>
                <div className="cards mt-10">

                    {items.map(item => {
                        return (
                              <Link to={"/product/" + item.id}>
                                <div key={item.id} className="card-item ac">
                                    <div className="card-item-image">
                                        <img src={item.image} alt={item.name} />
                                    </div>
                                    <div className="card-item-col pg-10">
                                        <div className="card-item-title mt-10">
                                            {item.name}
                                        </div>
                                        <div className="card-item-description mt-10">
                                            {item.description}
                                        </div>
                                        <div className="card-item-row mt-10 ac">
                                            <div className="card-item-value">
                                                R$ {item.value}
                                            </div>
                                            <div className="card-item-value-discount ml-10 ">
                                                R$ {item.value}
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </Link>
                        );
                    })}

                </div>
            </div>
            <Footer />
        </>
    );
}

export default Menu;
