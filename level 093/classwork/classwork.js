
const add = (a, b) => a + b;

const greet = () => console.log("Hello!");

const multiply = (a, b) => {
  const result = a * b;
  return result;
};



const name1 = "Gela";
const greeting = `Hello, ${name1}!`;

const a = 5, b = 10;
const sumText = `Sum is ${a + b}`;



function greet(name2 = "Guest") {
    return `Hello, ${name2}`;
  }

  function sum(a = 0, b = 0) {
    return a + b;
  }

  function createProfile(user = { name: "Anonymous", age: 0 }) {
    return user;
  }
  



  //  Rest
function total(...numbers) {
    return numbers.reduce((sum, n) => sum + n, 0);
  }
  
  //  Spread
  const arr1 = [1, 2, 3];
  const arr2 = [...arr1];
  
  //  Spread
  const user = { name: "Ana" };
  const fullUser = { ...user, age: 25 };
  