import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  // const [message, setMessage] = useState({})
  // const [ciphertext, setCiphertext] = useState({})
  const [plain_text, setPlainText] = useState({})
  // const [error, setErrorMessage] = useState({})


  useEffect(() => {
    // const path = 'http://127.0.0.1:5000/crypto'
    // const path = 'http://127.0.0.1:5000/shift_decrypt'
    const path = 'https://cryptography-web-application.herokuapp.com/shift_decrypt'

    axios({
      method: 'POST',
      url: path,
      data: {
        cipherText: 'ifmmp'
      }
    })
      .then(response => {
        console.log("SUCCESS", response)
        setPlainText(response)
      }).catch(error => {
        console.log(error)
      })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <h1>Cryptography Web App</h1>
        <div>{plain_text.status === 200 ?
          <h3>{plain_text.data.decryptions[1]}</h3>
          :
          <h3>Cryptic...Fail</h3>}
        </div>
      </header>

    </div>
  );
}

export default App;