import React from 'react';
import '../../App.css';
import Description from '../Description';
import VigenereEncrypt from './VigenereEncrypt';
import VigenereDecrypt from './VigenereDecrypt';

function Vigenere() {

    return (
        <div className="Container">
            <h1>Vigenere Cipher</h1>
            <Description content={description} />
            <div className='Ciphers'>
                <VigenereEncrypt />
                <VigenereDecrypt />
            </div>


        </div>
    );
}

const description = "Vigenere Cipher is a polyalphabetic substitution cipher\
 that uses a repeated word as its key over the course of the text, referencing\
  a Vigenere table to encrypt/decrypt the text."

export default Vigenere;