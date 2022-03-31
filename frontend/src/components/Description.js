import React, { Component } from 'react';

class Description extends Component {
    // name = this.props.name || 'Submit';
    render() {
        return (
            <div>
                <p>
                    This is a description of the [cipher name] cipher
                </p>
            </div>
        );
    }
}

export default Description;