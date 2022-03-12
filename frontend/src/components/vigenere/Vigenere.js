import React, { useEffect, useState } from 'react';
import axios from 'axios'
import '../../App.css';
import VigenereEncrypt from './VigenereEncrypt';
import VigenereDecrypt from './VigenereDecrypt';

function Vigenere() {

    return (
        <div className="App">
            <header className="App-header">
                <h1>Vigenere Cipher</h1>
                <VigenereEncrypt />
                <VigenereDecrypt />
            </header>

        </div>
    );
}

export default Vigenere;