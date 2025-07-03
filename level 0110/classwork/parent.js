import React from 'react';

function Parent(props) {
  return (
    <div>
      <button onClick={props.onTouch}>Click me</button>
      <div>{props.children}</div>
    </div>
  );
}

export default Parent;
