import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';
import Card from '../Card';

function AffineDecrypt() {
    const [response, setResponse] = useState({})
    const [ciphertext, setCiphertext] = useState({
        text: "",
        alpha: "",
        beta: ""
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
        // const path = 'http://127.0.0.1:5000/affine_decrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/affine_decrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                text: ciphertext.text,
                alpha: ciphertext.alpha,
                beta: ciphertext.beta
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
                    <label htmlFor="">Alpha:
                        <input
                            type="number"
                            pattern='[0-9]'
                            name="alpha"
                            id="alpha-num"
                            value={ciphertext.alpha}
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
                            value={ciphertext.beta}
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
                        <p>Decryption failed :( </p>
                        <p>Likely due to an alpha value that is not co-prime with 26.</p>
                    </div>}
            </div>
        </div>
    );
}

export default AffineDecrypt;