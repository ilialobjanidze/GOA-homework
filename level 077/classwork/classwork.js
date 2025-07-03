
const fruits1 = ["apple", "banana", "cherry"];
for (const fruit of fruits1) {
  console.log(fruit);
}

const name1 = "John";
for (const s of name1) {
  console.log(s);
}

const numbers = new Set([412, 2913, 83]);
for (const number of numbers) {
  console.log(number);
}

//for loop works on arrays, strings, sets, maps

const add = (a, b) => a + b;

const greet = (name = "User") => `Hello, ${name}!`;


const multiply = (a, b = 1) => a * b;


const formatName = (firstName, lastName = "Lobjanidze") => `${firstName} ${lastName}`;

const car = { brand: "Tesla", model: "Model 3", year: 2022 };
for (const key in car) {
  console.log(`${key}: ${car[key]}`);
}

const colors = ["red", "green", "blue"];
for (const index in colors) {
  console.log(`${index}: ${colors[index]}`);
}


//for...in works with objects, arrays and strings





const dog = {
    name: "Mia",
    age: 7,
    breed: "Husky",
    return() {
      return `${this.name} is a ${this.age}-year-old ${this.breed}.`;
    }
  };



  const key1 = "name";
const key2 = "age";
const person = {
  [key1]: "Gela", 
  [key2]: 64,      
  ["city" + "Name"]: "Gori" 
};


