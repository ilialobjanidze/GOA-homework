window.onload = function() {
    loadTasks();
  }
  

  function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();
    
    if (taskText) {
      const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
      tasks.push(taskText);
      localStorage.setItem('tasks', JSON.stringify(tasks));
  
      taskInput.value = ''; 
      renderTasks();
    }
  }
  

  function deleteTask(index) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.splice(index, 1);
    localStorage.setItem('tasks', JSON.stringify(tasks));
  
    renderTasks();
  }
  
  // Load tasks from localStorage and render them
  function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.forEach((task, index) => {
      const taskItem = document.createElement('li');
      taskItem.textContent = task;
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.onclick = () => deleteTask(index);
      taskItem.appendChild(deleteButton);
      document.getElementById('taskList').appendChild(taskItem);
    });
  }
  

  function renderTasks() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = ''; 
    loadTasks(); 
  }
  