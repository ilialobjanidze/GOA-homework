//1
// JSX stands for JavaScript XML.
// it allows us to write HTML-like code inside JavaScript.
// JSX is used in React to describe what the UI should look like.



//2
//virtual DOM is a copy of the real DOM, but it exists in memory,but not in the browser.


//3
import React from 'react';
function NameList() {
  const names = ['Gela', 'Nika', 'Luka', 'Mari', 'Ana'];

  return (
    <ul>
      {names.map((name, index) => (
        <li key={index}>{name}</li>
      ))}
    </ul>
  );
}

