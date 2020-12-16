import React, { Component } from 'react'

export class SideNavbar extends Component {
    render() {
        return (
            <div className="SideNavbar">
                <ul>
                    
                    <li><img src={process.env.PUBLIC_URL + "/static/images/shivansh.png"} alt="shivansh"/></li>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Skills</a></li>
                    <li><a href="#">Projects</a></li>
                    <li><a href="#">Others</a></li>
                </ul> 
            </div>
        )
    }
}

export default SideNavbar
