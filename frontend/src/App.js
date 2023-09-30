import React, { useState, useEffect,useRef } from 'react';
import './App.css';
import SideNavbar from './SideNavbar';
import ChatPanel from './ChatPanel';
import {Route, Routes} from "react-router-dom";
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Home from './pages/Home';
import Customize from './pages/Customize';
import Products from './pages/Products';
import UserDetail from './pages/UserDetail';
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
  const [userSocket, setUserSocket] = useState(null);
  const [valueList, setValueList] = useState([]);
  const [checkedValues, setCheckedValues] = useState([]);
  const [progressbar, setprogressbar] = useState(false);
  const [token, setToken]=useState(localStorage.getItem('authToken'));
  const [userInfo, setUserInfo] = useState('User');
  const [isAuthenticated, setIsAuthenticated] = useState(false);

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
    if (!token){
      return;
    }
    const newUserSocket = new WebSocket(`ws://localhost:8000/ws/user?token=${token}`);
    newUserSocket.onopen = () => {
      console.log("gbhjk",token);
      setUserSocket(newUserSocket);
    };

    const newProcessSocket = new WebSocket(`ws://localhost:8000/ws/process?token=${token}`);
    newProcessSocket.onopen = () => {
      setProcessSocket(newProcessSocket);
    };

    const newChatSocket = new WebSocket(`ws://localhost:8000/ws/chat?token=${token}`);
    newChatSocket.onopen = () => {
      setChatSocket(newChatSocket);
    };

    const initiatesocket = new WebSocket(`ws://localhost:8000/ws/initiate?token=${token}`);

    initiatesocket.onopen = () => {
      console.log("WebSocket connection opened");
    };

    initiatesocket.onmessage = (event) => {
      console.log("Received message:", event.data);
      const data = JSON.parse(event.data);
      if(data.authentication==false){
setIsAuthenticated(false);

      }

      else{
                    setIsAuthenticated(true);

              console.log("ertre message:",data.chat_data);
      setChats(data.chat_data)
      setValueList(data.saved_data_source)
      setUserInfo(data.username)
      }
      // Handle the received message in your React component
    };

    // initiatesocket.onclose = () => {
    //   console.log("WebSocket connection closed");
    // };
    console.log("lkmnj");
    // window.addEventListener("beforeunload", () => {
    //   // Send a message to the backend before the session ends
    //   if (initiatesocket.readyState === WebSocket.OPEN) {
    //     initiatesocket.send("Session is ending2");
    //     const filenameMessage1 = JSON.stringify({ type: 'filename', filename: chats });

    //     initiatesocket.send(filenameMessage1);
        
    //   }
    // });
        initiatesocket.onclose = (event) => {
      if (event.wasClean) {
        console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
      } else {
        console.error("WebSocket connection abruptly closed.");
      }
    };
    
          newUserSocket.onclose = (event) => {
      if (event.wasClean) {
        console.log(`WebSocket connection closed cleanly, code=${event.code}, reason=${event.reason}`);
      } else {
        console.error("WebSocket connection abruptly closed.");
      }
    };  
    return () => {
      if (processSocket) {
        processSocket.close();
      }
      if (chatSocket) {
        chatSocket.close();
      }
      // if ( initiatesocket) {
      //   initiatesocket.close();
      // }
      // if (newUserSocket) {
      //   newUserSocket.close();
      // }
    };
  }, [token]);
  // const [messages, setMessages] = useState([]);
  const selectedChatIdRef = useRef(null);

  const [selectedChatId, setSelectedChatId] = useState(null);
  const [chats, setChats] = useState([]);
