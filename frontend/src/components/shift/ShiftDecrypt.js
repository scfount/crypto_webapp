import React, { useEffect, useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';

function ShiftDecrypt() {
    const [decryptedText, setDecryptedText] = useState({})
    const [shiftDecrypt, setShiftDecrypt] = useState({
        plaintext: '',
        key: 0
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setShiftDecrypt({
            ...shiftDecrypt,
            [name]: value
        });
    };


    const handleSubmit = (event) => {
        event.preventDefault();
        // const path = 'http://127.0.0.1:5000/shift_encrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/shift_decrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                ciphertext: shiftDecrypt.ciphertext,
                key: shiftDecrypt.key
            }
        })
            .then(response => {
                console.log("SUCCESS", response)
                setDecryptedText(response)
            }).catch(error => {
                console.log(error)
            })
    }

    return (
        <div className="App">
            <h2>Decrypt</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="">Ciphertext:
                        <input
                            type="text"
                            name="ciphertext"
                            id="cipher-text"
                            value={shiftDecrypt.ciphertext}
                            onChange={handleChange} />
                    </label>
                </div>
                <div>
                    <label htmlFor="">Key:
                        <input
                            type="number"
                            pattern='[0-9]'
                            name="key"
                            id="key-num"
                            value={shiftDecrypt.key}
                            onChange={handleChange} />
                    </label>
                </div>
                <Button name={'Decrypt'} />
            </form>

            <div>{decryptedText.status === 200 &&
                <div>
                    <h4>Decrypted Text:</h4>
                    <p>{decryptedText.data.plaintext}</p>
                </div>}
            </div>

        </div>
    );
}

export default ShiftDecrypt;