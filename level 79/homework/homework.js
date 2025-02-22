let a = 5;
let b = 10;

[a, b] = [b, a];






function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); 

let [first, second, ...others] = [1, 2, 3, 4, 5];
console.log(first);   
console.log(second);   
console.log(others);  


const person = { name1: 'Ilia', age: 15, job: 'Unemployed' };
const { name1, ...rest } = person;
console.log(name1);  
console.log(rest);  






let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];
console.log(arr2); 


let person1 = { name: 'Gela', age: 53 };
let personCopy = { ...person1, job: 'Technician' };
console.log(personCopy); 

function greet(name, age) {
    console.log(`Hello, my name is ${name} and I am ${age} years old.`);
}


