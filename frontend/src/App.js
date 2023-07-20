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
import ChatPanel from './ChatPanel';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './pages/Home';
import Reports from './pages/Reports';
import 'boxicons'
import Products from './pages/Products';
const App = () => {

  
  const getAllRoutes = (node, prefix = '', routes = []) => {
    if (node.props) {
      const { children, path } = node.props;
      prefix = path ? prefix + path : prefix;
  
      if (children) {
        React.Children.forEach(children, (child) => {
          getAllRoutes(child, prefix, routes);
        });
      } else {
        routes.push(prefix);
      }
    }
  
    return routes;
  };
  
  const [messages, setMessages] = useState([]);
  const [selectedChatId, setSelectedChatId] = useState(null);
  const [chats, setChats] = useState([]);
const chats1 = ['CP2OjIkU5f', '6arELI86qY', 'JSql2fp2UQ', '2n7lGWSUtW', 'U0s3FJ4jj6', 'gV022AfgJi', 'g3wbgZ6BzG', 'AJgUp71Hly', 'ZwLiazPGSD', 'V0Qp2QIVnt'];
  const handleAddChatWindow = () => {
    const newChatId = chats1[chats.length];
    setChats((prevChats) => [...prevChats, { chatId: newChatId, messages: [] }]);
    setSelectedChatId(newChatId); // Automatically select the newly added chat window
    console.log("bbbbbbbbbbbb");
    const allRoutes = getAllRoutes(Routes);

    console.log('All available routes:');
    console.log(allRoutes);
  };
  const code = `
  import logging
  `
  const handleSendMessage = (message, chatId) => {
    console.log("qqqqqqqqqqqqq")
    console.log(chatId);

    const newMessage = {
      id: messages.length + 1,
      avatar: 'https://example.com/avatar.png',
      username: 'John Doe',
      message,
      timestamp: Date.now(),
    };

    setMessages([...messages, newMessage]);
    setChats((prevChats) => {
      return prevChats.map((chat) =>
        chat.chatId === chatId
          ? { ...chat, messages: [...chat.messages, newMessage] }
          : chat
      );
    });
    console.log(chats);

    setSelectedChatId(chatId);
  };
  const getChatMessages = (chatId) => {
    console.log("ooooo");
    const selectedChat = chats.find((chat) => chat.chatId === chatId);
    console.log(selectedChat)
    return selectedChat ? selectedChat.messages : [];
  };
  
  const handleChatItemClick = (chatId) => {
    console.log(chatId);
    console.log("eeee")

    setSelectedChatId(chatId); // Update the selected chat ID when a chat is clicked
    const allRoutes = getAllRoutes(Routes);

    // console.log('All available routes:');
    // console.log(allRoutes);
  };

  
  return (
    <div className="app">
  <div className="chat">
        <div className="sidebars">
    
  
   
 <BrowserRouter>
 <SideNavbar
        chats={chats}
        selectedChatId={selectedChatId}
        handleChatItemClick={handleChatItemClick}
        handleAddChatWindow={handleAddChatWindow}
      />
        <Routes>
          <Route path='/' exact element={<Home />} />
          <Route path='/reports' element={<Reports />} />
          <Route path='/products' element={<Products />} />
          <Route path='chats' element={<ChatPanel   
                  chats={chats}
                  selectedChatId={selectedChatId}
                  handleSendMessage={handleSendMessage}
                  getChatMessages={getChatMessages}
                   />} />
          {chats.map((chat) => (
                 <Route key={selectedChatId} path={`/chats/${chat.chatId}`}  element={<ChatPanel   
                  selectedChatId={selectedChatId}
                  handleSendMessage={handleSendMessage}
                  getChatMessages={getChatMessages}
                   />} />
        ))}
   
        </Routes>
      </BrowserRouter>
      </div >
   
      </div >
    </div>
  );
};
export default App;
