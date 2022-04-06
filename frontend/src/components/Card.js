import { React, Component } from 'react';

class Card extends Component {
    text = this.props.text || 'text';
    key = this.props.key || 'key';
    render() {
        return (
            <div>
                <p>{this.text}</p>
                <p>{this.key}</p>
            </div>
        );
    }
}

export default Card;