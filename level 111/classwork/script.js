import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(prev => prev + 1);
  };

  return (
    <div>
      <p>Current count: {count}</p>
      <button onClick={handleClick}>Increase</button>
    </div>
  );
};

export default Counter;
