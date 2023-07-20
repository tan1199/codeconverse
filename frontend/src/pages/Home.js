import React, { useState } from 'react';
import './Home.css';
import '../ChatPanel.css';
function Home() {

  const [showTextbox, setShowTextbox] = useState(false);

  const handleButtonClick = () => {
    setShowTextbox(true);
  };

  const handleSendClick = () => {
    // Handle the logic for sending the textbox content (e.g., display or process it)
    console.log('Sending:', textboxValue);
    // Reset the textbox and hide it after sending
    setTextboxValue('');
    setShowTextbox(false);
  };

  const [textboxValue, setTextboxValue] = useState('');

  const handleTextboxChange = (event) => {
    setTextboxValue(event.target.value);
  };

  return (
    <div className="home">
      <div>Build AI Chat Search For Product Copilots
With Mendable, you can seamlessly craft Product Copilots that empower your users in navigating and unlocking the full value of your products. These applications do not just enhance product exploration, they redefine it.
Why use Mendable AI Chat Search for Product Copilots?
There are a number of reasons top companies choose Mendable as their preferred AI Chat Search provider.

<p>Fully managed GUI ingestion & deployment</p>
<p>Support for the most popular data sources</p>
<p>Interchangable models (GPT 3.5, GPT 4, and more)</p>
<p>Model finetuning and chat insights</p>
<p>Prebuilt chat components, messaging bots, and API</p>
</div>

<div class="lds-ripple"><div></div><div></div></div><div className="button-container">
<div class="progress">
  <div class="progress-value"></div>
</div>
        <div className="row">
          <button className="send-button-home" onClick={() => handleButtonClick('Button 1')}>Button 1</button>
          <button className="send-button-home" onClick={() => handleButtonClick('Button 2')}>Button 2</button>
        </div>
        <div className="row">
          <button className="send-button-home" onClick={() => handleButtonClick('Button 3')}>Button 3</button>
          <button className="send-button-home" onClick={() => handleButtonClick('Button 4')}>Button 4</button>
        </div>
      </div>
<div className='input-container-home'>
      {showTextbox && (
        <div>
          <input
            type="text"
            placeholder="Add Repository.."
            value={textboxValue}
            onChange={handleTextboxChange}
            className='input-box-home'
          />
          <button onClick={handleSendClick} className="send-button-home">Upload</button>
        </div>
      )}
      </div>
    </div>
  );
}

export default Home;