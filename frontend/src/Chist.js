import React, { useState } from 'react';
import ChatMessage from './components/ChatMessage';
import UserList from './components/UserList';
import InputBox from './components/InputBox';
function Chist() {
    const [chats, setChats] = useState([]);
    const handleAddChatWindow = () => {
        const newChatId = `chat-${Math.random().toString(36).substr(2, 9)}`;
        setChats((prevChats) => [...prevChats, { chatId: newChatId, messages: [] }]);
      };
      
    const handleSendMessage = (message, chatId) => {
        const newMessage = {
          id: chats.find((chat) => chat.chatId === chatId).messages.length + 1,
          avatar: 'https://example.com/avatar.png',
          username: 'John Doe',
          message,
          timestamp: Date.now(),
        };
      
        setChats((prevChats) => {
          return prevChats.map((chat) =>
            chat.chatId === chatId
              ? { ...chat, messages: [...chat.messages, newMessage] }
              : chat
          );
        });
      };
  return (
    <div>
    {chats.map((chat) => (
      <div key={chat.chatId}>
        <h2>Chat Window: {chat.chatId}</h2>
        <ChatMessage messages={chat.messages} />
        <InputBox
          onSendMessage={(message) => handleSendMessage(message, chat.chatId)}
        />
      </div>
    ))}
    <button onClick={handleAddChatWindow}>Add New Chat Window</button>
  </div>
  )
}

export default Chist