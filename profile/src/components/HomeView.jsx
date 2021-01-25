import React, { Component, useEffect } from 'react'
import {animateText} from '../animations'

export class HomeView extends Component {
    componentDidMount() {
        animateText("introduction","backInDown",5,5,true);
        animateText("name", "bounce", 3, 5, 15, true);
    }
    render() {
        return (
            <div className="HomeView">
                <div className="firstDiv">
                    <div className="ShivanshImage">
                        <img src={process.env.PUBLIC_URL + "/static/images/shivansh-2.png"} alt="shivansh" />
                        <h2 id="name" className="name" align="center">Shivansh Shrivastava</h2>
                    </div>
                    <p className="introduction" align="center">
                            Hello, I am Shivansh Shrivastava.
                    </p>
                </div>
                <div className="aboutMe" data-aos="animate-aboutme-text">
                    <h1>About Me</h1>
                    <p className="aboutMeText">
                        I’m proud of my ability to persevere and overcome challenges. 
                        This year I was having a hard time in trig, but I met with the
                        teacher outside of class and committed to studying for two hours
                        a day, and ended up with an A in the class. I’m also really 
                        passionate about my interests, especially writing and foreign 
                        languages
                    </p>
                </div>
            </div>
        )
    }
}
export default HomeView
