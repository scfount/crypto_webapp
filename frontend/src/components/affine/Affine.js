import React from 'react';
import '../../App.css';
import Description from '../Description';
import AffineDecrypt from './AffineDecrypt';
import AffineEncrypt from './AffineEncrypt';

function Affine() {

    return (
        <div className="Container">
            <h1>Affine Cipher</h1>
            <Description content={description} />
            <div className='Ciphers'>
                <AffineEncrypt />
                <AffineDecrypt />
            </div>

        </div>
    );
}

const description = "Description for Affine"

export default Affine;