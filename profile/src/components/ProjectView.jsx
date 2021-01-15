import React, { Component } from 'react';
import AOS from 'aos';
export class ProjectView extends Component {
    componentDidMount() {
        AOS.init()
    }
    componentDidUpdate() {
        AOS.init()
    }
    render() {
        return (
            <div data-aos="fade-up" data-aos-duration="1500" className="project">
                <div className="project-header">
                    <h3>{this.props.project.name}</h3>
                    <br/>
                    <img src={this.props.project.imageurl} alt={this.props.project.name+"_pic"} />
                </div>
                <div className="project-description">
                    <p>
                        <span className="descriptions">Technology Used :</span> {this.props.project.tech_used}
                    </p>
                    <p>
                        <span className="descriptions">Description : </span> {this.props.project.description}
                    </p>
                </div>
            </div>
        )
    }
}
export default ProjectView
