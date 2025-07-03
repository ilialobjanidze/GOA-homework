document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let isValid = true;
    
    document.querySelectorAll("input, select").forEach(input => {
        input.classList.remove("error");
    });

    let name = document.getElementById("name");
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let gender = document.getElementById("gender");
    let country = document.getElementById("country");
    let terms = document.getElementById("terms");

    if (name.value === "") {
        name.classList.add("error");
        isValid = false;
    }
    if (email.value === "") {
        email.classList.add("error");
        isValid = false;
    }
    if (password.value === "") {
        password.classList.add("error");
        isValid = false;
    }
    if (gender.value === "") {
        gender.classList.add("error");
        isValid = false;
    }
    if (country.value === "") {
        country.classList.add("error");
        isValid = false;
    }
    if (!terms.checked) {
        alert("You must agree to the Terms & Conditions.");
        isValid = false;
    }
    if (isValid) {
        alert("Registration successful!");
    }
});