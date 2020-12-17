import React, { Component } from 'react'

export class HomeView extends Component {
    render() {
        return (
            <div className="HomeView">
                <div className="ShivanshImage">
                    <img src={process.env.PUBLIC_URL + "/static/images/shivansh-2.png"} alt="shivansh" />
                    <h2 id="name" align="center">Shivansh Shrivastava</h2>
                </div>
                <p className="introduction" align="center">
                    <span className="text-info1">Hello, I am Shivansh <br/>Shrivastava.</span> <br />
                    <span className="text-info1">I am a student of B.Tech 3rd Year.</span>
                </p>
            </div>
        )
    }
}
export default HomeView
