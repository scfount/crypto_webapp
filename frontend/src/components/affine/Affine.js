import React from 'react';
import '../../App.css';
import Description from '../Description';
import AffineDecrypt from './AffineDecrypt';
import AffineEncrypt from './AffineEncrypt';

function Affine() {

    return (
        <div className="Container">
            <h1>Affine Cipher</h1>
            <Description />
            <AffineEncrypt />
            <AffineDecrypt />
        </div>
    );
}

export default Affine;