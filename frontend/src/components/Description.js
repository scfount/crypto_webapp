import React, { Component } from 'react';

class Description extends Component {
    content = this.props.content || ':)';
    render() {
        return (
            <div>
                <p>
                    {this.content}
                </p>
            </div>
        );
    }
}

export default Description;