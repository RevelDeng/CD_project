import React, {useState} from 'react';
import ReactDOM from 'react-dom';

function cart_total() {
    const [total, setTotal] = useState("")

    // const updateTotal = () => {
    //     setTotal(previousState => {
    //         return {...previousState, total: }
    //     })
    // }

    return <p>Cart total: ${total}</p>
}

ReactDOM.render(
    <cart_total/>,
    document.getElementById('cart_total')
)