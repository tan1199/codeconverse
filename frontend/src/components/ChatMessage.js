import React from 'react';
import reactLogo from "../images/avatar.png";

const ChatMessage = ({ avatar, username, message, timestamp }) => {
  return (
    <div className="chat-message">
      <div className="avatar">
        <img src={reactLogo} alt="User Avatar" />
      </div>
      <div className="message-content">
        <div className="username">{username}</div>
        <div className="message">{message}</div>
      </div>
    </div>
  );
};

export default ChatMessage;
