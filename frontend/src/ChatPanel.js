import React, { useEffect,useRef } from 'react';
import ChatMessage from './components/ChatMessage';
import InputBox from './components/InputBox';
import './ChatPanel.css';

function ChatPanel({chatsize,selectedChatId,handleSendMessage,getChatMessages}) {

  const messagesEndRef = useRef(null)

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
          {getChatMessages(selectedChatId).map((message, index) => (
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