import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import { Link } from 'react-router-dom';
import './SideNavbar.css';
import { SidebarData } from './SidebarData';

import { IconContext } from 'react-icons';


function SideNavbar() {

  const [isOpen, setIsOpen] = useState(true);

  function menuBtnChange() {
    setIsOpen(!isOpen);
  }
  return (
  <>
    <div className={`sidebar ${isOpen ? 'open' : ''}`}>
      <div className="logo-details">
        <i className="bx bxl-c-plus-plus icon"></i>
        <div className="logo_name">Codeconverse</div>
  <button id="btn" onClick={menuBtnChange}>
       <FaIcons.FaBars size={10}  onClick={menuBtnChange} />
      </button>      </div>
      <ul className="nav-list">


             {SidebarData.map((item, index) => {
                                     return (
                              <li>
                                    <Link to={item.path}>



                                                <i className="bx bx-cog">{item.icon}</i>
                                                <span className="links_name">{item.title}</span>
                                             </Link>
                                              <span className="tooltip">{item.title}</span>
                                            </li>
                                     );
                                   })}
             </ul>
           </div>


    </>
  );
}

export default SideNavbar;