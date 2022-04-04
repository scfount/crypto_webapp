import '../App.css';
import React from 'react';
import Nav from './Nav';
import Shift from './shift/Shift';
import Vigenere from './vigenere/Vigenere';
import Affine from './affine/Affine';
import Description from './Description';
import { HashRouter as Router, Routes, Route } from 'react-router-dom'

function HomePage() {

    return (
        <Router>
            <Nav />
            <Routes>
                <Route path='/shift' element={<Shift />} />
                <Route path='/vigenere' element={<Vigenere />} />
                <Route path='/affine' element={<Affine />} />
                <Route path='/' element={<Home />} />
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

export default HomePage;