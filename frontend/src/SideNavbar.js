import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as BsIcons from 'react-icons/bs';
import * as BiIcons from 'react-icons/bi';
import * as IoIcons from 'react-icons/io';
import * as MdIcons from 'react-icons/md'; 
import { Link } from 'react-router-dom';
import './SideNavbar.css';
import ChatItem from './ChatItem';
import { SidebarData } from './SidebarData';

import { IconContext } from 'react-icons';
import { useNavigate } from 'react-router-dom';



function SideNavbar({ chats, selectedChatId, handleChatItemClick, handleAddChatWindow, deletechat }) {
  const navigate = useNavigate();
  
  const navigatetohome = () => {
    navigate(`/`);
  };
  
  const reversedChats = chats.slice().reverse();
console.log("dfdgfgd")
console.log(selectedChatId)
  const [isOpen, setIsOpen] = useState(true);
const abc=selectedChatId;
  function menuBtnChange() {
    setIsOpen(!isOpen);
  }
  return (
  <>
    <div className={`sidebar ${isOpen ? 'open' : 'qq'}`}>
      <div className="logo-details">
        <i className="bx bxl-c-plus-plus icon"></i>

        <div className="logo_name" onClick={() => navigatetohome()} >Code Converse</div>
  <button id="btn" onClick={menuBtnChange}>
       <FaIcons.FaBars size={25}  onClick={menuBtnChange} />
      </button>      </div>
      <ul className="nav-list">

      <button className="add-chat-window-button" onClick={handleAddChatWindow}>➕         New Chat</button>



      {isOpen ? (

<div className='conversationname'>
{reversedChats.map((chat)=> {

                                     return (
                                      <div className='qsdfi'>

                                      <li>
                                        <Link to={`/chats/${chat.chatId}`} >
                                      {/* <i className="bx bx-cog"><BiIcons.BiSolidChat /></i> */}

          <span className="links_name">
  <ChatItem
    key={chat.chatId}
    chat={chat}
    selectedChatId={selectedChatId}
    handleChatItemClick={handleChatItemClick}
    deletechat={deletechat}
  />
  {/* <div className='del'><MdIcons.MdDelete size={20} /></div> */}
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
  <div className='desl' onClick={() => deletechat(chat.chatId)}><MdIcons.MdOutlineDeleteOutline color='white' size={20} /></div> 
  </div>

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