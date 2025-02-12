let age = 18;
let status1 = (age >= 18) ? 'Adult' : 'Minor';
console.log(status1);  

let number = 5;
let result = (number % 2 === 0) ? 'Even' : 'Odd';
console.log(result); 

let temperature = 30;
let weather = (temperature > 25) ? 'Hot' : 'Cool';
console.log(weather); 

let isLoggedIn = true;
let hasPermission = true;
let canAccess = isLoggedIn && hasPermission;
console.log(canAccess);  

let age1 = 22;
let hasID = false;
let canBuyAlcohol = age1 >= 18 && hasID;
console.log(canBuyAlcohol); 

let isMember = false;
let isPremium = true;
let canAccessContent = isMember && isPremium;
console.log(canAccessContent); 

function testScope() {
    if (true) {
      var varVariable = 'Var variable';
      let letVariable = 'Let variable';
      const constVariable = 'Const variable';
    }
    console.log(varVariable); 
    console.log(letVariable); 
    console.log(constVariable); 
  }
  
  