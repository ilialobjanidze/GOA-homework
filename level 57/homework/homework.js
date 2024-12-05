// Event listener is attached to the 'submit' event of the registration form
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    // Prevents the default form submission behavior, which would reload the page
    event.preventDefault(); 

    // Grabbing the values from the input fields
    const name = document.getElementById('name').value; // Get value of the 'name' input field
    const email = document.getElementById('email').value; // Get value of the 'email' input field
    const password = document.getElementById('password').value; // Get value of the 'password' input field
    
    // Get the selected value from the radio buttons for gender (if any is selected)
    const gender = document.querySelector('input[name="gender"]:checked')?.value;

    // Check if the 'terms' checkbox is checked
    const termsChecked = document.getElementById('terms').checked;

    // Log the gathered information to the console
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Gender:", gender);
    console.log("Terms accepted:", termsChecked);

    // Display a success message as an alert
    alert("Successfully registered");
});

// Reset the form fields after submission (if needed)
document.getElementById('registrationForm').reset();
