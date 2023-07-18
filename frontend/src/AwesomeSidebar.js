import React from 'react';
import './AwesomeSidebar.css'; // Stylesheet for the sidebar

const AwesomeSidebar = () => {
  return (
    <div className="sidebar">
      <h2>Awesome Sidebar</h2>
      <input type="text" placeholder="Enter something..." />
      <div className="button-group">
        <button>Button 1</button>
        <button>Button 2</button>
        <button>Button 3</button>
      </div>
    </div>
  );
};

export default AwesomeSidebar;
