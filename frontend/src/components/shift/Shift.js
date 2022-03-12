import React from 'react';
import '../../App.css';
import ShiftEncrypt from './ShiftEncrypt';
import ShiftDecrypt from './ShiftDecrypt';

function Shift() {


    return (
        <div className="App">
            <h1>Shift Cipher</h1>
            <ShiftEncrypt />
            <ShiftDecrypt />
        </div>
    );
}

export default Shift;