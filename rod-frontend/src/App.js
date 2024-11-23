import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import NavBar from './components/NavBar';
import HomeLink from './components/HomeLink';
import UploadActivities from './components/UploadActivities';
import Stats from './components/Stats';
import ActivityHistory from './components/ActivityHistory';

function App() {
  return (
    <Router>
      <NavBar />

      {/* stock pic for all pages */}
      <div style={{
        position: 'relative',
        height: '100vh',  
        overflow: 'hidden', 
      }}>
        <img 
          src="/images/uphillRun.jpg" 
          alt="Running Banner"
          style={{
            width: '100%', 
            height: '100%', 
            objectFit: 'cover', 
            objectPosition: 'center', 
            position: 'absolute', 
            top: 0,
            left: 0,
          }}
        />
        <div style={{
          position: 'absolute', 
          top: '25%', 
          left: '50%',
          transform: 'translate(-50%, -50%)',
          color: 'black',
          textAlign: 'center',
          zIndex: 1, 
        }}>
          <h1>RunningOnData Dashboard</h1>
        </div>
      </div>

      <nav style={{
        position: 'absolute', 
        bottom: '20px', 
        left: '50%',
        transform: 'translateX(-50%)',
        zIndex: 1, 
        textAlign: 'center', 
      }}>
        <Link to="/" style={{ color: 'white', margin: '10px' }}>Home</Link>
        <Link to="/upload" style={{ color: 'white', margin: '10px' }}>Upload</Link>
        <Link to="/stats" style={{ color: 'white', margin: '10px' }}>Stats</Link>
        <Link to="/history" style={{ color: 'white', margin: '10px' }}>History</Link>
      </nav>

      {/* routes to start with  */}
      <Routes>
        <Route path="/upload" element={<UploadActivities />} />
        <Route path="/stats" element={<Stats />} />
        <Route path="/history" element={<ActivityHistory />} />
      </Routes>
    </Router>
  );
}

export default App;