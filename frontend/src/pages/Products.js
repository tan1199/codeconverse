import React from 'react';
import './Products.css';
import { useNavigate } from 'react-router-dom';

function Products({isAuthenticated}) {
  
  const navigate = useNavigate();
  
  const navigatetodatasource = () => {

    if(isAuthenticated){
    navigate(`/data`);
  }
  else{
        navigate(`/user`);
  }
  };
  return (
    <div className='products' style={{ backgroundImage: `url(/888.jpg)`,backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat', }}>
  <div className='home-panels'>
  <div className ='divhea' title="Code Converse">Code Converse</div>

      <div className="grid-containern">
        <div className="grid-itemn box">
    <h1>Code Discovery</h1>     
    <div className="para-content"> 
    Natural language search surfaces internal existing patterns and returns accurate results in less time, making it a powerful alternative to slow keyword searches.</div> 
    </div>
    <div className="grid-itemn box">
    <h1>Human Explanation</h1>      
   <div className="para-content"> Powered by static analysis, vector search, and AI, it understands your codebase in 5+ languages helps you move quickly through refs and defs.  </div>
   </div>
        <div className="grid-itemn box">
    <h1>Customization</h1>      
    <div className="para-content">
    GPT-3.5-Turbo and GPT-4 are supported with a variety of base models coming soon
Edit the prompt to prevent hallucinations, maintain voice and format requirements
    .  </div>
    </div>
     <div className="grid-itemn box">
    <h1>Lightning Fast Regex</h1>     
    <div className="para-content">
 The fastest way to precisely navigate to specific code, identifiers, paths and repos with regex..</div> 
    </div>
      </div>
</div>
<button  onClick={() => navigatetodatasource()} className="get-started">
<div className="waviy">
        <span style={{'--i': 1}}>G</span>
        <span style={{'--i': 2}}>e</span>
        <span style={{'--i': 3}} className="spaced-span">t</span>
        <span style={{'--i': 5}}>S</span>
        <span style={{'--i': 2}}>t</span>
        <span style={{'--i': 2}}>a</span>
        <span style={{'--i': 2}}>r</span>
        <span style={{'--i': 6}}>t</span>
        <span style={{'--i': 7}}>e</span>
        <span style={{'--i': 8}}>d</span>
      </div>
      </button>
  {/* <div className="loader">Generating...</div> */}
    </div>
  );
}

export default Products;