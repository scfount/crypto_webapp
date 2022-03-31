import './App.css';
import React from 'react';
import Nav from './components/Nav';
import Shift from './components/shift/Shift';
import Vigenere from './components/vigenere/Vigenere';
import Affine from './components/affine/Affine';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Description from './components/Description';

function App() {

  return (
    <Router>
      <Nav />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/shift' element={<Shift />} />
        <Route path='/vigenere' element={<Vigenere />} />
        <Route path='/affine' element={<Affine />} />
      </Routes>
    </Router>
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