document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const gender = document.querySelector('input[name="gender"]:checked')?.value;
    const termsChecked = document.getElementById('terms').checked;


 

    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Gender:", gender);
    console.log("Terms accepted:", termsChecked);

    alert("Succesfuly registered");

});
document.getElementById('registrationForm').reset();  