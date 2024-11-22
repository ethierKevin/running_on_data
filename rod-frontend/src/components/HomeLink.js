// src/components/HomeLink.js
import React from 'react';
import { Link } from 'react-router-dom';

const HomeLink = () => (
  <Link to="/" style={{ textDecoration: 'none' }}>
    <h1 style={{ color: '#FFF' }}>Running On Data</h1>
  </Link>
);

export default HomeLink;