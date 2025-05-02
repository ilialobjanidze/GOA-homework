let personCount = localStorage.getItem('personCount') || 0;

document.getElementById('personForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const age = document.getElementById('age').value;

  const person = { name, age };

  personCount++;
  localStorage.setItem(`person${personCount}`, JSON.stringify(person));
  localStorage.setItem('personCount', personCount);

  alert('Person saved!');
});