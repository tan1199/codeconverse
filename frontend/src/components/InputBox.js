import React, { useState } from 'react';

const InputBox = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    setMessage(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && message.trim() !== '') {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <div className="input-container">
            <textarea
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        class="input-box"
        autoFocus
        rows={1} // Start with a single row
        style={{ height: `${(message.split('\n').length + 1) * 30}px` }}
    
      />
      <button onClick={() => onSendMessage(message)}  class="send-button">Ask</button>

    </div>
  );
};

export default InputBox;
