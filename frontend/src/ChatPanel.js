import React, { useEffect,useRef } from 'react';
import ChatMessage from './components/ChatMessage';
import InputBox from './components/InputBox';
import './ChatPanel.css';

function ChatPanel({chatsize,selectedChatId,handleSendMessage,getChatMessages}) {

  const messagesEndRef = useRef(null)
  const selectedChatmeaages=getChatMessages(selectedChatId)
  const lengthofchat = selectedChatmeaages.length
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
  }, [chatsize]);

  console.log("whooo", chatsize);
// chatsize=1;
  return (
    <div>
        <div className="chat-panel">
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
            />
          ))}
          <div>
             {chatsize % 2 !== 0 ? (<div class="loader">Generating...</div>
):(<div></div>)
      }
      </div>
       
    
        </div>
              ):(<div>
                <div className='headingpanel'>Understand your codebase with GPT-4 and Semantic Code Search</div>
                <p className='parapanel'>👉🏼 We’re excited to share Code Converse, a novel to understand your codebase.</p>
                <p className='parapanel'>👉🏼 A blazing fast code search engine capable of understanding 5 languages</p>
                <p className='parapanel'>👉🏼 Precise code navigation, built on stack graphs and scope queries</p>
                <p className='parapanel'>👉🏼 An intelligent AI agent, powered by GPT-4 and semantic code search</p>


              
              
              
              </div>)}
              </div>
      ) : (
        <div>
          <h2>No chat selected</h2>
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

export default ChatPanel