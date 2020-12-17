import React, { Component } from 'react'

export class SkillsView extends Component {
    state = {
        progress: 100,
        django: 80,
        djangorestframework: 70,
        python: 75,
        htmlcss: 90,
        android: 80,
        cpp: 90,
        competitive: 50,
        kalilinux:70
    }
    render() {
        return (
            <div>
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

                <div id="skillbox-2" className="Skills">
                    <h1 align="center">Other Skills</h1>
                    <div className="Barbox">
                        <p>C++</p>
                        <div className="bar">
                            <div className="C++" style={{ width: this.state.cpp + "%" }}></div>
                            <p>90%</p>
                        </div>
                    </div>
                    <div className="Barbox">
                        <p>Competitive Programing</p>
                        <div className="bar">
                            <div className="Competitive" style={{ width: this.state.djangorestframework + "%" }}></div>
                            <p>50%</p>
                        </div>
                    </div>
                    <div className="Barbox">
                        <p>Ethical Hacking</p>
                        <div className="bar">
                            <div className="EthicalHacking" style={{ width: this.state.python + "%" }}></div>
                            <p>66%</p>
                        </div>
                    </div>
                    <div className="Barbox" width="70%">
                        <p>Kali Linux</p>
                        <div className="bar">
                            <div className="Kalilinux" style={{ width: this.state.kalilinux + "%" }}></div>
                            <p>70%</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default SkillsView
