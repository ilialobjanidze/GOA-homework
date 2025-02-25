
let numbers = [512, 21, 23];
let [a, b, c] = numbers;
console.log(a, b, c); 


let moreNumbers = [312, 20, 430, 42150];
let [, second, , fourth] = moreNumbers;
console.log(second, fourth); 

let values = [7];
let [first, secondValue = 130] = values;
console.log(first, secondValue); 


let user = { name1: "Giorgi", age: 14 };
let { name1, age } = user;
console.log(name1, age); 

let car = { brand: "BMW", model: "M5" };
let { brand: carBrand, model: carModel } = car;
console.log(carBrand, carModel);

let person = { firstName: "Ilia" };
let { firstName, lastName = "Lobjanidze" } = person;
console.log(firstName, lastName); 

let [first1, second2, ...rest] = [1, 2, 3, 4, 5];
console.log(first1, second2); 
console.log(rest);

function sum(first, second, ...others) {
  console.log(first, second);
  console.log(others); 
}



let personInfo = { name2: "Aubameyang", age: 35, country: "Spain" };
let { name2, ...otherInfo } = personInfo;
console.log(name2);
console.log(otherInfo);

let arr1 = [3, 122, 4124];
let arr2 = [1239, 51, 3124];
let combined = [...arr1, ...arr2];
console.log(combined); 

//spread expands elements from an array or object, allowing you to merge, copy, or pass them as separate values


//rest collects remaining elements into an array or object when destructuring or handling function parameters