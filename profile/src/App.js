import './App.css';
import BlackTheme from './components/ThemesAndLayouts/BlackTheme'
import { useEffect } from 'react';
import $ from 'jquery';

function App() {
  useEffect(() => {
    $(".Main").css("display", "flex");
  })

  return (
    <div className="App">
      <BlackTheme />
    </div>
  );
}

export default App;