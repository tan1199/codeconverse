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



function SideNavbar({ chats, selectedChatId, handleChatItemClick, handleAddChatWindow, deletechat, isAuthenticated, handletoastmessage,userInfo }) {
  const navigate = useNavigate();
  if(isAuthenticated){
userInfo= "Logout"
  }
  const handleLogout = () => {
      if(!isAuthenticated){
        return;
  }
    localStorage.setItem('authToken', null);
    handletoastmessage('Logged Out')
     setTimeout(() => {
    window.location.reload();

      }, 2000);
     };
  const navigatetohome = () => {
    navigate(`/`);
  };
  
  const reversedChats = chats.slice().reverse();
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
  {/* <button id="btn" onClick={menuBtnChange}>
       <FaIcons.FaBars size={25}  onClick={menuBtnChange} />
  </button>  */}
      </div> 
      <ul className="nav-list">

      <button className="add-chat-window-button" onClick={handleAddChatWindow}>➕         New Chat</button>



      {isOpen ? (

<div className='conversationname'>
{reversedChats.map((chat, index)=> {

                                     return (
                                      <div className='qsdfi' key={index}>

                                      <li key={index}>
                                        <Link to={`/chats/${chat.chatId}`} >
                                      {/* <i className="bx bx-cog"><BiIcons.BiSolidChat /></i> */}

          <span>
  <ChatItem
    key={chat.chatId}
    chat={chat}
    selectedChatId={selectedChatId}
    handleChatItemClick={handleChatItemClick}
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
  <div className='desl' onClick={() => deletechat(chat.chatId)}><MdIcons.MdOutlineDeleteOutline color='white' size='2vw' /></div> 
  </div>

  );
})}
</div>
      ) : (
        <div>
        </div>
      )}



{ isAuthenticated ? (
  <div>
        {SidebarData.map((item, index) => {
                                     return (
                              <li key={index}>
                                    <Link to={item.path} className='sideitems'>



                                                <div className='asb'>{item.icon}</div>
                                                <span className="links_names" >{item.title}</span>
                                             </Link>
                                              <span className="tooltip">{item.title}</span>
                                            </li>
                                     );
                                   })}</div>
):(        <div>  {SidebarData.map((item, index) => {
                                     return (
                              <li key={index}>
                                    <Link to="/" onClick={() => handletoastmessage('Please Login to access')}  className='sideitems'>



                                                <div className='asb'>{item.icon}</div>
                                                <span className="links_names">{item.title}</span>
                                             </Link>
                                              <span className="tooltip">{item.title}</span>
                                            </li>
                                     );
                                   })}
                                   </div>)}
                        <li key='1'>
                                    <Link to="/user"  onClick={() => handleLogout()} className='sideitems'>


                                                  <div className='asb'><IoIcons.IoMdPeople  size='1.5vw' /></div>
                                                <span className="links_names">{userInfo}</span>
                                             </Link>
                                              <span className="tooltip">{userInfo}</span>
                                            </li>
             </ul>
       </div>


    </>
  );
}

export default SideNavbar;