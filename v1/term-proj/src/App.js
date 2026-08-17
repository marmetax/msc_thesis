import React from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';
import SoftwareEngineer from './nav/SoftwareEngineer';
import Client from './nav/Client';

function App() {
  return (
      <div className="App">
        <h1>Breast Cancer Prediction App</h1>
        <h1>Select a Profile:</h1>
        <div style={{ marginBottom: '10px' }}>
          <Button component={Link} to="/sofeng" variant="contained">
            Software Engineer
          </Button>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <Button component={Link} to="/client" variant="contained">
            Client
          </Button>
        </div>
      </div>
  );
}

export default App;