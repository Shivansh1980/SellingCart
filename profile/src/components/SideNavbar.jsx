import React, { Component } from 'react'
import { FaHome, FaRProject, } from 'react-icons/fa'
import { GoArchive } from "react-icons/go";
import { GiAcidTube} from 'react-icons/gi'


export class SideNavbar extends Component {
    render() {
        return (
            <div className="SideNavbar">
                <ul>
                    <li><img src={process.env.PUBLIC_URL + "/static/images/shivansh.png"} alt="shivansh"/></li>
                    <li><FaHome className="icons" color="green" size="2em"/><a href="#">Home</a></li>
                    <li><GiAcidTube className="icons" color="green" size="2em" /><a href="#skillbox">Skills</a></li>
                    <li><FaRProject className="icons" color="green" size="2em"/><a href="#">Projects</a></li>
                    <li><GoArchive className="icons" color="green" size="2em"/><a href="#">Others</a></li>
                </ul> 
            </div>
        )
    }
}

export default SideNavbar
