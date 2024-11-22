import express from 'express';
import axios from 'axios';
// const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello, frontend world!');
});

app.listen(port, () => {
  console.log(`Frontend running on http://localhost:${port}`);
});


// const axios = require('axios'); // you'll need to install axios
app.get('/api/data', async (req, res) => {
  try {
    const response = await axios.get('http://localhost:5000/your-flask-api-endpoint');
    res.json(response.data);
  } catch (error) {
    res.status(500).send('Error connecting to Flask backend');
  }
});