import React, { useState } from 'react';
import ChatMessage from './components/ChatMessage';
import InputBox from './components/InputBox';
import './ChatPanel.css';

function ChatPanel({selectedChatId,handleSendMessage,getChatMessages}) {

 
  return (
    <div>
        <div className="chat-panel">
      <div className="chat-messages">
      {selectedChatId ? (
          <div>
          {getChatMessages(selectedChatId).map((message) => (
            <ChatMessage
              key={message.id}
              avatar={message.avatar}
              username={message.username}
              message={message.message}
              timestamp={message.timestamp}
            />
          ))}
            
       
    
        </div>
      ) : (
        <div>
          <h2>No chat selected</h2>
          <p>Select a chat from the sidebar or add a new chat window.</p>
        </div>
      )}
    </div>
    <InputBox
            onSendMessage={(message) => handleSendMessage(message, selectedChatId)}
          />
  </div>
    </div>  
  )
}

export default ChatPanel