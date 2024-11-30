// src/components/UploadActivities.js
import React, { useState } from 'react';
import axios from 'axios';

const UploadActivities = () => {
  
  const [file, setFile] = useState(null);

  // get first file
  const handleFileChange = (e) => {
    setFile(e.target.files[0]); 
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      console.error("Please upload a file");
      return;
    }
    // append file 
    const formData = new FormData();
    formData.append('file', file); 


    try {
      const response = await axios.post('http://localhost:8000/upload_csv', formData, {
        headers: {
          'Content-Type': 'multipart/form-data' 
        }
      });
      console.log(response.data); 
      console.log('Uploading with POST', formData);

    } catch (error) {
      console.error("There was an error uploading the file!", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept=".csv" onChange={handleFileChange} required />
      <button type="submit">Upload Activities</button>
    </form>
  );
};

export default UploadActivities;
  