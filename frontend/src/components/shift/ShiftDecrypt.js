import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';

function ShiftDecrypt() {
    const [decryptedText, setDecryptedText] = useState({})
    const [shiftDecrypt, setShiftDecrypt] = useState({
        ciphertext: "",
        key: ""
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setShiftDecrypt({
            ...shiftDecrypt,
            [name]: value
        });
    };

    const getDecryptions = (path) => {
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

    const handleSubmit = (event) => {
        event.preventDefault();
        if (shiftDecrypt.key == "") {
            // const path = 'http://127.0.0.1:5000/shift_decrypt_no_key'
            const path = 'https://cryptography-web-application.herokuapp.com/shift_decrypt_nokey'
            getDecryptions(path)
        }

        else {
            // const path = 'http://127.0.0.1:5000/shift_decrypt'
            const path = 'https://cryptography-web-application.herokuapp.com/shift_decrypt'
            getDecryptions(path)
        }
    }

    return (
        <div>
            <h3>Decryption</h3>
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

            <div className='text'>{decryptedText.status === 200 &&
                <div>
                    <h4>Decrypted Text:</h4>
                    <p>{decryptedText.data.plaintext}</p>
                </div>}
            </div>

        </div>
    );
}

export default ShiftDecrypt;