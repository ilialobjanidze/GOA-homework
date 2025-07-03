document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    let isValid = true;
  

    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const gender = document.getElementById('gender');
    const country = document.getElementById('country');
    const terms = document.getElementById('terms');
  

  
    if (!terms.checked) {
      alert('You must agree to the Terms & Conditions to register.');
      isValid = false;
    }
  
    if (isValid) {
      alert('Registration successful!');
      document.getElementById('registrationForm').reset();
    }
  });
  