import React, { useState, useEffect,useRef } from 'react';
import axios from 'axios';
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
import { useNavigate } from 'react-router-dom';

import Home from './pages/Home';
import Reports from './pages/Reports';
import 'boxicons'
import Products from './pages/Products';
const App = () => {
  const navigate = useNavigate();

  // Update the route whenever chatid changes
  const [statusMessage, setStatusMessage] = useState('');
  const [chatMessage, setChatMessage] = useState('');
  const [statusSocket, setStatusSocket] = useState(null);
  const [chatSocket, setChatSocket] = useState(null);
  const [valueList, setValueList] = useState([]);
  const [checkedValues, setCheckedValues] = useState([]);
  const [progressbar, setprogressbar] = useState(false);
  function generateRandomString() {
    // const strlength=Math.floor(Math.random() * 11) + 10;
    const strlength=10;
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = '';
    const charactersLength = characters.length;
    
    for (let i = 0; i < strlength; i++) {
      const randomIndex = Math.floor(Math.random() * charactersLength);
      result += characters.charAt(randomIndex);
    }
    
    return result;
  }
  // Function to handle checkbox changes.
const handleCheckboxChange = (value) => {
  if (checkedValues.includes(value)) {
    // If value is already checked, remove it from the checked values.
    setCheckedValues(checkedValues.filter((item) => item !== value));
  } else {
    // If value is not checked, add it to the checked values.
    setCheckedValues([...checkedValues, value]);
  }
};
  useEffect(() => {
    const newStatusSocket = new WebSocket('ws://localhost:8000/ws/status');
    newStatusSocket.onopen = () => {
      setStatusSocket(newStatusSocket);
    };

    const newChatSocket = new WebSocket('ws://localhost:8000/ws/chat');
    newChatSocket.onopen = () => {
      setChatSocket(newChatSocket);
    };

    return () => {
      if (statusSocket) {
        statusSocket.close();
      }
      if (chatSocket) {
        chatSocket.close();
      }
    };
  }, []);
  // const [messages, setMessages] = useState([]);
  const selectedChatIdRef = useRef(null);

  const [selectedChatId, setSelectedChatId] = useState(null);
  const [chats, setChats] = useState([]);
const chats1 = ['CP2OjIkU5f', '6arELI86qY', 'JSql2fp2UQ', '2n7lGWSUtW', 'U0s3FJ4jj6', 'gV022AfgJi', 'g3wbgZ6BzG', 'AJgUp71Hly', 'ZwLiazPGSD', 'V0Qp2QIVnt'];
const handleAddChatWindow = () => {
  const newChatId = Date.now().toString();
  setChats((prevChats) => [...prevChats, { chatId: newChatId, messages: [] }]);
  setSelectedChatId(newChatId); // Set the selectedChatId immediately after adding the new chat
  console.log("bbbbbbbbbbbb");
  selectedChatIdRef.current = newChatId;
  navigate(`/chats/${newChatId}`);

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
     const action='chat';
    const socket = action === 'chat' ? chatSocket : statusSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

    setStatusMessage(`Sending ${action} action`);
    socket.send(JSON.stringify({ action,chatId, data: message }));
    // setMessages([...messages, newMessage]);
    console.log("rrrrr")
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

  useEffect(() => {
    if (!statusSocket || !chatSocket) return;

    statusSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'status') {
        setStatusMessage(data.message);
      }
    };

    chatSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log(selectedChatId)
      console.log("88888")
      console.log(data.message)
      if (data.action === 'chat') {
        const new_message_from_backend = {
          id: Date.now(),
          avatar: 'https://example.com/avatar.png',
          username: 'AI Assistant',
          message:data.message,
          timestamp: Date.now(),
        };
        setChats((prevChats) => {
          return prevChats.map((chat) =>
            chat.chatId === data.chatId
              ? { ...chat, messages: [...chat.messages, new_message_from_backend] }
              : chat
          );
        });
        if(data.progressbar){
          setprogressbar(true);
        }
else{
  setprogressbar(false);
}
    console.log(chats);
    setValueList([...valueList, generateRandomString()]);
    console.log("zxzxzx");
    console.log(valueList);
    console.log(checkedValues);
  }    };
}, [statusSocket, chatSocket,selectedChatId,checkedValues,valueList]);

  return (
    <div className="app">
  <div className="chat">
        <div className="sidebars">
    
  
   
 <SideNavbar
        chats={chats}
        selectedChatId={selectedChatIdRef.current}
        handleChatItemClick={handleChatItemClick}
        handleAddChatWindow={handleAddChatWindow}
      />
        <Routes>
          <Route path='/' exact element={<Home values={valueList} 
        checkedValues={checkedValues}
        onCheckboxChange={handleCheckboxChange}
        progressbar={progressbar}/>} />
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
      </div >
   
      </div >
    </div>
  );
};
export default App;
