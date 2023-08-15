import React, { useState } from 'react';
import './Home.css';
import * as AiIcons from 'react-icons/ai';

import '../ChatPanel.css';
function Home({ values, checkedValues, onCheckboxChange, progressbar  }) {
console.log("homey",progressbar);
const len=values.length;

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
      <div>
{/* 
<p>Fully managed GUI ingestion & deployment</p>
<p>Support for the most popular data sources</p>
<p>Interchangable models (GPT 3.5, GPT 4, and more)</p>
<p>Model finetuning and chat insights</p>
<p>Prebuilt chat components, messaging bots, and API</p> */}
</div>
<div className="checkbox-btn">
<div className="checkbox-holder">
{!len && (
<p className='parahome'>Build AI Chat Search For Product Copilots With Mendable, you can seamlessly craft Product Copilots that empower your users in navigating and unlocking the full value of your products
  Build AI Chat Search For Product Copilots With Mendable, you can seamlessly craft Product and unlocking the full value of your products</p>)}
{len && (<div className="checkbox-list">
      {values.map((value, index) => (
        <div className="checkbox-wrapper" key={index}>
          <input className="inp-cbx" id={`cbx-${index}`}            
           type="checkbox"
            checked={checkedValues.includes(value)}
            onChange={() => onCheckboxChange(value)}
          />
          <label className="cbx" htmlFor={`cbx-${index}`}>
            <span>
              <svg width="12px" height="10px" viewBox="0 0 12 10">
                <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
              </svg>
            </span>
            <span>{value}</span>
          </label>
        </div>
      ))}
      {/* <div className="checkbox-wrapper" key={len}>
          <input className="inp-cbx" id={`cbx-${len}`}            
           type="checkbox"
          />
          <label className="cbx" htmlFor={`cbx-${len}`}>
            <span>
              <svg width="12px" height="10px" viewBox="0 0 12 10">
                <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
              </svg>
            </span>
            <span>metadata filter</span>
          </label>
        </div> */}
    </div>)}
    </div>


<div className="button-container">
{/* <div class="progress">
  <div class="progress-value"></div>
</div> */}
        <div className="row">
          <button className="send-button-home" onClick={() => handleButtonClick('Add Github Source')}>Add Github Source</button>
          <button className="send-button-home" onClick={() => handleButtonClick('Add Gitlab source')}>Add Gitlab source</button>
        </div>
        <div className="row">
          <button className="send-button-home" onClick={() => handleButtonClick('Add repository')}>Add repository</button>
          <button className="send-button-home" onClick={() => handleButtonClick('Paste code')}>Paste code</button>
        </div>
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
      {progressbar && (<div class="lds-ripple"><div></div><div></div></div>)}
    </div>
  );
}

export default Home;