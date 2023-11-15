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
import About from './pages/About';
const App = () => {
  const navigate = useNavigate();
    const [isFilterToggleOn, setIsFilterToggleOn] = useState(false);
      const [isRerankToggleOn, setIsRerankToggleOn] = useState(false);

    const onFilterToggleChange = () => {
      // console.log(isFilterToggleOn);
      setIsFilterToggleOn(prevToggle => !prevToggle);
    };
        const onRerankToggleChange = () => {
      // console.log(isRerankToggleOn);
      setIsRerankToggleOn(prevToggle => !prevToggle);
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
  const [token, setToken]=useState(localStorage.getItem('authToken'));
  const [userInfo, setUserInfo] =useState({
    username: 'Guest',
    email: '',
    usage: '',
  });
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
    const action='api_key_update';
    const socket = processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }
    // setChatMessage(`Sending ${action} action`);
    socket.send(JSON.stringify({ type: action, action, data: apikey }));
    // setMessages([...messages, newMessage]);
    
        handletoastmessage('API Key Successfully Updated');
     setTimeout(() => {
    window.location.reload();

      }, 2000);
   
       
        };

  const handlePromptChange = (prompt) => {
    setPrompt(prompt);
  };

  // Function to handle checkbox changes.
const handleCheckboxChange = (value) => {
  const action='chat';
  const socket = action === 'chat' ? chatSocket : processSocket;
  if (checkedValues.includes(value)) {
    // If value is already checked, remove it from the checked values.
   
    const activedf = JSON.stringify({ type: 'activate', active_df:checkedValues.filter((item) => item !== value)  });
    socket.send(activedf);
    setCheckedValues(checkedValues.filter((item) => item !== value));
  } else {
    // If value is not checked, add it to the checked values.
    setCheckedValues([...checkedValues, value]);    
    const activedf = JSON.stringify({ type: 'activate', active_df:[...checkedValues, value] });

    socket.send(activedf);
  }
};
  useEffect(() => {
    if (!token){
      return;
    }

    const newProcessSocket = new WebSocket(`wss://cc-backend.up.railway.app/ws/process?token=${token}`);
    newProcessSocket.onopen = () => {
      setProcessSocket(newProcessSocket);
    };

    const newChatSocket = new WebSocket(`wss://cc-backend.up.railway.app/ws/chat?token=${token}`);
    newChatSocket.onopen = () => {
      setChatSocket(newChatSocket);
    };

    const initiatesocket = new WebSocket(`wss://cc-backend.up.railway.app/ws/initiate?token=${token}`);

    initiatesocket.onopen = () => {
      console.log("WebSocket connection opened");
    };

    initiatesocket.onmessage = (event) => {
      
      const data = JSON.parse(event.data);
      if(data.authentication==false){
setIsAuthenticated(false);

      }

      else{
                    setIsAuthenticated(true);

      setChats(data.chat_data)
      setValueList(data.saved_data_source)
      setUserInfo({
    username: data.username,
    email: data.email_id,
    usage: data.usage,
  })
      }
      // Handle the received message in your React component
    };

    // initiatesocket.onclose = () => {
    //   console.log("WebSocket connection closed");
    // };
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
    };
  }, [token]);
  const selectedChatIdRef = useRef(null);

  const [selectedChatId, setSelectedChatId] = useState(null);
  const [chats, setChats] = useState([]);
