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
import Customize from './pages/Customize';
import 'boxicons'
import Products from './pages/Products';
const App = () => {
  const navigate = useNavigate();
    const [isToggleOn, setIsToggleOn] = useState(false);
  
    const handleToggleChange = () => {
      console.log(isToggleOn);
      setIsToggleOn(prevToggle => !prevToggle);
    };
  // Update the route whenever chatid changes
  const [prompt, setPrompt] = useState('');

  const [processMessage, setProcessMessage] = useState('');
  const [chatMessage, setChatMessage] = useState('');
  const [processSocket, setProcessSocket] = useState(null);
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
  const handleApiKeyChange = (apikey) => {
    // if (checkedValues.includes(value)) {
    //   // If value is already checked, remove it from the checked values.
    //   setCheckedValues(checkedValues.filter((item) => item !== value));
    // } else {
    //   // If value is not checked, add it to the checked values.
    //   setCheckedValues([...checkedValues, value]);
    // }
  };

  const handlePromptChange = (prompt) => {
    console.log("oiljgvdfljdfli")
    console.log("promt",prompt);
    setPrompt(prompt);
    // if (checkedValues.includes(value)) {
    //   // If value is already checked, remove it from the checked values.
    //   setCheckedValues(checkedValues.filter((item) => item !== value));
    // } else {
    //   // If value is not checked, add it to the checked values.
    //   setCheckedValues([...checkedValues, value]);
    // }
  };

  // Function to handle checkbox changes.
const handleCheckboxChange = (value) => {
  const action='chat';
  const socket = action === 'chat' ? chatSocket : processSocket;
  if (checkedValues.includes(value)) {
    // If value is already checked, remove it from the checked values.

   
    const activedf = JSON.stringify({ type: 'activate', active_df:checkedValues.filter((item) => item !== value)  });
    console.log("hnhnhnj",activedf)
    socket.send(activedf);
    setCheckedValues(checkedValues.filter((item) => item !== value));
  } else {
    // If value is not checked, add it to the checked values.
    setCheckedValues([...checkedValues, value]);    
    const activedf = JSON.stringify({ type: 'activate', active_df:[...checkedValues, value] });
    console.log("olhnhnj",activedf)

    socket.send(activedf);
  }
};
  useEffect(() => {
    const newProcessSocket = new WebSocket('ws://localhost:8000/ws/process');
    newProcessSocket.onopen = () => {
      setProcessSocket(newProcessSocket);
    };

    const newChatSocket = new WebSocket('ws://localhost:8000/ws/chat');
    newChatSocket.onopen = () => {
      setChatSocket(newChatSocket);
    };
    const initiatesocket = new WebSocket("ws://localhost:8000/ws/initiate");

    initiatesocket.onopen = () => {
      console.log("WebSocket connection opened");
    };

    initiatesocket.onmessage = (event) => {
      console.log("Received message:", event.data);
      const data = JSON.parse(event.data);
      console.log("ertre message:",data.chat_data);
      setChats(data.chat_data)
      setValueList(data.saved_data_source)
      // Handle the received message in your React component
    };

    // initiatesocket.onclose = () => {
    //   console.log("WebSocket connection closed");
    // };
    console.log("lkmnj");
    window.addEventListener("beforeunload", () => {
      // Send a message to the backend before the session ends
      if (initiatesocket.readyState === WebSocket.OPEN) {
        initiatesocket.send("Session is ending2");
        const filenameMessage1 = JSON.stringify({ type: 'filename', filename: chats });

        initiatesocket.send(filenameMessage1);
        
      }
    });
    return () => {
      if (processSocket) {
        processSocket.close();
      }
      if (chatSocket) {
        chatSocket.close();
      }
      if ( initiatesocket) {
        initiatesocket.close();
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
  const handleAddDataSourceClick = (datasourcevalue, sourcetype) => {
    // Handle the logic for sending the textbox content (e.g., display or process it)
    console.log('Sending:', datasourcevalue);
    // Reset the textbox and hide it after sending
    // setdatasourcevalue('');
    // setShowTextbox(false);
    const action='progress';
    const socket = action === 'chat' ? chatSocket : processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

    setProcessMessage(`Parsing  ${datasourcevalue}`);
  const urlMessage = JSON.stringify({ type: 'url', url_string: datasourcevalue, sourcetype:sourcetype });
  socket.send(urlMessage);
    // socket.send(JSON.stringify({ action, data: datasourcevalue }));
  };

  const handleFileUpload = (selectedFile) => {
    // Here, you can handle the upload logic, e.g. send the file to a server.
    if (selectedFile) {
      console.log('Uploading file in APP:', selectedFile);
      const action='progress';
      console.log(processSocket);
      const socket = action === 'chat' ? chatSocket : processSocket;
      if (!socket) {
        console.error('Socket is not available for this action.');
        return;
      }
      const filenameMessage = JSON.stringify({ type: 'filename', filename: selectedFile.name });
      socket.send(filenameMessage);
      
      setProcessMessage(`Uploadin ${selectedFile.name}`);
        const reader = new FileReader();
        reader.onload = (event) => {
          const chunk = event.target.result;
          console.log("chunk ",chunk);
          socket.send(chunk);
        };
        reader.readAsArrayBuffer(selectedFile);

      console.log("ttttttttttttttttt")
    } else {
      console.log('No file selected.');
    }
  };


  const handleSendMessage = (message, chatId) => {
    console.log("qqqqqqqqqqqqq")
    console.log(chatId);
    const query_timestamp=Date.now()
    const newMessage = {
      id: query_timestamp,
      avatar: 'https://example.com/avatar.png',
      username: 'User',
     message: message,
      timestamp: query_timestamp,
    };
    setChats((prevChats) => {
      return prevChats.map((chat) =>
        chat.chatId === chatId
          ? { ...chat, messages: [...chat.messages, newMessage] }
          : chat
      );
    });
     const action='chat';
    const socket = action === 'chat' ? chatSocket : processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

    // setChatMessage(`Sending ${action} action`);
    socket.send(JSON.stringify({ type: 'chat', action,chatId, data: message ,ch:chats,metadata_filter:isToggleOn,query_timestamp:query_timestamp}));
    // setMessages([...messages, newMessage]);
    console.log("rrrrr");
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
    if (!processSocket || !chatSocket) return;
      
    processSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'process') {
        setProcessMessage(data.message);
        console.log("progress_message ",data.message);
        if ('data_source_name' in data){
          if(valueList.length==0){
            handleCheckboxChange(data.data_source_name)
            // setCheckedValues([...checkedValues, data.data_source_name]);
          }
          setValueList([...valueList, data.data_source_name]);
        }
      }
    };

    chatSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log(selectedChatId)
      console.log("88888")
      console.log(data.message)
      if (data.action === 'chat') {
        const new_message_from_backend = {
          id: data.response_timestamp,
          avatar: 'https://example.com/avatar.png',
          username: 'AI Assistant',
          message:data.message,
          timestamp: data.response_timestamp,
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

    console.log("zxzxzx");
    console.log(valueList);
    console.log(checkedValues);
    console.log("back",new_message_from_backend);
  }    };
}, [processSocket, chatSocket, selectedChatId,checkedValues,valueList]);

  return (
    <div className="app">
  <div className="chat">
        <div className="sidebars">
    
  
   
 <SideNavbar
        chats={chats}
        selectedChatId={selectedChatId}
        handleChatItemClick={handleChatItemClick}
        handleAddChatWindow={handleAddChatWindow}
      />
        <Routes>
          <Route path='/' exact element={<Home values={valueList} 
          processMessage={processMessage}
        checkedValues={checkedValues}
        onCheckboxChange={handleCheckboxChange}
        handleAddDataSourceClick = {handleAddDataSourceClick}
        handleFileUpload = {handleFileUpload}
        progressbar={progressbar}/>} />
          <Route path='/customize' element={<Customize 
          isToggleOn={isToggleOn} 
          onToggleChange={handleToggleChange}
          handleApiKeyChange={handleApiKeyChange}
          handlePromptChange={handlePromptChange}/>} 
          />
          <Route path='/products' element={<Products />} />
          <Route path='chats' element={<ChatPanel   
                  chats={chats}
                  selectedChatId={selectedChatId}
                  handleSendMessage={handleSendMessage}
                  getChatMessages={getChatMessages}
                   />} />
          {chats.map((chat) => (
                 <Route key={selectedChatId} path={`/chats/${chat.chatId}`}  element={<ChatPanel   
                  chatsize={chat.messages.length}
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
