import React, { useState, useEffect } from 'react';
import AIimg from "../images/aiicon.avif";
import Userimg from "../images/usericon.png";
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { prism } from 'react-syntax-highlighter/dist/esm/styles/prism'; // Import desired syntax highlighting style
import { language } from 'react-syntax-highlighter/dist/esm/styles/prism'; // Import the language style you want to use
import { dark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { atomDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { nightOwl } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { dracula } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { materialDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { tomorrowNight } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { synthwave84 } from 'react-syntax-highlighter/dist/esm/styles/prism';
import * as prismstyle from 'react-syntax-highlighter/dist/esm/styles/prism';
const ChatMessage = ({ avatar, username, message, timestamp,chatindex,regenerateAnswer }) => {

    const [activeDiv, setActiveDiv] = useState(null);


  const handleCloseTooltip = (source_location) => {
console.log("ccchchch",chatindex)
regenerateAnswer(chatindex,source_location)
    setActiveDiv(null);
  };
  const handleMouseEnter = (divId) => {
    setActiveDiv(divId);
  };

  const handleMouseLeave = (delayTime=100) => {
     setTimeout(() => {
          setActiveDiv(null);
    }, delayTime);
  };

   useEffect(() => {

    document.addEventListener('click', handleMouseLeave);

    return () => {
      document.removeEventListener('click', handleMouseLeave);
    };
  }, []);
  const imageSource = chatindex % 2 === 0 ? Userimg : AIimg;
  const paragraphs = message.split('------------------------------------------------------------------------------------------');

  // Display the first paragraph as it is
  const answer = paragraphs[0].trim();

  // If there is a second paragraph, split it into lines
  const sources = paragraphs.length > 1 ? paragraphs[1].trim().split('\n') : null;

  const renderContent = (content) => {
    const splitText = (inputText) => {
      const parts = inputText.split(/(`[^`]+`)/); // Include the backticks in the capturing group
      return parts.map((part, index) =>
        part.startsWith('`') ? (
          <span key={index} className="highlighted-text">
            {part.slice(1, -1)} {/* Remove backticks */}
          </span>
        ) : (
          <span key={index} className='plain-text '>{part}</span>
        )
      );
    };
    // console.log("content",content);
    const lang = ['java','cpp','pyhthon','rust','json','sh' ,'javascript','go','kotlin','swift','php','csharp','ruby'];
    // const str = "```word\nThis is the first line.\nThis is the second line.\n``` Some other text ```another\nContent here.\n```";
    // const pattern = /```(\w+)\n([\s\S]*?)```/g;
    
    // const matches = [...content.matchAll(pattern)];
    
    // matches.forEach(match => {
    //   const fullMatch = match[0];
    //   const word = match[1];
    //   const content = match[2];
    //   console.log(`Word: ${word}`);
    //   console.log(`Content:\n${content}`);
    //   console.log('----------');
    // });
    const pattern = /```(\w+)\n([\s\S]*?)```/g;

let lastIndex = 0;
const matches = [];
let match;
const str=content;
const renderedSections = [];
while ((match = pattern.exec(str)) !== null) {
  const beforeMatch = str.substring(lastIndex, match.index);
  renderedSections.push(
    <div key={renderedSections.length} className="explanation">
      {splitText(beforeMatch)}
    </div>
  );
  matches.push({ type: 'text', content: beforeMatch });
  
  const word = match[1];
  const content1 = match[2];
  matches.push({ type: 'match', word, content });
  renderedSections.push(
    <SyntaxHighlighter key={renderedSections.length} language={word} style={prismstyle.dracula}  wrapLines={true} className='syntax-high'>
      {match[2]}
    </SyntaxHighlighter>
  );
  lastIndex = pattern.lastIndex;
}

const remainingText = str.substring(lastIndex);
if (remainingText) {
  matches.push({ type: 'text', content: remainingText });
  renderedSections.push(
    <div key={renderedSections.length} className="explanation">
      {splitText(remainingText)}
    </div>
  );
}

// matches.forEach(item => {
//   if (item.type === 'text') {
//     console.log(`Text:\n${item.content}`);
//   } else if (item.type === 'match') {
//     console.log(`Word: ${item.word}`);
//     console.log(`Content:\n${item.content}`);
//   }
//   console.log('----------');
// });
  //   const sections = content.split(/```(\w+)\n([\s\S]*?)```/g);
  //   const renderedSections = [];
  
  //   let explanation = ''; // Initialize explanation variable
  // console.log(sections)
  //   for (const section of sections) {
  //     console.log("in1",section);
  //     if (section.startsWith('```')) {
  //       // If it's a code block
  //       if (explanation) {
  //         // console.log("ine",section);

  //         // If an explanation exists, render it
  //         renderedSections.push(
  //           <div key={renderedSections.length} className="explanation">
  //             {explanation}
  //           </div>
  //         );
  //         explanation = ''; // Clear explanation
  //       }
  
  //       const [language, code] = section.split('\n', 2); // Split section into language and code
  //       if (language && code) {
  //         renderedSections.push(
  //           <SyntaxHighlighter key={renderedSections.length} language={language} style={nightOwl} className='syntax-high'>
  //             {code}
  //           </SyntaxHighlighter>
  //         );
  //       }
  //     } else {
  //       // If it's an explanation
  //       explanation += section; // Append to explanation
  //     }
  //   }
  
  //   // Render any remaining explanation
  //   if (explanation) {
  //     renderedSections.push(
  //       <div key={renderedSections.length} className="explanation">
  //         {explanation}
  //       </div>
  //     );
  //   }
  
    return renderedSections;
  };
  



  const codeString = ` 

def main():
    while True:
        try:
            progress()
        except Exception as e:
            print(e)
        time.sleep(60)


if __name__ == '__main__':
    main()
  `;
  return (
    <div className="chat-message">
      <div className="avatar">
        <img src={imageSource} alt="User Avatar" />
      </div>
      <div className="message-content">
        <div className="username">{username}</div>
        {/* <div className="message">{message}</div> */}
        {renderContent(answer)}
         {sources && (
        <div>
           <br />
            {/* <br /> */}
          <p className='source-heading'>Verified Sources:</p>
          <div className='sources'>
            {sources.map((link, index) => (
   
              <div className='source' key={index}>
                  {link.includes("github.com") ? (<a className="anchor-content" href={link.split(' ')[1]}  target="_blank" rel="noopener noreferrer" 
                    onMouseEnter={() => handleMouseEnter(index)}
                 onMouseLeave={() => handleMouseLeave(3000)}>
                   {index+1}) {link.split(' ')[0]} <p className='source-text'>{link.split(' ')[1].slice(19,)}</p>
                </a>) : (<div className="anchor-content" 
                    onMouseEnter={() => handleMouseEnter(index)}
                 onMouseLeave={() => handleMouseLeave(3000)}>
                   {index+1}) {link.split(' ')[0]} <p className='source-text'>{link.split(' ')[1]}</p>
                </div>)}
                
                         {activeDiv === index && (
            <div className="tooltip">
              {/* {div.explanation} */} 
              <button onClick={() => handleCloseTooltip(link.split(' ')[2])} className="tooltip-button">
                Regenrate 
              </button>
            </div>
              )}
              </div>
            ))}
          </div>
        </div>
      )}

        {/* 
        <SyntaxHighlighter language="python"  style={prismstyle.atomDark}  wrapLines={true} className='syntax-high'>
{codeString}
   </SyntaxHighlighter> */}
         {/* <div className="loader">Generating...</div>  */}

      </div>
    </div>
  );
};

export default ChatMessage;
