const firstName = document.getElementById('first-name');
const lastName = document.getElementById('last-name');
const radioEnquiry = document.getElementById('enquiry');
const radioSupport = document.getElementById('support');
const message = document.getElementById('message');
const consentCheckbox = document.getElementById('contact-consent');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-form');

function firstNameValidation() {
    if (firstName.value.trim() === "") {
        firstName.style.border = "1px solid red";
    } else {
        firstName.style.border = "";
    }
}

function lastNameValidation() {
    if (lastName.value.trim() === "") {
        lastName.style.border = "1px solid red";
    } else {
        lastName.style.border = "";
    }
}

function radioValidation() {
    const queryOptionsContainer = document.querySelector('.query-options');
    if (!radioEnquiry.checked && !radioSupport.checked) {
        queryOptionsContainer.style.border = "1px solid red";
        queryOptionsContainer.style.borderRadius = "5px";
        queryOptionsContainer.style.padding = "10px";
    } else {
        queryOptionsContainer.style.border = "";
        queryOptionsContainer.style.padding = "";
    }
}

function messageValidation() {
    if (message.value.trim() === "") {
        message.style.border = "1px solid red";
    } else {
        message.style.border = "";
    }
}

function checkboxValidation() {
    const checkboxContainer = consentCheckbox.parentElement;
    if (!consentCheckbox.checked) {
        checkboxContainer.style.border = "1px solid red";
        checkboxContainer.style.borderRadius = "5px";
        checkboxContainer.style.padding = "10px";
    } else {
        checkboxContainer.style.border = "";
        checkboxContainer.style.padding = "";
    }
}

function validateAll() {
    firstNameValidation();
    lastNameValidation();
    radioValidation();
    messageValidation();
    checkboxValidation();
    emailValidation();
}

submitButton.addEventListener('click', (event) => {
    event.preventDefault();
    validateAll();
});
