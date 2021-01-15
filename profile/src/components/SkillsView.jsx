import React, { Component } from 'react'
import AOS from 'aos';

class SkillsView extends Component {
    componentDidMount() {
        AOS.init()
    }
    componentDidUpdate() {
        AOS.init()
    }

    state = {
        skills: {
            Django: 80,
            DjangoRestFramework: 70,
            Reactjs:60,
            Python: 75,
            HtmlCss: 90,  
        },
        otherSkills: {
            Android: 80,
            Cpp: 90,
            CompetitivePrograming: 50,
            EthicalHacking: 66,
            KaliLinux: 70
        }
    }
    render() {
        return (
            <div className="SkillSet">
                <div id="skillbox" data-aos="flip-left" data-aos-duration="2000" className="Skills">
                    <h1 align="center">Skills</h1>
                    {
                        Object.entries(this.state.skills).map(([name, value]) => (
                            <div className="Barbox">
                                <p>{name}</p>
                                <div className="bar">
                                    <div data-aos="animate-bar" data-aos-offset="100%" className={name} style={{ width: value + "%" }}></div>
                                    <p>{value + "%"}</p>
                                </div>
                            </div>
                        ))
                    }
                </div>

                <div id="skillbox-2" data-aos="flip-right" data-aos-duration="1500" className="Skills">
                    <h1 align="center">Other Skills</h1>
                    {
                        Object.entries(this.state.otherSkills).map(([name, value]) => (
                            <div className="Barbox">
                                <p>{name}</p>
                                <div className="bar">
                                    <div className={name} data-aos="animate-bar" data-aos-offset="100%" style={{ width: value + "%" }}></div>
                                    <p>{value + "%"}</p>
                                </div>
                            </div>
                        ))
                    }
                </div>
            </div>
        )
    }
}

export default SkillsView
