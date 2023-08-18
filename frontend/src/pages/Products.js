import React from 'react';
import './Products.css';
import { useNavigate } from 'react-router-dom';

function Products() {
  const navigate = useNavigate();
  
  const navigatetodatasource = () => {
    navigate(`/`);
  };

  return (
    <div className='products'>
  <div className='home-panels'>
    <div className='he'>
          <svg className='qwes' viewBox="0 0 960 300">
        <symbol id="s-text">
          <text textAnchor="middle" x="50%" y="80%">Code Converse</text>
        </symbol>

        <g className="g-ants">
          <use xlinkHref="#s-text" className="text-copy"></use>
          <use xlinkHref="#s-text" className="text-copy"></use>
          <use xlinkHref="#s-text" className="text-copy"></use>
          <use xlinkHref="#s-text" className="text-copy"></use>
          <use xlinkHref="#s-text" className="text-copy"></use>
        </g>
      </svg>
      </div>

      <div className="grid-containern">
        <div className="grid-itemn">
    <h1>Code Discovery</h1>     
    <div className="para-content"> 
    Natural language search surfaces internal libraries and existing patterns and returns accurate results in less time, making it a powerful alternative to slow keyword searches.</div> 
    </div>
    <div className="grid-itemn">
    <h1>Human Explanation</h1>      
   <div className="para-content"> Powered by static analysis, vector search, and AI, it understands your codebase in 5+ languages helps you move quickly through refs and defs.  </div>
   </div>
        <div className="grid-itemn">
    <h1>Customization</h1>      
    <div className="para-content">
    GPT-3.5-Turbo and GPT-4 are supported with a variety of base models coming soon
Edit the prompt to prevent hallucinations, maintain voice and format requirements
    .  </div>
    </div>
     <div className="grid-itemn">
    <h1>Lightning Fast Regex</h1>     
    <div className="para-content">
 The fastest way to precisely navigate to specific code, identifiers, paths and repos with regex..</div> 
    </div>
      </div>
</div>
<button  onClick={() => navigatetodatasource()} className="get-started">Get Started</button>
      
    </div>
  );
}

export default Products;