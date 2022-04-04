import './App.css';
import React from 'react';
import Nav from './components/Nav';
import Shift from './components/shift/Shift';
import Vigenere from './components/vigenere/Vigenere';
import Affine from './components/affine/Affine';
import { HashRouter } from 'react-router-dom'
import { BrowserRouter as Routes, Route } from 'react-router-dom';
import Description from './components/Description';

function App() {

  return (
    <HashRouter>
      <Nav />
      <Routes>
        <Route path='/shift' element={<Shift />} />
        <Route path='/vigenere' element={<Vigenere />} />
        <Route path='/affine' element={<Affine />} />
        <Route path='/' element={<Home />} />
      </Routes>
    </HashRouter>
  );
}

const Home = () => (
  <div className='Container'>
    <h1>Cryptography Web App</h1>
    <Description content={description} />
  </div>
);

const description = "This app was built using React and Flask"

export default App;