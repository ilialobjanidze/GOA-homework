import React from 'react';

function App() {
  const handleClick = () => {
    const name = prompt("enter your name:");
    if (name) {
      alert(`Your name is: ${name}`);
    } else {
      alert("name was not entered.");
    }
  };

  return (
    <div>
      <button onClick={handleClick}>Click here</button>
    </div>
  );
}

export default App;
