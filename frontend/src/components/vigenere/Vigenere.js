import React from 'react';
import '../../App.css';
import Description from '../Description';
import VigenereEncrypt from './VigenereEncrypt';
import VigenereDecrypt from './VigenereDecrypt';

function Vigenere() {

    return (
        <div className="Container">
            <h1>Vigenère Cipher</h1>
            <Description content={description} />
            <Description content={decryption_info} />
            <div className='Ciphers'>
                <VigenereEncrypt />
                <VigenereDecrypt />
            </div>


        </div>
    );
}

const description = "Vigenère Cipher is a polyalphabetic substitution cipher\
 that uses a repeated string as its key over the course of the text, referencing\
  a Vigenère table to encrypt/decrypt the text by substituting letters based on\
  their intersection in the Vigenère table with their corresponding key letter."

const decryption_info = "Auto-Decryption: Leave key length blank if not known or key is known."



export default Vigenere;