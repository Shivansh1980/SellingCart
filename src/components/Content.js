import React, { Component } from 'react';
class Content extends Component {
    render() {
        return (
            <div>
                <h1>
                    this is text of content and rendering from Header
                </h1>
                <button onClick={this.props.childComponent}>Click Me</button>
            </div>
        )
    }
};
export default Content