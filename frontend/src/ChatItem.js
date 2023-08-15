import React from 'react';
import './SideNavbar.css';
import './ChatItem.css';

const ChatItem = ({ chat, selectedChatId, handleChatItemClick }) => {
  console.log("zxcv",selectedChatId)
  return (
    <div
      key={chat.chatId}
      className={`chat-item links_name ${selectedChatId === chat.chatId ? 'active' : ''}`}
      onClick={() => handleChatItemClick(chat.chatId)}
    >
      {chat.chatId}
    </div>
  );
};

export default ChatItem;
