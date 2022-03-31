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

const description = "Affine Cipher is a monoalphabetic substitution cipher where\
 each letter is translated into a number using a mathematical function, then\
 translated back into a letter within modulus 26. The alpha value and size of\
 of the alphabet must be coprime, otherwise decryption may not be possible."

export default Affine;