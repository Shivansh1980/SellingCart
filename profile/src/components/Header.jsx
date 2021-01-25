import React, { Component } from 'react'
import { animateText } from '../animations'
import {FaCog} from 'react-icons/fa'
export class Header extends Component {
    componentDidMount() {
        animateText("heading","flipInX",3,10,true);
    }
    render() {
        return (
            <div className="Header">
                <h1 className="heading">
                    WELCOME TO MY PORTFOLIO!
                </h1>
            </div>
        )
    }
}

export default Header
