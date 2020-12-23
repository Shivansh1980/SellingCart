import React, { Component } from 'react'

export class ProjectView extends Component {
    render() {
        return (
            <div>
                <iframe src={process.env.PUBLIC_URL + "/static/images/shivansh-2.png"} frameborder="0"></iframe>
            </div>
        )
    }
}
export default ProjectView