// const chats1 = ['CP2OjIkU5f', '6arELI86qY', 'JSql2fp2UQ', '2n7lGWSUtW', 'U0s3FJ4jj6', 'gV022AfgJi', 'g3wbgZ6BzG', 'AJgUp71Hly', 'ZwLiazPGSD', 'V0Qp2QIVnt'];
const handleAddChatWindow = () => {
  if(!isAuthenticated){
    handletoastmessage('User not logged in');
    return;
  }
  if(chats.length){
        const maxChatId = Math.max(...chats.map(chat => parseInt(chat.chatId, 10)), 0);
    const maxIdChat = chats.find((chat) => chat.chatId.toString() === maxChatId.toString());
    if(maxIdChat['messages'].length===0){
      // console.log("nm,.",maxIdChat['messages'].length,isDelete,chats.length,chats[chats.length-1])
        navigate(`/chats/${maxChatId.toString()}`);
          setSelectedChatId(maxChatId.toString()); 
            selectedChatIdRef.current = maxChatId.toString();
      return;
    }
    // console.log("clog",maxChatId,typeof maxIdChat['messages'],maxIdChat.length,maxIdChat['messages'])

  }

  const newChatId = Date.now().toString();
  setChats((prevChats) => [...prevChats, { chatId: newChatId, messages: [] }]);
  setSelectedChatId(newChatId); // Set the selectedChatId immediately after adding the new chat
  selectedChatIdRef.current = newChatId;
  navigate(`/chats/${newChatId}`);

};
  
  const handleAddDataSourceClick = (datasourcevalue, sourcetype) => {
    // Handle the logic for sending the textbox content (e.g., display or process it)
    // console.log('Sending:', datasourcevalue,sourcetype);
    // Reset the textbox and hide it after sending
    // setdatasourcevalue('');
    // setShowTextbox(false);
    if(sourcetype==='Gitlab'){
      handletoastmessage(`Coming Soon`)
      return;
    }
    const action='progress';
    const socket = action === 'chat' ? chatSocket : processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

    setProcessMessage('Uploading Data Source');
  const urlMessage = JSON.stringify({ type: 'url', source_string: datasourcevalue, sourcetype:sourcetype });
  socket.send(urlMessage);
    // socket.send(JSON.stringify({ action, data: datasourcevalue }));
  };
  const deletedatasource = (datasource) => {
    // Handle the logic for sending the textbox content (e.g., display or process it)
    // console.log('deleting:', datasource);
    const action='progress';
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
      // console.log('Uploading file in APP:', selectedFile);
      const action='progress';
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
          socket.send(chunk);
        };
        reader.readAsArrayBuffer(selectedFile);

    } else {
      console.log('No file selected.');
    }
  };


  const handleSendMessage = (message, chatId) => {
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
    socket.send(JSON.stringify({ type: 'chat', action,chatId, data: message ,ch:chats,metadata_filter:isFilterToggleOn,rerank:isRerankToggleOn,query_timestamp:query_timestamp,source_location:"",regenerate:false,custom_prompt:prompt}));
    // setMessages([...messages, newMessage]);
    setSelectedChatId(chatId);


  };

  const regenerateResponse = (message, chatId,source_location) => {
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
    socket.send(JSON.stringify({ type: 'chat', action,chatId, data: message ,ch:chats,metadata_filter:isFilterToggleOn,rerank:isRerankToggleOn,query_timestamp:query_timestamp,source_location:source_location,regenerate:true,custom_prompt:prompt}));
    // setMessages([...messages, newMessage]);
    setSelectedChatId(chatId);


  };


  const handlesetSelectedChatId = (newValue) => {

    setSelectedChatId(newValue);
  };

  const getChatMessages = (chatId) => {

    const selectedChat = chats.find((chat) => chat.chatId === chatId);
    return selectedChat ? selectedChat.messages : [];
  };
  const deletechat = (ChatId) => {
    const maxChatId = Math.max(...chats.map(chat => parseInt(chat.chatId, 10)), 0);
      const maxIdChat = chats.find((chat) => chat.chatId.toString() === maxChatId.toString());
     if((ChatId.toString() === maxChatId.toString())&&(maxIdChat['messages'].length===0)){
      return;
     }
    handleAddChatWindow();
    setChats((prevChats) => {
      return prevChats.filter((chat) => chat.chatId !== ChatId);
    });
    const action='progress';
    const socket = action === 'chat' ? chatSocket : processSocket;
    if (!socket) {
      console.error('Socket is not available for this action.');
      return;
    }

    const deletechatIdMessage = JSON.stringify({ type: 'deletechatId', filename: ChatId });
    socket.send(deletechatIdMessage);
    
    }
  
  const handleChatItemClick = (chatId) => {

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
    var google_auth=false;
          if((aud==client_id)&&(['accounts.google.com', 'https://accounts.google.com'].includes(iss))){
google_auth=true
  setUserInfo(prevValues => ({
      ...prevValues,
      username: username,
      email_id: username,
    }));
username=email_id
      }
    fetch("https://cc-backend.up.railway.app/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({username:username,password:password,email_id:email_id, isSignup: isSignup,google_auth:google_auth }),
    })
      .then((response) => response.json())
      .then((data) => {
        if(data.access_token){
            setToken(data.access_token)
            setIsAuthenticated(true);
            // Storing the token in LocalStorage
            localStorage.setItem('authToken', data.access_token);
    handletoastmessage(`${username} logged in Successfully`)
    if(!google_auth){
        setUserInfo(prevValues => ({
      ...prevValues,
      username: username,
      email_id: email_id,
    }));
    }
                navigate(`/data`);
        }
        else{
              setToken(data.access_token)
            setIsAuthenticated(false);
            // Storing the token in LocalStorage
            localStorage.setItem('authToken', data.access_token);
    handletoastmessage(`Log in failed due to ${data.insert_status}`)
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      })

  };
  useEffect(() => {
    if (!processSocket || !chatSocket) return;
      
    processSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'process') {
        setProcessMessage(data.message);
        // console.log("progress_message ",data.message);
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
    // console.log(chats);

    // console.log("zxzxzx");
    // console.log(valueList);
    // console.log(checkedValues);
    // console.log("back",new_message_from_backend);
  }
else{
      handletoastmessage(`Please Set a Valid API key`)
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
        deletechat={deletechat}
        isAuthenticated={isAuthenticated}
        handletoastmessage={handletoastmessage}
        userInfo={userInfo.username}
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
          isFilterToggleOn={isFilterToggleOn} 
          onFilterToggleChange={onFilterToggleChange} 
          isRerankToggleOn={isRerankToggleOn} 
          onRerankToggleChange={onRerankToggleChange} 
          handleApiKeyChange={handleApiKeyChange}
          handlePromptChange={handlePromptChange}
          userInfo={userInfo}
          />} 
          />
                    <Route path='/about' element={<About/>}/>
          <Route path='/' element={<Products
           isAuthenticated={isAuthenticated} />} />
          <Route path='/user' element={<UserDetail
           handleUserDetail={handleUserDetail} 
            isAuthenticated={isAuthenticated}/>} />
          {chats.map((chat) => (
                 <Route key={selectedChatId} path={`/chats/${chat.chatId}`}  element={<ChatPanel   
                  handlesetSelectedChatId={handlesetSelectedChatId}
                  selectedChatId={selectedChatId}
                  handleSendMessage={handleSendMessage}
                  getChatMessages={getChatMessages}
                  regenerateResponse = {regenerateResponse}
                   />} />
        ))}
    <Route  path="*" element={<About/>}/>
        </Routes>
      </div >
   
      </div >
                  <ToastContainer className={true}/>

    </div>
  );
};
export default App;
