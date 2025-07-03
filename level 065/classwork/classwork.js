// 1
const array1 = [1, 23, 51, 921, 231];


// 2
let array2 = new Array(1, 15, 415, 92, 71);


// 3
let array3 = new Array(5); 
array3[0] = 100;
array3[1] = 200;
array3[2] = 300;
array3[3] = 400;
array3[4] = 500;


// 4
console.log(array1[2]); 
console.log(array2[3]); 
console.log(array3[4]); 


// 5
console.log(array1.slice(1, 4)); 
console.log(array2.slice(0, 3)); 
console.log(array3.slice(2, 5)); 



// 6
function RandomNumber(n) {
  return Math.floor(Math.random() * 5);
}
console.log(getRandomNumber(10)); 


// 7
let counter = 0;
let interval = setInterval(function()  {
  console.log(counter);
  if (counter >= 30) {
    clearInterval(numbers); 
  }
}, 100); 


// 8
let today = new Date();
console.log("day: ${today.getDate()}"); 
console.log("month: ${today.getMonth()}");
console.log("year: ${today.getFullYear()}");