import React, { useState } from 'react';
import './ShoppingCart.css';

import { FaShoppingBag } from 'react-icons/fa';

function Navbar() {
    const [counter, setCounter] = useState(0)

    function counterAdd() {
        setCounter(...counter + 1);
    }
    function showBag() {
        const bag = document.getElementById('bag');
        bag.classList.toggle('hide');
    }
    return (
        <>
            <div className="nav-item nav-bag" onClick={showBag}>
                <FaShoppingBag size={16} color="#FFF" />
                {counter > 0 ? (<div className="items-buy">{counter}</div>) : ("")}
            </div>
            <div id="bag" className="hide floating-list">
                {
                    counter === 0 ? (
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

export default Navbar;

