import '../App.css';
import { React, Component } from 'react';
import Nav from './Nav';
import Shift from './shift/Shift';
import Vigenere from './vigenere/Vigenere';
import Affine from './affine/Affine';
import Description from './Description';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import crypto_img from './crypto_img.jpeg';

class HomePage extends Component {

    render() {
        return (
            <Router>
                <Nav />
                <Routes>
                    <Route path='/shift' element={<Shift />} />
                    <Route path='/vigenere' element={<Vigenere />} />
                    <Route path='/affine' element={<Affine />} />
                    <Route path='/' element={<Home />} />
                </Routes>
            </Router >
        );
    }
}

const Home = () => (
    <div id='homepage' className='Container'>
        <h1>Select a cipher above to begin!</h1>
        <Description content={description} />
        <img className='crypto_img' src={crypto_img} alt="Cryptography Image" />

    </div>

);

const description = "Built by Steven Fountain using React and Flask"

export default HomePage;