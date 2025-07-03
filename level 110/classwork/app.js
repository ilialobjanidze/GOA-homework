import React from 'react';
import Parent from './parent';

function App() {
  function handleTouch() {
    alert('Touch event triggered from Parent!');
  }

  return (
    <Parent onTouch={handleTouch}>
      <h1>child element</h1>
    </Parent>
  );
}

export default App;
