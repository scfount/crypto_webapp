import React from 'react';
import '../../App.css';
import AffineDecrypt from './AffineDecrypt';
import AffineEncrypt from './AffineEncrypt';

function Affine() {

    return (
        <div className="App">
            <h1>Affine Cipher</h1>
            <AffineEncrypt />
            <AffineDecrypt />
        </div>
    );
}

export default Affine;