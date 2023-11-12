import React, { useState } from 'react';
import './Customize.css';

function Customize({ isFilterToggleOn,onFilterToggleChange,isRerankToggleOn,onRerankToggleChange,handleApiKeyChange,handlePromptChange,userInfo }) {

  const [isOpen, setIsOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);
  const [prompt, setPrompt] = useState('');
  const [apikey, setApikey] = useState('');

const handlePrompt = (e) => {
  setPrompt(e.target.value);
};
const handleKeyChange = (e) => {
  setApikey(e.target.value);
};

const handlePromptKeyDown = (e) => {
  if (e.keyCode === 13) {
    e.preventDefault();
  }
  if (e.key === 'Enter' && prompt.trim() !== '') {
    handlePromptChange(prompt);
    setPrompt('');
  }
};
const handleApiKeyDown = (e) => {
  if (e.keyCode === 13) {
    e.preventDefault();
  }
  if (e.key === 'Enter' && apikey.trim() !== '') {
    handleApiKeyChange(apikey);
    setApikey('');
  }
};
  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  const handleOptionClick = (option) => {
    setSelectedOption(option);
    setIsOpen(false);
  };

  const options = [
    { value: 'option1', label: 'GPT-3-16K' },
    { value: 'option2', label: 'GPT-3' },
    { value: 'option3', label: 'GPT-4' },
  ];
  
  return (
    <div className='ModelConfig' style={{ backgroundImage: `url(/888.jpg)`,backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat', }}>
    <div className="App">
      <div className="grid-container">
                <div className="grid-item2">  
        <h2> Profile</h2>
         <div className="profilecontainer">
      <div className="labelprofile">Username:</div>
           <div className="labelprofile">Email:</div>
           </div>
                   <div className="profilecontainer">
      <input type="text" className="inputprofile" value={userInfo.username.split('@')[0]} readOnly />

 
      <input type="text" className="inputprofile" value={userInfo.email.slice(0,25)} readOnly />
</div>
                   <div className="profilecontainer">
      <div className="labelprofile">Usage:</div>
           <div className="labelprofile">Api Key:</div>
           </div>
                              <div className="profilecontainer">
      <input type="text" className="inputprofile" value={userInfo.usage + ' tokens consumed'} readOnly /> 
              <input
        type="password"
        placeholder="sk-xxxxxxxxxxxxx👁️‍🗨️"
        value={apikey}
        onChange={handleKeyChange}
        onKeyDown={handleApiKeyDown}
        className="inputprofile"
        autoFocus
        rows={1} // Start with a single row
        // style={{ height: `${(prompt.split('\n').length + 1) * 30}px` }}
    
      />
      </div>

  </div>
        <div className="grid-item1">
          
<h2>Select a Model</h2>
          <div className="cool-dropdown">
      <div className="selected-option" onClick={toggleDropdown}>
        {selectedOption ? selectedOption.label : 'GPT-3-16K'}
        <span className={`arrow ${isOpen ? 'open' : ''}`}>&#9660;</span>
      </div>
      {isOpen && (
        <ul className="options">
          {options.map((option) => (
            <li
              key={option.value}
              className="option"
              onClick={() => handleOptionClick(option)}
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
    </div>


  <div className="grid-item3">  
        <h2> Custom Prompt</h2>
        {/* <input type="text"  className="custom-prompts" value='dsgsgfsdfsfds v dsgds' 
        onChange={handlePrompt}
        onKeyDown={handlePromptKeyDown}/> */}
        <textarea
        type="text"
        placeholder="Enter a custom prompt for the AI. Test the model after changing it for optimal performance ...."
        value={prompt}
        onChange={handlePrompt}
        onKeyDown={handlePromptKeyDown}
        className="custom-prompts"
        rows={1} // Start with a single row
        // style={{ height: `${(prompt.split('\n').length + 1) * 30}px` }}
    
      />
        </div>

        <div className="grid-item4">
          <h2>Retrieval Settings </h2>
          <div className='toggles'>
            <div>
        <div className="checkbox-wrapper-44">
          <div className="checkbox-wrapper-text">Metadata Filtering</div>
      <label className="toggleButton">
      <input type="checkbox" checked={isFilterToggleOn} onChange={onFilterToggleChange} />
              <div>
          <svg viewBox="0 0 44 44">
            <path d="M14,24 L21,31 L39.7428882,11.5937758 C35.2809627,6.53125861 30.0333333,4 24,4 C12.95,4 4,12.95 4,24 C4,35.05 12.95,44 24,44 C35.05,44 44,35.05 44,24 C44,19.3 42.5809627,15.1645919 39.7428882,11.5937758" transform="translate(-2.000000, -2.000000)"></path>
          </svg>
        </div>
      </label>
    </div>
    </div>
    <div>
        <div className="checkbox-wrapper-44">
     <div className="checkbox-wrapper-text">Cohere Rerank</div>
      <label className="toggleButton">
      <input type="checkbox" checked={isRerankToggleOn} onChange={onRerankToggleChange} />
              <div>
          <svg viewBox="0 0 44 44">
            <path d="M14,24 L21,31 L39.7428882,11.5937758 C35.2809627,6.53125861 30.0333333,4 24,4 C12.95,4 4,12.95 4,24 C4,35.05 12.95,44 24,44 C35.05,44 44,35.05 44,24 C44,19.3 42.5809627,15.1645919 39.7428882,11.5937758" transform="translate(-2.000000, -2.000000)"></path>
          </svg>
        </div>
      </label>
    </div>
    </div>
    </div>
        </div>
      </div>
    </div>

    </div>
  );
}

export default Customize;