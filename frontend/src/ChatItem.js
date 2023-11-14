import React from 'react';
import './SideNavbar.css';
import './ChatItem.css';
import * as MdIcons from 'react-icons/md'; 
import * as BiIcons from 'react-icons/bi';
function formatTimestamp(timestamp) {
  const date = new Date(Number(timestamp));
  const year = date.getFullYear().toString().slice(-2);
  const month = (date.getMonth() + 1).toString().padStart(2, '0');
  const day = date.getDate().toString().padStart(2, '0');
  const hours = date.getHours().toString().padStart(2, '0');
  const minutes = date.getMinutes().toString().padStart(2, '0');
  const seconds = date.getSeconds().toString().padStart(2, '0');
  return `${year}/${month}/${day} ${hours}:${minutes}:${seconds}`;
}


const ChatItem = ({ chat, selectedChatId, handleChatItemClick }) => {
  return (
    <div
      key={chat.chatId}
      className={`chat-item links_name ${selectedChatId === chat.chatId ? 'active' : ''}`}
      onClick={() => handleChatItemClick(chat.chatId)}
    >                                  
    <BiIcons.BiSolidChat size ='1.5vw' id='ioplk' /> {formatTimestamp(chat.chatId)}
    </div>
  );
};

export default ChatItem;
