import '../App.css';
import React from 'react';
import { Link } from 'react-router-dom';

function Nav() {
    const navStyle = {
        color: 'white',
        textDecoration: 'none'
    };

    return (
        <nav>
            <Link style={navStyle} to='/'>
                <h3>Cryptography</h3>
            </Link>
            <ul className='nav-links'>
                <Link style={navStyle} to='/shift'>
                    <li>Shift</li>
                </Link>
                <Link style={navStyle} to='/vigenere'>
                    <li>Vigenere</li>
                </Link>
                <Link style={navStyle} to='/affine'>
                    <li>Affine</li>
                </Link>
            </ul>
        </nav>
    );
}

export default Nav;