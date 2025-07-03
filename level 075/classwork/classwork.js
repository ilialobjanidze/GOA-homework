
const form = document.getElementById('userForm');
const submitBtn = document.getElementById('submit');


form.addEventListener('submit', function(event) {
  event.preventDefault(); 

  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  console.log('Name:', username);
  console.log('Email:', email);
  console.log('Password:', password);
});



//ES6 (ECMASCRIPT6) is latest update of js that was released in 2016, it added many new useful functions.

//We use scope to lock functions,variables, and things like that out from code,we create some kind of space for them from where they cant get outt until we let them


//
const name = "Alex";
const age = 25;
const city = "Tbilisi";
//
console.log("My name is ${name}.");
console.log("I am ${age} years old.");
console.log("I live in ${city}.");
//

//
const age1 = 18;
const canVote = age1 >= 18 ? "Yes, you can vote!" : "No, you are too young.";
console.log(canVote);
//
//
const loggedIn = true;
const message = loggedIn ? "Welcome back!" : "Please log in.";
console.log(message);
//
//
const score = 85;
const grade = score >= 90 ? "A" : score >= 75 ? "B" : "C";
console.log(`Your grade is: ${grade}`);
//


//
let isAdult = false;
let age2 = 25;

if (age2 >= 18) {
  isAdult = true;
}

isAdult && console.log("You are an adult.");
//
//
let loggedIn1 = true;
let username = "Bondo";

loggedIn1 && console.log(`Welcome back, ${username}!`);
//


//
let user = {
    username: "Alice",
    age: 22
  };
  
  user.age >= 18 && console.log(`${username} is old enough to drive.`);
//  