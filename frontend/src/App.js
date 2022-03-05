import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import Button from './components/Button';

function App() {
  const [encryptedText, setEncryptedText] = useState({})
  const [shiftEncrypt, setShiftEncrypt] = useState({
    plaintext: '',
    key: 0
  })

  const handleChange = (event) => {
    const { name, value } = event.target;
    setShiftEncrypt({
      ...shiftEncrypt,
      [name]: value
    });
  };


  const handleSubmit = (event) => {
    event.preventDefault();
    // const path = 'http://127.0.0.1:5000/shift_encrypt'
    const path = 'https://cryptography-web-application.herokuapp.com/shift_encrypt'
    axios({
      method: 'POST',
      url: path,
      data: {
        plaintext: shiftEncrypt.plaintext,
        key: shiftEncrypt.key
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
      <header className="App-header">
        <h1>Cryptography Web App</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="">Plaintext:
              <input
                type="text"
                name="plaintext"
                id="plain-text"
                value={shiftEncrypt.plaintext}
                onChange={handleChange} />
            </label>
          </div>
          <div>
            <label htmlFor="">Shift:
              <input
                type="number"
                pattern='[0-9]'
                name="key"
                id="key-num"
                value={shiftEncrypt.key}
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
      </header>

    </div>
  );
}

export default App;