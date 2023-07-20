import React from 'react'
import {useParams} from "react-router-dom";

function ConversationPage(props) {
    const  { chatId } = useParams();

    // Sample chat messages (you can replace these with actual chat data)
    const chatMessages = [
      {
        id: 1,
        sender: "John",
        message: "Hey there!",
      },
      {
        id: 2,
        sender: "Jane",
        message: "Hi John, how are you?",
      },
      {
        id: 3,
        sender: "John",
        message: "I'm doing well, thank you!",
      },
      {
        id: 4,
        sender: "Jane",
        message: "That's great!",
      },
    ];
  
    return (
      <div className="conversation-container">
        <h3>Chat ID: {chatId}</h3>
        {chatMessages.map((message) => (
          <p key={message.id}>
            <strong>{message.sender}:</strong> {message.message}
          </p>
        ))}
        <button className="back-button" onClick={() => props.history.goBack()}>
          Back to Chat History
        </button>
      </div>
    );
  }

export default ConversationPage