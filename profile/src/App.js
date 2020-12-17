import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import SideNavbar from './components/SideNavbar';
import HomeView from './components/HomeView';
import Skills, { SkillsView } from './components/SkillsView'
function App() {
  return (
    <div className="App">
      <SideNavbar></SideNavbar>
      <Header></Header>
      <main className="Main">
        <HomeView></HomeView>
        <SkillsView></SkillsView>
      </main>
    </div>
  );
}

export default App;
