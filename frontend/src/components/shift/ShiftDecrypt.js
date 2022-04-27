import React, { useState } from 'react';
import axios from 'axios'
import '../../App.css';
import Button from '../Button';
import Card from '../Card';

function ShiftDecrypt() {
    const [response, setResponse] = useState({})
    const [ciphertext, setCiphertext] = useState({
        text: "",
        key: ""
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
        // const path = 'http://127.0.0.1:5000/shift_decrypt'
        const path = 'https://cryptography-web-application.herokuapp.com/shift_decrypt'
        axios({
            method: 'POST',
            url: path,
            data: {
                text: ciphertext.text,
                key: ciphertext.key
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
                            id="text"
                            value={ciphertext.text}
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
                            value={ciphertext.key}
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
                        <p>Not sure why, try something else.</p>
                    </div>}
            </div>
        </div>
    );
}

export default ShiftDecrypt;