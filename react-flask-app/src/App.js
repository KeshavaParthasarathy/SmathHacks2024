import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import suggestedRecipe from './suggestedRecipe';

function App() {
  return (
    <Router> {/* This is necessary to wrap your Routes */}
      <div className="App">
        <header className="bg">
          <div className="topnav">
            {/* Links here */}
          </div>
          <div id="box">
            <h1 className="title">EcoEats</h1>
            <div className="button-container">
              <Link to="/suggestedRecipe" className="box-button">Menu</Link>
              <Link to="/contact" className="box-button">Contact</Link>
            </div>
          </div>
        </header>
        <Routes>
          <Route path="/suggestedRecipe" element={<suggestedRecipe />} />
          {/* Define other routes here */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
