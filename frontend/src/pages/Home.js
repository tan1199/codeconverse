import React, { useState } from 'react';
import './Home.css';
import * as AiIcons from 'react-icons/ai';
import * as MdIcons from 'react-icons/md'; 

import '../ChatPanel.css';
function Home({ values, processMessage, checkedValues, onCheckboxChange, handleAddDataSourceClick, handleFileUpload, progressbar,deletedatasource  }) {

  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    if (event.target.files[0]){
      // console.log('Uploading file:', event.target.files[0]);
      handleFileUpload(event.target.files[0])
      // setSelectedFile(null);
      // You can use fetch or any other library to upload the file to your server.
    } else {
      console.log('No file selected.');
    }
  };

// console.log("homey",progressbar);
const len=values.length;

  const [sourcetype, setSourcetype] = useState('');

  const handleButtonClick = (sourcetype) => {
    if((sourcetype==='Github')||(sourcetype==='Gitlab')||(sourcetype==='Code')){
      setSourcetype(sourcetype);
    }
  };

  const handleSendClick = () => {
    // Handle the logic for sending the textbox content (e.g., display or process it)
    // console.log('Sending:', datasourcevalue);
    // Reset the textbox and hide it after sending
    setdatasourcevalue('');
    setSourcetype('');
  };

  const [datasourcevalue, setdatasourcevalue] = useState('');

  const handleTextboxChange = (event) => {
    setdatasourcevalue(event.target.value);
    // console.log('current datasourcevalue is:', datasourcevalue);

  };

  const handleKeyDowndatasource = (e) => {
    if (e.keyCode === 13) {
      e.preventDefault();
    }
    if (e.key === 'Enter' && datasourcevalue.trim() !== '') {
      // console.log(datasourcevalue,sourcetype)
      handleAddDataSourceClick(datasourcevalue,sourcetype);
      setSourcetype('');
      setdatasourcevalue('')
    }
  };
  return (
    <div className="home" style={{ backgroundImage: `url(/124.jpg)`,backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat', }}>
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
{len ? (<div className="checkbox-list">
      <div className='checkbox-heading'>Saved Data Sources</div>
      {values.map((value, index) => (
        <div className='fl-wrap' key={index}>
        <div className="checkbox-wrapper" key={index}>
          <input className="inp-cbx" id={`cbx-${index}`}            
           type="checkbox"
            checked={checkedValues.includes(value)}
            onChange={() => onCheckboxChange(value)}
          />
          <label className="cbx" htmlFor={`cbx-${index}`}>
            <span className='cbb'>
              <svg width="1vw" height="1vh" viewBox="0 0 12 10">
                <polyline width="1vw" height="1vh" points="1.5 6 4.5 9 10.5 1"></polyline>
              </svg>
            </span>
            <div className='datasrc'>{value.length > 22 ? value.slice(0, 22) + '...' : value.substring(0, 22)}</div>
          </label>
        </div>
        <div className='del' onClick={() => deletedatasource(value)}><MdIcons.MdOutlineDeleteOutline color='beige'  size='2vw' /></div> 

        </div>
      ))}

    </div>):(<p className='parahome'>Your Data sources will appear here</p>)}
    </div>


<div className="button-container">
<div className="add-data-source">Add a Data Source</div>
        <div className="row">
          <button className="send-button-home1" onClick={() => handleButtonClick('Github')}>💽  Github Source</button>
          <button className="send-button-home1" onClick={() => handleButtonClick('Gitlab')}>💽  Gitlab source</button>
        </div>
        <div className="row">
        <button className="send-button-home1" onClick={() => handleButtonClick('Code')}>📼 Paste code</button>

          <button className="send-button-home1" onClick={() => {document.getElementById('fileInput').click();
                setSourcetype('');}}>📼 Archived Repository</button>
        </div>
        <div>
      <input
        id="fileInput"
        type="file"
        accept=".zip, .rs, .py, .java, .js, .cpp" // Specify the allowed file types
        style={{ display: 'none' }}
        onChange={handleFileChange}
      />

    </div>
      </div>
      </div>
<div >
      {sourcetype!=='' && (
        <div className='input-container-home'>
          <textarea
            type="text"
            placeholder="Add Repository.."
            value={datasourcevalue}
            onChange={handleTextboxChange}
            onKeyDown={handleKeyDowndatasource}
            className='input-box-home'
            autoFocus 
          />
          <button onClick = {() =>  {
          handleAddDataSourceClick(datasourcevalue,sourcetype);
          setSourcetype('');
          setdatasourcevalue('')
          }} className="send-button-home">Upload</button>

        </div>
      )}
      </div>
      {/* {progressbar && (<div className="lds-ripple"><div></div><div></div></div>)} */}
      {processMessage !=='' && (
      <div className='container'>
        <div className='inner-div'>{processMessage}</div>
        {/* <div className='inner-div'>fgdg</div> */}
        <div className='inner-div'>
          <span className="loadinginfo"></span>

        </div>
        {/* <div className='inner-div'><div className="lds-ripple"><div></div><div></div></div></div> */}
      </div>)}
      {/* <div className="container">
  <div className="inner-div">Div 1</div>
  <div className="inner-div">Div 2</div>
</div> */}

    </div>
  );
}

export default Home;