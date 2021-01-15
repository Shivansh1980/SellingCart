import React, { Component } from 'react'

export class HomeView extends Component {
    render() {
        return (
            <div className="HomeView">
                <div className="ShivanshImage">
                    <img src={process.env.PUBLIC_URL + "/static/images/shivansh-2.png"} alt="shivansh" />
                    <h2 id="name" align="center">Shivansh Shrivastava</h2>
                </div>
                <p className="Introduction" align="center">
                    Hello, I am Shivansh Shrivastava.
                </p>
            </div>
        )
    }
}
export default HomeView
