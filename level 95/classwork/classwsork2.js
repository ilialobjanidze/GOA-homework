document.getElementById('userForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('uname').value;
    const age = document.getElementById('uage').value;

    const newUser = { name, age };

    // Get existing list or create empty one
    const existingUsers = JSON.parse(localStorage.getItem('users')) || [];

    existingUsers.push(newUser);
    localStorage.setItem('users', JSON.stringify(existingUsers));

    alert('User added to list!');
  });