// const chats1 = ['CP2OjIkU5f', '6arELI86qY', 'JSql2fp2UQ', '2n7lGWSUtW', 'U0s3FJ4jj6', 'gV022AfgJi', 'g3wbgZ6BzG', 'AJgUp71Hly', 'ZwLiazPGSD', 'V0Qp2QIVnt'];
const handleAddChatWindow = () => {
  if(!isAuthenticated){
    handletoastmessage('User not logged in');
    return;
  }
  const newChatId = Date.now().toString();
  setChats((prevChats) => [...prevChats, { chatId: newChatId, messages: [] }]);
  setSelectedChatId(newChatId); // Set the selectedChatId immediately after adding the new chat
  console.log("bbbbbbbbbbbb");
  selectedChatIdRef.current = newChatId;
  navigate(`/chats/${newChatId}`);
  console.log("fgb",newChatId)
};
  
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
  const deletedatasource = (datasource) => {
    // Handle the logic for sending the textbox content (e.g., display or process it)
    console.log('deleting:', datasource);
    const action='progress';
    console.log(processSocket);
    const socket = action === 'chat' ? chatSocket : processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

 
    const deletefilenameMessage = JSON.stringify({ type: 'deletedatasource', filename: datasource });
    socket.send(deletefilenameMessage);
    setValueList((prevValueList) => {
      return prevValueList.filter((datasourcename) => datasourcename !== datasource);
    });
    
    setValueList((prevCheckedValues) => {
      return prevCheckedValues.filter((checkedvalue) => checkedvalue !== datasource);
    });
    }

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
  const handlesetSelectedChatId = (newValue) => {
    console.log("napa",newValue)

    setSelectedChatId(newValue);
  };

  const getChatMessages = (chatId) => {
    console.log("ooooo");
    console.log("na",chatId,":lk",chats)
    console.log(typeof chats[0].chatId);  // Output: "function"
    console.log(typeof chatId);  // Output: "function"

    const selectedChat = chats.find((chat) => chat.chatId === chatId);
    console.log(selectedChat)
    // console.log(messages)
    return selectedChat ? selectedChat.messages : [];
  };
  const deletechat = (ChatId) => {
    console.log("deletechat",ChatId);
    handleAddChatWindow();
        console.log("nowathome",ChatId);
    setChats((prevChats) => {
      return prevChats.filter((chat) => chat.chatId !== ChatId);
    });
    const action='progress';
    console.log(processSocket);
    const socket = action === 'chat' ? chatSocket : processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

    const deletechatIdMessage = JSON.stringify({ type: 'deletechatId', filename: ChatId });
    socket.send(deletechatIdMessage);
    
    }
  
  const handleChatItemClick = (chatId) => {
    console.log(chatId);
    console.log("eeee")

    setSelectedChatId(chatId); // Update the selected chat ID when a chat is clicked

  };
  const handletoastmessage = (message) =>{
            toast(`${message}`, {
    position: toast.POSITION.BOTTOM_RIGHT,
    className: 'toast-message',
    bodyClassName:'toast-mess',
    autoClose: 500, // Automatically close the toast after 2 seconds
    hideProgressBar: true, // Hide the progress bar

});
  }
  const handleUserDetail = (isSignup,username,password,email_id,aud,iss,client_id) => {
    console.log("userdetails",isSignup,username,password,email_id,aud,iss,client_id);
    var google_auth=false;
          if((aud==client_id)&&(['accounts.google.com', 'https://accounts.google.com'].includes(iss))){
google_auth=true
setUserInfo(username);
username=email_id
      }
    fetch("http://localhost:8000/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({username:username,password:password,email_id:email_id, isSignup: isSignup,google_auth:google_auth }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        console.log("oipoo")
        console.log(data.token)
        if(data.access_token){
            setToken(data.access_token)
            setIsAuthenticated(true);
            // Storing the token in LocalStorage
            localStorage.setItem('authToken', data.access_token);
    handletoastmessage(`${username} logged in Successfully`)
    if(!google_auth){
          setUserInfo(username);
    }
            console.log("jghn");
                navigate(`/data`);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      })

  };
  useEffect(() => {
    if (!processSocket || !chatSocket || !userSocket) return;
      
    processSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'process') {
        setProcessMessage(data.message);
        console.log("progress_message ",data.message);
        if ('data_source_name' in data){
          if(valueList.length===0){
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
}, [processSocket, chatSocket,userSocket, selectedChatId,checkedValues,valueList]);

  return (
    <div className="app">
  <div className="chat">
        <div className="sidebars">
    
  
   
 <SideNavbar
        chats={chats}
        selectedChatId={selectedChatId}
        handleChatItemClick={handleChatItemClick}
        handleAddChatWindow={handleAddChatWindow}
        deletechat={deletechat}
        isAuthenticated={isAuthenticated}
        handletoastmessage={handletoastmessage}
        userInfo={userInfo}
      />
        <Routes>
          <Route path='/data' exact element={<Home values={valueList} 
          processMessage={processMessage}
        checkedValues={checkedValues}
        onCheckboxChange={handleCheckboxChange}
        handleAddDataSourceClick = {handleAddDataSourceClick}
        handleFileUpload = {handleFileUpload}
        progressbar={progressbar}
        deletedatasource={deletedatasource}
        />} />
          <Route path='/customize' element={<Customize 
          isToggleOn={isToggleOn} 
          onToggleChange={handleToggleChange}
          handleApiKeyChange={handleApiKeyChange}
          handlePromptChange={handlePromptChange}/>} 
          />
          <Route path='/' element={<Products
           isAuthenticated={isAuthenticated} />} />
          <Route path='/user' element={<UserDetail
           handleUserDetail={handleUserDetail} 
            isAuthenticated={isAuthenticated}
            userInfo={userInfo}/>} />
          {chats.map((chat) => (
                 <Route key={selectedChatId} path={`/chats/${chat.chatId}`}  element={<ChatPanel   
                  handlesetSelectedChatId={handlesetSelectedChatId}
                  selectedChatId={selectedChatId}
                  handleSendMessage={handleSendMessage}
                  getChatMessages={getChatMessages}
                   />} />
        ))}
   
        </Routes>
      </div >
   
      </div >
                  <ToastContainer className={true}/>

    </div>
  );
};
export default App;
