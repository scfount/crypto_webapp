import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';

function VigenereEncrypt() {
    const [encryptedText, setEncryptedText] = useState({})
    const [vigenereEncrypt, setVigenereEncrypt] = useState({
        plaintext: '',
        key: ''
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setVigenereEncrypt({
            ...vigenereEncrypt,
            [name]: value
        });
    };


    const handleSubmit = (event) => {
        event.preventDefault();
        // const path = 'http://127.0.0.1:5000/vigenere_encrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/vigenere_encrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                plaintext: vigenereEncrypt.plaintext,
                key: vigenereEncrypt.key
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
        <div>
            <h3>Encryption</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="">Plaintext:
                        <input
                            type="text"
                            name="plaintext"
                            id="plain-text"
                            value={vigenereEncrypt.plaintext}
                            onChange={handleChange} />
                    </label>
                </div>
                <div>
                    <label htmlFor="">Key:
                        <input
                            type="text"
                            name="key"
                            id="key-value"
                            value={vigenereEncrypt.key}
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

export default VigenereEncrypt;