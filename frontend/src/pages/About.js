import React, { useState, useEffect } from 'react';
import './About.css';
import aa from "../images/cc.gif";
const App = () => {
    useEffect(() => {
    // Add the event listener to remove the scrollbar when the component mounts
    document.body.style.overflow = 'hidden';

    // Clean up the event listener when the component unmounts
    return () => {
      document.body.style.overflow = 'visible';
    };
  }, []); 
  return (
    <div className="about" style={{ backgroundImage: `url(/124.jpg)`,backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat', }}>
      <div className='about-info'>Coming Soon</div>
            <div className='test-info'></div>

            {/* <img src={aa} alt="My GIF" style={{ width: '1300px', height: '180px' }} /> */}

      </div>
  );
};

export default App;