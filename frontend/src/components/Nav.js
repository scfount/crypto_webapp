import '../App.css';
import { React, Component } from 'react';
import { Link } from 'react-router-dom';

class Nav extends Component {
    render() {
        return (
            <nav>
                <div className='nav-links'>
                    <Link className='link home' to='/'>
                        <h3>Cryptography</h3>
                    </Link>
                    <div className='links'>
                        <Link className='link' to='/shift'>
                            <li>Shift</li>
                        </Link>
                        <Link className='link' to='/vigenere'>
                            <li>Vigenere</li>
                        </Link>
                        <Link className='link-end' to='/affine'>
                            <li>Affine</li>
                        </Link>
                    </div>
                </div>
            </nav >
        );
    }
}

export default Nav;