import React, { useEffect,useRef } from 'react';
import ChatMessage from './components/ChatMessage';
import InputBox from './components/InputBox';
import './ChatPanel.css';
import { useLocation } from 'react-router-dom';

function ChatPanel({handlesetSelectedChatId,selectedChatId,handleSendMessage,getChatMessages,regenerateResponse}) {
  
  const location = (useLocation()).pathname;
      useEffect(() => {
        // Check if selectedChatId is null and pathname includes "/chats/"
        if (selectedChatId === null && location.includes("/chats/")) {
          console.log("alaaa")
          selectedChatId=parseInt(location.substring(7));
          handlesetSelectedChatId(selectedChatId);
        }
      }, [selectedChatId, location, handlesetSelectedChatId]);    
  const messagesEndRef = useRef(null)
  const selectedChatmeaages=getChatMessages(selectedChatId)
  const lengthofchat = selectedChatmeaages.length
  // console.log("qaxzs",selectedChatmeaages[0].message)
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }
  const regenerateAnswer = (index,source_location) => {
console.log("jnbhj",index-1,source_location)
regenerateResponse(selectedChatmeaages[index-1].message,selectedChatId,source_location)
  };
  useEffect(() => {
    scrollToBottom()
  }, [lengthofchat]);

  // console.log("lenofselectedchat", lengthofchat);
// chatsize=1;
  return (
    <div>
        <div className="chat-panel" style={{ backgroundImage: `url(/545.jpg)`,backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat', }}>
      <div className="chat-messages">
      {selectedChatId ? (
        <div>
              {lengthofchat > 0 ? (

          <div>
          {selectedChatmeaages.map((message, index) => (
            <ChatMessage
              key={message.id}
              avatar={message.avatar}
              username={message.username}
              message={message.message}
              timestamp={message.timestamp}
              chatindex={index}
              regenerateAnswer={regenerateAnswer}
            />
          ))}
          <div>
             {lengthofchat % 2 !== 0 ? (<div className="loader">Generating...</div>
):(<div></div>)
      }
      </div>
       
    
        </div>
              ):(<div>
                <div className='headingpanel'>Understand your codebase with GPT-4 and Semantic Code Search</div>
                <p className='parapanel'>🪄 We’re excited to share Code Converse, a novel to understand your codebase.</p>
                <p className='parapanel'>🪄 A blazing fast code search engine capable of understanding multiple languages</p>
                <p className='parapanel'>🪄 Precise code navigation, built on stack graphs and scope queries</p>
                <p className='parapanel'>🪄 An intelligent AI agent, powered by GPT-4 and semantic code search</p>


              
              
              
              </div>)}
              </div>
      ) : (
        <div>
          <h2>No chat selected</h2>
        <div>Current Route: {location.pathname}</div>
          <p>Select a chat from the sidebar or add a new chat window.</p>
        </div>
      )}
            <div ref={messagesEndRef} />
    </div>
    <InputBox
            onSendMessage={(message) => handleSendMessage(message, selectedChatId)}
          />
  </div>
    </div>  
  )
}

export default ChatPanel;