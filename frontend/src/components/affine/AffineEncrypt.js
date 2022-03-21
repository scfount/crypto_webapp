import React, { useEffect, useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';

function AffineEncrypt() {
    const [encryptedText, setEncryptedText] = useState({})
    const [affineEncrypt, setAffineEncrypt] = useState({
        plaintext: '',
        alpha: 0,
        beta: 0
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setAffineEncrypt({
            ...affineEncrypt,
            [name]: value
        });
    };


    const handleSubmit = (event) => {
        event.preventDefault();
        // const path = 'http://127.0.0.1:5000/affine_encrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/affine_encrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                plaintext: affineEncrypt.plaintext,
                alpha: affineEncrypt.alpha,
                beta: affineEncrypt.beta
            }
        })
            .then(response => {
                console.log("SUCCESS", response)
                setEncryptedText(response)
            }).catch(error => {
                console.log(error)
            })
    }

    return (
        <div className="App">
            <h2>Encrypt</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="">Plaintext:
                        <input
                            type="text"
                            name="plaintext"
                            id="plain-text"
                            value={affineEncrypt.plaintext}
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
                            value={affineEncrypt.alpha}
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
                            value={affineEncrypt.beta}
                            onChange={handleChange} />
                    </label>
                </div>
                <Button name={'Encrypt'} />
            </form>

            <div>{encryptedText.status === 200 &&
                <div>
                    <h4>Encrypted Text:</h4>
                    <p>{encryptedText.data.ciphertext}</p>
                </div>}
            </div>

        </div>
    );
}

export default AffineEncrypt;