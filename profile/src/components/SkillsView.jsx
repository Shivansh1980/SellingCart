import React, { Component } from 'react'

export class SkillsView extends Component {
    state = {
        progress: 100,
        django: 80,
        djangorestframework: 70,
        python: 75,
        htmlcss: 90,
        android: 80
    }
    render() {
        return (
            <div id="skillbox" className="Skills">
                <h1 align="center">Skills</h1>
                <div className="Barbox">
                    <p>Django</p>
                    <div className="bar">
                        <div className="Django" style={{ width: this.state.django + "%" }}></div>
                        <p>80%</p>
                    </div>
                </div>
                <div className="Barbox">
                    <p>Django Rest Framework</p>
                    <div className="bar">
                        <div className="DjangoRestFramework" style={{ width: this.state.djangorestframework + "%" }}></div>
                        <p>70%</p>
                    </div>
                </div>
                <div className="Barbox">
                    <p>Python</p>
                    <div className="bar">
                        <div className="Python" style={{ width: this.state.python + "%" }}></div>
                        <p>75%</p>
                    </div>
                </div>
                <div className="Barbox" width="70%">
                    <p>HTML and CSS</p>
                    <div className="bar">
                        <div className="HtmlCss" style={{ width: this.state.htmlcss + "%" }}></div>
                        <p>90%</p>
                    </div>
                </div>
                <div className="Barbox">
                    <p>AndroidDevelopment</p>
                     <div className="bar">
                        <div className="AndroidDevelopment" style={{ width: this.state.android + "%" }}></div>
                        <p>80%</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default SkillsView
