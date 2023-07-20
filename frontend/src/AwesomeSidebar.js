import React, { useState } from 'react';
import './AwesomeSidebar.css'; // Stylesheet for the sidebar
import {BrowserRouter, Route, Routes,useParams} from "react-router-dom";
import { Link } from 'react-router-dom';
import ConversationPage from './ConversationPage';

const AwesomeSidebar = () => {
  const [chats, setChats] = useState([]);
  const [newChat, setNewChat] = useState("");

  const handleAddChat = () => {
    if (newChat.trim() === "") return;
    setChats([...chats, newChat]);
    setNewChat("");
  };
  return (
    <BrowserRouter>
    <div className="app">
      <div className="sidebar12">
        <div className="add-chat">
          <input
            type="text"
            placeholder="Enter new chat name"
            value={newChat}
            onChange={(e) => setNewChat(e.target.value)}
          />
          <button onClick={handleAddChat}>Add Chat</button>
        </div>
        <div className="chat-history">
          <h2>Chat History</h2>
          <ul>
            {chats.map((chat, index) => (
              <li key={index}>
                <Link to={`/chat/${index}`}>{chat}</Link>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <div className="chat-window">
        <h2>Chat Window</h2>
        <Routes>
          <Route path="/chat/:id" element={<ConversationPage/>} />
        </Routes>
      </div>
    </div>
  </BrowserRouter>
);
}



export default AwesomeSidebar;
