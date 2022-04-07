import { React, Component } from 'react';
import '../App.css';

class Card extends Component {
    text = this.props.text || 'text';
    key = this.props.shiftKey || null;
    render() {
        return (
            <div className='card'>
                <p>Text: {this.text.toUpperCase()}</p>
                {
                    (this.key != null) &&
                    <p>Key: {this.key}</p>
                }

            </div>
        );
    }
}

export default Card;