import {NavLink} from 'react-router-dom';
import React, {Component} from 'react';
import Login from './Login'
import Character from './Character'
import Inventory from './Inventory'
import '../App.css';

class Nav extends Component {
  constructor (props){
        super(props);
        this.state = {

        }
      }

      render(){




  return(
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
    <div className="container-fluid" id="navContainer">
    <NavLink to="/">Game</NavLink>
    <NavLink to="/login/">Account</NavLink>
    <NavLink to="/character/">Character</NavLink>
    <NavLink to="/magic/">Magic</NavLink>
    <NavLink to="/inventory/">Inventory</NavLink>
    </div>
    </nav>
  );
}
}
export default Nav;
