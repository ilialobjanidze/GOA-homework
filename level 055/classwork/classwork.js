const form = document.getElementById('myForm');

form.addEventListener('submit', function(event) {

  event.preventDefault();
  const textValue = form.elements['textInput'].value;
  console.log(textValue);
});