import '../App.css';
import React from 'react';
import { Link } from 'react-router-dom';

function Nav() {
    return (
        <nav>
            <div className='nav-links'>
                <Link className='link' to='/'>
                    <h3>Cryptography</h3>
                </Link>
                <div className='links'>
                    <Link className='link' to='/shift'>
                        <p>Shift</p>
                    </Link>
                    <Link className='link' to='/vigenere'>
                        <p>Vigenere</p>
                    </Link>
                    <Link className='link-end' to='/affine'>
                        <p>Affine</p>
                    </Link>
                </div>
            </div>
        </nav>
    );
}

export default Nav;