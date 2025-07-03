import React, { useState } from 'react';

const TodoList = () => {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  const handleAdd = () => {
    const trimmedTask = task.trim();
    if (trimmedTask === '') return;
    setTasks(prev => [...prev, trimmedTask]);
    setTask('');
  };

  return (
    <div>
      <input 
        type="text" 
        value={task}
        onChange={(e) => setTask(e.target.value)} 
        placeholder="Enter a task..."
      />
      <button onClick={handleAdd}>Add Task</button>

      <ul>
        {tasks.map((item, index) => (
          <li key={index}>{item}</li> 
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
