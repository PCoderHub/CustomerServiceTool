import React from 'react';
import { Route, Routes } from 'react-router-dom';
import './App.css';
import AgentHome from './components/AgentHome';
import Home from './components/Home';
import Layout from './components/Layout';
import Login from './components/Login';
import MyTickets from './components/MyTickets';
import Register from './components/Register';
import UpdateTicket from './components/UpdateTicket';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route path='/' element={<Register />}></Route>
          <Route path='/login' element={<Login />}></Route>
          <Route path='/home' element={<Home />}></Route>
          <Route path='/agent' element={<AgentHome />}></Route>
          <Route path='/mytickets' element={<MyTickets />}></Route>
          <Route path='/edit' element={<UpdateTicket />} ></Route>
        </Route>
      </Routes>
    </div>
  );
}

export default App;


/*"eslintConfig": {
  "extends": [
    "react-app",
    "react-app/jest"
  ]
},*/