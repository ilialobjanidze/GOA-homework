// Modularity means dividing a program into smaller, independent pieces (modules)
// that can be reused, tested, and maintained more easily.
//
// It improves code organization, readability, and helps avoid tangled dependencies.


// Modularity means dividing a program into smaller, independent pieces (modules)
// that can be reused, tested, and maintained more easily.



const numbers = [1, 2, 3, 4];


const doubled = numbers.map(n => n * 2);
console.log(doubled);


const strings = numbers.map(String);
console.log(strings); 


const numbers1 = [1, 2, 3, 4, 5, 6];


const evens = numbers1.filter(n => n % 2 === 0);
console.log(evens);

const greaterThanThree = numbers1.filter(n => n > 3);
console.log(greaterThanThree); 

