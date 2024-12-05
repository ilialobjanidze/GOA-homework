// Adding event listener to the button
document.getElementById('checkAdultBtn').addEventListener('click', function() {
    // Asking the user if they are an adult using the confirm function
    let isAdult = confirm("Are you an adult?");
    
    // Checking the response from the confirm function
    if (isAdult) {
        console.log("You are Adult");  // User clicked "OK"
    } else {
        console.log("You are kid");    // User clicked "Cancel"
    }
});