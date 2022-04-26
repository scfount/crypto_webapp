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
            <Description content={decryption_info} />
            <div className='Ciphers'>
                <ShiftEncrypt />
                <ShiftDecrypt />
            </div>

        </div>
    );
}
const description = "Shift Cipher is a simple substitution cipher that translates\
 each letter of the alphabet into a number: A = 0 ... Z = 25, adds the specified key\
 as the shift, then translates that new number back to a new letter within modulus\
 26."

const decryption_info = "Auto-Decryption: Leave key blank if not known."

export default Shift;