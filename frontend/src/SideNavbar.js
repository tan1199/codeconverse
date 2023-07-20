import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import { Link } from 'react-router-dom';
import './SideNavbar.css';
import ChatItem from './ChatItem';
import { SidebarData } from './SidebarData';

import { IconContext } from 'react-icons';


function SideNavbar({ chats, selectedChatId, handleChatItemClick, handleAddChatWindow }) {

  const [isOpen, setIsOpen] = useState(true);

  function menuBtnChange() {
    setIsOpen(!isOpen);
  }
  return (
  <>
    <div className={`sidebar ${isOpen ? 'open' : 'qq'}`}>
      <div className="logo-details">
        <i className="bx bxl-c-plus-plus icon"></i>

        <div className="logo_name">Codeconverse</div>
  <button id="btn" onClick={menuBtnChange}>
       <FaIcons.FaBars size={10}  onClick={menuBtnChange} />
      </button>      </div>
      <ul className="nav-list">
      <button id="btn" onClick={handleAddChatWindow}>Add New Chat Window</button>





      {isOpen ? (

<div className='conversationname'>
{chats.map((chat)=> {
                                     return (
                                      <li>
                                        <Link to={`/chats/${chat.chatId}`} >
                                      <i className="bx bx-cog"><AiIcons.AiFillHome /></i>

          <span className="links_name">
  <ChatItem
    key={chat.chatId}
    chat={chat}
    selectedChatId={selectedChatId}
    handleChatItemClick={handleChatItemClick}
  />
  </span>
  </Link>
  <span className="tooltip">
  <ChatItem
    key={chat.chatId}
    chat={chat}
    selectedChatId={selectedChatId}
    handleChatItemClick={handleChatItemClick}
  />
    </span>
  </li>
  );
})}
</div>
      ) : (
        <div>
        </div>
      )}




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