import React, { useState, useEffect } from "react";

function App() {
  const [newMessage, setNewMessage] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(messages);
        
    fetch("http://localhost:8000/api/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: newMessage }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(messages);
        
        console.log(newMessage);
        setMessages([...messages, { text: newMessage, sender: "Me" }, { text: data.message, sender: "Bot" }]);
        // setMessages((prevMessages) => [
        //   ...prevMessages,
        //   { text: newMessage, sender: "Me" },
        // ]);

        // setMessages((prevMessages) => [
        //   ...prevMessages,
        //   { text: data.message, sender: "Bot" },
        // ]);
        console.log(messages);
        
        console.log(data.message);
        setNewMessage("");
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };


  return (
    <div>
      <h1>Chat App</h1>
      <div>
        {messages.map((message, index) => (
          <p key={index}>
            <strong>{message.sender}: </strong>
            {message.text}
          </p>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default App;
