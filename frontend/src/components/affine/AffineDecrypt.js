import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';

function AffineDecrypt() {
    const [decryptedText, setDecryptedText] = useState({})
    const [affineDecrypt, setAffineDecrypt] = useState({
        ciphertext: '',
        alpha: 0,
        beta: 0
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setAffineDecrypt({
            ...affineDecrypt,
            [name]: value
        });
    };


    const handleSubmit = (event) => {
        event.preventDefault();
        // const path = 'http://127.0.0.1:5000/affine_decrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/affine_decrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                ciphertext: affineDecrypt.ciphertext,
                alpha: affineDecrypt.alpha,
                beta: affineDecrypt.beta
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
        <div>
            <h3>Decryption</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="">Ciphertext:
                        <input
                            type="text"
                            name="ciphertext"
                            id="cipher-text"
                            value={affineDecrypt.ciphertext}
                            onChange={handleChange} />
                    </label>
                </div>
                <div>
                    <label htmlFor="">Alpha:
                        <input
                            type="number"
                            pattern='[0-9]'
                            name="alpha"
                            id="alpha-num"
                            value={affineDecrypt.alpha}
                            onChange={handleChange} />
                    </label>
                </div>
                <div>
                    <label htmlFor="">Beta:
                        <input
                            type="number"
                            pattern='[0-9]'
                            name="beta"
                            id="beta-num"
                            value={affineDecrypt.beta}
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

export default AffineDecrypt;