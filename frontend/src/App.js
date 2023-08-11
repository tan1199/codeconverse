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

  
  // const [messages, setMessages] = useState([]);
  const [selectedChatId, setSelectedChatId] = useState(null);
  const [chats, setChats] = useState([]);
const chats1 = ['CP2OjIkU5f', '6arELI86qY', 'JSql2fp2UQ', '2n7lGWSUtW', 'U0s3FJ4jj6', 'gV022AfgJi', 'g3wbgZ6BzG', 'AJgUp71Hly', 'ZwLiazPGSD', 'V0Qp2QIVnt'];
  const handleAddChatWindow = () => {
    const newChatId = chats1[chats.length];
    setChats((prevChats) => [...prevChats, { chatId: newChatId, messages: [] }]);
    setSelectedChatId(newChatId); // Automatically select the newly added chat window
    console.log("bbbbbbbbbbbb");
  };
  const code = `
  import loggingvvv
  `
  const handleSendMessage = (message, chatId) => {
    console.log("qqqqqqqqqqqqq")
    console.log(chatId);

    const newMessage = {
      id: Date.now(),
      avatar: 'https://example.com/avatar.png',
      username: 'John Doe',
     message: message,
      timestamp: Date.now(),
    };
    setChats((prevChats) => {
      return prevChats.map((chat) =>
        chat.chatId === chatId
          ? { ...chat, messages: [...chat.messages, newMessage] }
          : chat
      );
    });


    // setMessages([...messages, newMessage]);
    console.log("rrrrr")
// 
    // console.log(messages)
    fetch("http://localhost:8000/api/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
      const back_end_message=data.message;
      console.log("fgfggfg");
      console.log(data);
        const new_message_from_backend = {
          id: Date.now(),
          avatar: 'https://example.com/avatar.png',
          username: 'AI Assistant',
          message:back_end_message,
          timestamp: Date.now(),
        };
        setChats((prevChats) => {
          return prevChats.map((chat) =>
            chat.chatId === chatId
              ? { ...chat, messages: [...chat.messages, new_message_from_backend] }
              : chat
          );
        });
      })
      .catch((error) => {
        console.error("Error:", error);
      })

    console.log(chats);

    setSelectedChatId(chatId);
  };
  const getChatMessages = (chatId) => {
    console.log("ooooo");
    const selectedChat = chats.find((chat) => chat.chatId === chatId);
    console.log(selectedChat)
    // console.log(messages)
    return selectedChat ? selectedChat.messages : [];
  };
  
  const handleChatItemClick = (chatId) => {
    console.log(chatId);
    console.log("eeee")

    setSelectedChatId(chatId); // Update the selected chat ID when a chat is clicked

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
