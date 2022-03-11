import React, { useEffect, useState } from 'react';
import '../App.css';
import ShiftEncrypt from './shift/ShiftEncrypt';
import ShiftDecrypt from './shift/ShiftDecrypt';

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