import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';
import Card from '../Card';

function VigenereDecrypt() {
    const [response, setResponse] = useState({})
    const [ciphertext, setCiphertext] = useState({
        text: "",
        key: "",
        key_length: null
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setCiphertext({
            ...ciphertext,
            [name]: value
        });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        // const path = 'http://127.0.0.1:5000/vigenere_decrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/vigenere_decrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                text: ciphertext.text,
                key: ciphertext.key,
                key_length: ciphertext.key_length
            }
        })
            .then(response => {
                console.log("SUCCESS", response)
                setResponse(response)
            }).catch(error => {
                console.log(error)
                setResponse("ERROR")
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
                            name="text"
                            id="cipher-text"
                            value={ciphertext.text}
                            onChange={handleChange} />
                    </label>
                </div>
                <div>
                    <label htmlFor="">Key:
                        <input
                            type="text"
                            name="key"
                            id="key-value"
                            value={ciphertext.key}
                            onChange={handleChange} />
                    </label>
                </div>
                <div>
                    <label htmlFor="">Key Length:
                        <input
                            type="number"
                            pattern='[0-9]'
                            name="key_length"
                            id="key-num"
                            value={ciphertext.key_length}
                            onChange={handleChange} />
                    </label>
                </div>
                <Button name={'Decrypt'} />
            </form>

            <div className='text'>
                {response.status === 200 &&
                    <div>
                        <h4>Decrypted Text:</h4>
                        {JSON.parse(response.data.plaintext).map((decryption) =>
                            <Card text={decryption['text']} shiftKey={decryption['key']} key={decryption['text']} />)}
                    </div>}
                {response === "ERROR" &&
                    <div>
                        <p>Decryption failed :(</p>
                        <p>Likely due to a lack of memory on Heroku because I am too cheap to pay for it :)</p>
                    </div>}
            </div>
        </div>
    );
}

export default VigenereDecrypt;