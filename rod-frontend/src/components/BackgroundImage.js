// src/components/BackgroundImage.js
import React from 'react';

imageUrl = '../images/cantonTrack.jpg'

const BackgroundImage = ({ imageUrl, children }) => {
  return (
    <div
      style={{
        backgroundImage: `url(${imageUrl})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        height: '400px', // You can adjust the height as needed
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: '#FFF',
        padding: '20px',
      }}
    >
      {children}
    </div>
  );
};

export default BackgroundImage;
