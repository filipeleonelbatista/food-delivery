import React, { useState } from 'react';
import './ShoppingCart.css';

import { FaShoppingBag } from 'react-icons/fa';



function ShoppingCart() {
    const [shoppingList, setShoppingList] = useState([])

    function addToList(item) {
        setShoppingList([...shoppingList, item]);
    }

    function showBag() {
        const bag = document.getElementById('bag');
        bag.classList.toggle('hide');
    }
    return (
        <>
            <div className="nav-item nav-bag" onClick={showBag}>
                <FaShoppingBag size={16} color="#FFF" />
                {shoppingList.length > 0 ? (<div className="items-buy">{shoppingList.length}</div>) : ("")}
            </div>
            <div id="bag" className="hide floating-list">
                {
                    shoppingList.length === 0 ? (
                        <>
                            <div className="col">
                                <div className="fl-item">
                                    <div className="fl-content-item">
                                        <div className="fl-item-qtd">1x</div>
                                        <div className="fl-item-name">Hamburger delicioso</div>
                                        <div className="fl-item-value">R$ 15,50</div>
                                    </div>
                                    <div className="fl-opt-title">Opcionais</div>
                                    <div className="opt">
                                        <div className="fl-opt-qtd">3x</div>
                                        <div className="fl-opt-name">Queijo</div>
                                        <div className="fl-opt-value">R$ 1,50</div>
                                    </div>
                                </div>
                            </div>
                            <div className="divider"></div>
                            <div className="col">
                                <div className="floating-list-footer">
                                    Ver pedido
                            </div>
                            </div>
                        </>
                    ) : (
                            <div className="col">
                                <div className="fl-no-item">
                                    Não há itens na sacola.
                            </div>
                            </div>
                        )
                }
            </div>
        </>
    );
}

export default ShoppingCart;

