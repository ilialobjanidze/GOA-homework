// index.js

// Import the calculator and filter functions from calculator.js
import { calculator, filter } from './calculator.js';

function isEven(num) {
    return num % 2 === 0;
}

const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = filter(numbers, isEven);
console.log(`Even numbers: ${evenNumbers}`);

const resultAdd = calculator(10, 5, "add");
console.log(`Addition result: ${resultAdd}`);

const resultMultiply = calculator(10, 5, "multiply");
console.log(`Multiplication result: ${resultMultiply}`);
