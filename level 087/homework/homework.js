//1

const promise1 = new Promise((resolve) => {
    resolve("Hello, Promise!");
  });
  
  promise1.then((message) => console.log(message));
  

//2
const promise2 = new Promise((resolve, reject) => {
    reject("Something went wrong!");
  });
  
  promise2.catch((error) => console.log(error));
  
  
//3

const promise3 = new Promise((resolve) => {
    setTimeout(() => {
      resolve("2 seconds have passed");
    }, 2000);
  });
  
  promise3.then((message) => console.log(message));
  




//4
const promise4 = new Promise((resolve, reject) => {
    const random = Math.random();
    if (random > 0.5) {
      resolve("Success!");
    } else {
      reject("Failed!");
    }
  });
  
  promise4
    .then((message) => console.log(message))
    .catch((error) => console.log(error));

    
//5
const promise5 = new Promise((resolve) => {
    resolve(5);
  });
  
  promise5
    .then((number) => number * 2)
    .then((number) => number * 2)
    .then((number) => console.log(number));  
    
    

//6

const promise6 = new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data fetched!");
    }, 1000);
  });
  
  promise6.then((message) => console.log(message));
  