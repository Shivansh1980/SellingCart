import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import SideNavbar from './components/SideNavbar';
import HomeView from './components/HomeView';
import SkillsView from './components/SkillsView'
import ContactView from './components/ContactView'
import ProjectView from './components/ProjectView'
import { useState } from 'react';

const projects = [
  {
    'name': 'Selling Cart (An Ecommerce Website)',
    'tech_used': 'Django, Django Rest Framework, React Js, HTML5 and CSS3',
    'link': 'https://github.com/Shivansh1980/SellingCart',
    'description':'',
    'imageurl':''
  },

  {
    'name': 'iCLOCK (Android App)',
    'tech_used': 'Android Studio, Java',
    'link': 'https://github.com/Shivansh1980/iCLOCK',
    'description': '',
    'imageurl':''
  },

  {
    'name': 'Document Coverter (Website)',
    'tech_used': 'Django, Django Rest Framework, Python, HTML5 and CSS3',
    'link': 'https://github.com/Shivansh1980/doc-converter',
    'description': '',
    'imageurl': ''
  }
]
function App() {

  var projectComponents = [];
  for (var i = 0; i < projects.length; i++) {
    projectComponents.push(<ProjectView project={projects[i]} />)
  }

  return (
    <div className="App">
      <SideNavbar></SideNavbar>
      <Header></Header>
      <main className="Main">
        <HomeView></HomeView>
        <SkillsView></SkillsView>
        <ContactView />
        <div className="Projects">
          <h1 align="center">PROJECTS</h1>
          <div className="ProjectView">
            { projectComponents}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
