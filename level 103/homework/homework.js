import React, { useState } from "react";

function Contact() {
  // The hardcoded password to authorize access
  const password = "swordfish";
  
  // State variable to track whether the user is authorized
  const [authorized, setAuthorized] = useState(false);

  // Function to handle form submission (password entry)
  function handleSubmit(e) {
    e.preventDefault(); // Prevent page refresh on form submit

    // Get the value entered in the password input field
    const enteredPassword = e.target.querySelector('input[type="password"]').value;
    
    // Check if the entered password matches the stored password
    const auth = enteredPassword === password;
    
    // Update the authorized state based on the password check
    setAuthorized(auth);

    // The following variables are declared here but not used inside this function.
    // They should be declared outside or within the component return statement.
    const login = (
      <form action="#" onSubmit={handleSubmit}>
        <input type="password" placeholder="Password" />
        <input type="submit" />
      </form>
    );
    
    const contactInfo = (
      <ul>
        <li>client@example.com</li>
        <li>555.555.5555</li>
      </ul>
    );
  }

  // JSX returned by the component
  return (
    <div id="authorization">
      {/* Show different heading depending on authorization */}
      <h1>{authorized ? "Contact" : "Enter the Password"}</h1>
      
      {/* Conditionally render contact info or login form */}
      {authorized ? (
        <ul>
          <li>client@example.com</li>
          <li>555.555.5555</li>
        </ul>
      ) : (
        <form action="#" onSubmit={handleSubmit}>
          <input type="password" placeholder="Password" />
          <input type="submit" />
        </form>
      )}
    </div>
  );
}

export default Contact;
