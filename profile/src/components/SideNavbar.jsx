import React, { Component } from 'react'
import { FaHome, FaRProject, FaFileContract, FaCog } from 'react-icons/fa'
import { GoArchive } from "react-icons/go";
import { GiAcidTube} from 'react-icons/gi'


export class SideNavbar extends Component {
    render() {
        return (
            <div className="SideNavbar">
                <ul>
                    <li><a href="#skillbox"><img src={process.env.PUBLIC_URL + "/static/images/shivansh-2.png"} alt="shivansh" /></a></li>
                    <li><a href="#"><FaHome className="icons" color="green" size="1.7em" />Home</a></li>
                    <li><a href="#skillbox"><GiAcidTube className="icons" color="green" size="1.7em" />Skills</a></li>
                    <li><a href="#Projects"><FaRProject className="icons" color="green" size="1.7em" />Projects</a></li>
                    <li><a href="#Contact"><FaFileContract className="icons" color="green" size="1.6em" />Contact</a></li>
                    <li><a href="#settings"><FaCog className="icons" color="green" size="1.6em" />Settings</a></li>
                </ul> 
            </div>
        )
    }
}

export default SideNavbar
