
const form = document.getElementById("myForm");

form.addEventListener("submit", function(event) {
  event.preventDefault(); 

  const textValue = document.getElementById("textInput").value;
  const emailValue = document.getElementById("emailInput").value;
  const passwordValue = document.getElementById("passwordInput").value;

  console.log("Text:", textValue);
  console.log("Email:", emailValue);
  console.log("Password:", passwordValue);
});
