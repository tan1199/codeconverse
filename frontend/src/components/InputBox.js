import React, { useState } from 'react';
import * as AiIcons from 'react-icons/ai';

const InputBox = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    setMessage(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.keyCode === 13) {
      e.preventDefault();
    }
    if (e.key === 'Enter' && message.trim() !== '') {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <div className="input-container">
            <textarea
        type="text"
        placeholder="Send a message..."
        value={message}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        className="input-box"
        autoFocus
        rows={1} // Start with a single row
        style={{ height: `${(message.split('\n').length + 1) * 4}vh`, 
          padding: `${(message.split('\n').length + 1) }vh` 
      }}
    
      />
      <button onClick={() => {onSendMessage(message);
          setMessage(''); // Clear the message after sending
        }
        }  className="send-button-chat"><AiIcons.AiOutlineSend color='white' size={30} /> </button>

    </div>
  );
};

export default InputBox;
