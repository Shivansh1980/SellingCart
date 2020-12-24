import React, { Component } from 'react'

export class ProjectView extends Component {
    render() {
        return (
            <div className="project">
                <div className="project-header">
                    <h2>{this.props.project.name}</h2>
                    <img src={this.props.project.url} alt={this.props.project.name+"_pic"} />
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
