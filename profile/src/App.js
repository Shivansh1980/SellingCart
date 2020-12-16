import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import SideNavbar from './components/SideNavbar';
import HomeView from './components/HomeView'
function App() {
  return (
    <div className="App">
      <Header></Header>
      <main className="Main">
        <SideNavbar></SideNavbar>
        <HomeView></HomeView>
      </main>
    </div>
  );
}

export default App;
