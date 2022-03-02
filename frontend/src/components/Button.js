import React, { Component } from 'react';

class Button extends Component {
    name = this.props.name || 'Submit';
    render() {
        return (
            <button>{this.name}</button>
        );
    }
}

export default Button;