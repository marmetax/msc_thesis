// src/Client.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { TextField, Button, FormControl, InputLabel, Select, MenuItem } from '@mui/material';

import App from '../App';
import '../form_css.css';


const Client = () => {

  const [formData, setFormData] = useState({
    radius_mean: '',
    texture_mean: '',
    smoothness_mean: '',
    concave_points_mean: '',
    symmetry_mean: '',
  });

  const [responseData, setResponseData] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;

    // Check if the field is "Chest Pain level" and restrict it to the range of 0-3
    const floatValue = name === 'radius_mean' ? parseFloat(value) : value;

    setFormData((prevData) => ({
      ...prevData,
      [name]: floatValue,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Prepare the data to be sent to the backend API
    const requestData = {
      radius_mean: formData.radius_mean,
      texture_mean: formData.texture_mean,
      smoothness_mean: formData.smoothness_mean,
      concave_points_mean: formData.concave_points_mean,
      symmetry_mean: formData.symmetry_mean,
    };

    // Make the API call to the backend
    fetch('http://127.0.0.1:5000/api/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the backend
        setResponseData(data); // Store the response data in the component state
      })
      .catch((error) => {
        // Handle any errors that occur during the API call
        console.error('Error:', error);
      });

    // Reset the form fields after submission
    setFormData({
      radius_mean: '',
      texture_mean: '',
      smoothness_mean: '',
      concave_points_mean: '',
      symmetry_mean: '',
    });
  };

  return (
    <div className='form-container'>
      <h2>Please enter your information:</h2>
      <form onSubmit={handleSubmit}>
        <div>
        <label>Radius Mean(0.10-29.00)</label>
        <input
          type="number"
          name="radius_mean"
          value={formData.radius_mean}
          step="0.01"
          min="0.10"
          max="29.00"
          onChange={handleChange}
          required
          className="custom-input"
        />
        </div>
        <br />
        <div>
          <label>Texture Mean(0.10-40.00)</label>
          <input
              name="texture_mean"
              type="number"
              step="0.01"
              min="0.10"
              max="40"
              value={formData.texture_mean}
              onChange={handleChange}
              required
              className="custom-input"
          /> 
        </div>
        <br />
        <div>
          <label>Smoothness Mean(0.01-0.20)</label>
          <input
            type="number"
            step="0.01"
            min="0"
            max="0.20"
            name="smoothness_mean"
            value={formData.smoothness_mean}
            onChange={handleChange}
            required
            className="custom-input"
          />
        </div>
        <br />

        <div>
          <label>Concave Points Mean(0.0-0.30)</label>
          <input
            type="number"
            step="0.01"
            min= "0.00"
            max= "0.30"
            name="concave_points_mean"
            value={formData.concave_points_mean}
            onChange={handleChange}
            required
            className="custom-input"
          />
        </div>
        <br />

        <div>
          <label>Symmetry Mean(0.10-0.35)</label>
          <input
            type="number"
            min="0.10"
            max="0.35"
            step="0.01"
            name="symmetry_mean"
            value={formData.symmetry_mean}
            onChange={handleChange}
            required
            className="custom-input"
          />
        </div>
        <br />
        <div style={{marginLeft:80}}>
          <Button variant="contained" type="submit">Submit</Button>
          <Button component={Link} to="/" variant="contained">Home</Button>
        </div>
      </form>
      {responseData && (
        <div>
          <h2>Diagnostics</h2>
          <p style={{margin:10}}>{responseData}</p>
        </div>
      )}
    </div>
  );
};

export default Client;
