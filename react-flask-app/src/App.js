import logo from './logo.svg';
import './App.css';
import suggestedRecipe from './pages/suggestedRecipe';

function App() {
  return (
      <div className="App">
        <header className="bg">
          <div className="topnav">
            <a href="#news">News</a>
            <a href="#contact">Contact</a>
            <a href="#about">About</a>
            <a href="#home" class="active">Home</a>
            <a href="javascript:void(0);" class="icon" onclick="myFunction()">
              <i class="fa fa-bars"></i>
            </a>

          </div>
          <div id="box">
            <h1 className="title">EcoEats</h1>
            <div className="button-container">
              <a href="/suggestedRecipe" className="box-button">Menu</a>
              <a href="/contact" className="box-button">Contact</a>
            </div>
          </div>
        </header>
      </div>
  );
}

export default App;
