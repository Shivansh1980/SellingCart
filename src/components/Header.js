import React, { Component } from 'react'
import Content from './Content'

class Header extends Component {
    constructor(props) {
        super(props)

        const { name } = this.props;
        this.state = {
            message: name
        }
        this.childComponet = this.childComponet.bind(this)
    }
    childComponet() {
        alert('Hey, I am written in Header.js and You have called me from Content.js by passing my method as parameter inside <content/>')
    }
    clickHandler() {
        this.setState({
            message : "Wait We Are Going On Next Page"
        })
    }
    render() {
        return (
            <div>
                <h1>We are inside Parent <br/>{this.state.message}</h1>
                <Content childComponent={this.childComponet}/>
                <button onClick={this.clickHandler.bind(this)}>Click To Change</button>
            </div>
        )
    }
}
export default Header