import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import './index.css';

import App from './App';
import SoftwareEngineer from './nav/SoftwareEngineer';
import Client from './nav/Client';
import reportWebVitals from './reportWebVitals';

const rootElement = document.getElementById('root');
ReactDOM.render(
  <BrowserRouter>
   <Routes>
    <Route exact path="/" element={<App/>} />
    <Route path="/sofeng" element={<SoftwareEngineer/>} />
    <Route path="/client" element={<Client/>} />
  </Routes>
  </BrowserRouter>,
  rootElement
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
