import React from 'react';
import './SideNavbar.css';
import './ChatItem.css';
import * as MdIcons from 'react-icons/md'; 
import * as BiIcons from 'react-icons/bi';


const ChatItem = ({ chat, selectedChatId, handleChatItemClick, deletechat }) => {
  console.log("zxcv",selectedChatId)
  return (
    <div
      key={chat.chatId}
      className={`chat-item links_name ${selectedChatId === chat.chatId ? 'active' : ''}`}
      onClick={() => handleChatItemClick(chat.chatId)}
    >                                  
    <BiIcons.BiSolidChat size={20} id='ioplk' /> {chat.chatId}
    </div>
  );
};

export default ChatItem;
