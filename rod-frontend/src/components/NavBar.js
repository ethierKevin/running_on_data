// src/components/NavBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Button, Typography } from '@mui/material';

<div style={{
  backgroundImage: 'trackSunset.webp', 
  backgroundSize: 'cover', 
  height: '400px', 
  display: 'flex', 
  justifyContent: 'center', 
  alignItems: 'center',
}}></div>

const NavBar = () => {
  return (
    <AppBar position="static" style={{ backgroundColor: '#1c9536' }}>
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 2 }}>
          Running On Data 
        </Typography>
        {/* <Button color="inherit" component={Link} to="/upload">Upload Activities</Button>
        <Button color="inherit" component={Link} to="/stats">Show Stats/Insights</Button>
        <Button color="inherit" component={Link} to="/history">Show Activity History</Button> */}
      </Toolbar>
    </AppBar>
    
  );
};

export default NavBar;
