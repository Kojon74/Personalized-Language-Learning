import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import Navbar from './components/CustomNavbar'
import Start from './components/Start'
import About from './components/About'
import Contact from './components/Contact'
import TermList from './components/TermList'
import './App.css';


function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Route exact path="/" component={Start} />
        <Route exact path="/about" component={About} />
        <Route exact path="/contact" component={Contact} />
        <Route exact path="/termlist" component={TermList} />
      </Router>
    </div>
  );
}

export default App;
