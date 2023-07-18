import React, { useState } from 'react';
import ChatMessage from './components/ChatMessage';
import UserList from './components/UserList';
import InputBox from './components/InputBox';
import './App.css';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { dark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { atomDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import AwesomeSidebar from './AwesomeSidebar';
import Header from './Header';
import SideNavbar from './SideNavbar';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './pages/Home';
import Reports from './pages/Reports';
import 'boxicons'
import Products from './pages/Products';
const App = () => {
  const [messages, setMessages] = useState([]);
  const code = `
  import logging
  `
  const handleSendMessage = (message) => {
    const newMessage = {
      id: messages.length + 1,
      avatar: 'https://example.com/avatar.png',
      username: 'John Doe',
      message,
      timestamp: Date.now(),
    };

    setMessages([...messages, newMessage]);
  };

  return (
    <div className="app">
  <div className="chat">
        <div className="sidebars">
 <BrowserRouter>
         <SideNavbar/>
        <Routes>
          <Route path='/' exact element={Home} />
          <Route path='/reports' element={Reports} />
          <Route path='/products' element={Products} />
        </Routes>
      </BrowserRouter>

          <div className="chat-panel">
        <div className="chat-messages">
          {messages.map((message) => (
            <ChatMessage
              key={message.id}
              avatar={message.avatar}
              username={message.username}
              message={message.message}
              timestamp={message.timestamp}
            />
          ))}
   </div>
                <InputBox onSendMessage={handleSendMessage} />
        </div>
      </div >
    </div>
        </div>
  );
};
export default App;
