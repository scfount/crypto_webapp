import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';
import Card from '../Card';

function AffineEncrypt() {
    const [response, setResponse] = useState({})
    const [plaintext, setPlaintext] = useState({
        text: '',
        alpha: 0,
        beta: 0
    })

    const handleChange = (event) => {
        const { name, value } = event.target;
        setPlaintext({
            ...plaintext,
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
                text: plaintext.text,
                alpha: plaintext.alpha,
                beta: plaintext.beta
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
            <h3>Encryption</h3>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="">Plaintext:
                        <input
                            type="text"
                            name="text"
                            id="plaintext"
                            value={plaintext.text}
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
                            value={plaintext.alpha}
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
                            value={plaintext.beta}
                            onChange={handleChange} />
                    </label>
                </div>
                <Button name={'Encrypt'} />
            </form>

            <div className='text'>
                {response.status === 200 &&
                    <div>
                        <h4>Encrypted Text:</h4>
                        <Card text={response.data.ciphertext} shiftKey={null} key={response.data.ciphertext} />
                    </div>}
                {response === "ERROR" &&
                    <div>
                        <p>Encryption failed :( </p>
                        <p>Likely due to an invalid character in the text.</p>
                    </div>}
            </div>
        </div>
    );
}

export default AffineEncrypt;