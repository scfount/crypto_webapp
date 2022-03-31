import React from 'react';
import '../../App.css';
import Description from '../Description';
import ShiftEncrypt from './ShiftEncrypt';
import ShiftDecrypt from './ShiftDecrypt';

function Shift() {


    return (
        <div className="Container">
            <h1>Shift Cipher</h1>
            <Description content={description} />
            <div className='Ciphers'>
                <ShiftEncrypt />
                <ShiftDecrypt />
            </div>

        </div>
    );
}
const description = "Description for Shift"

export default Shift;