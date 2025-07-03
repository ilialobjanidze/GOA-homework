//A Promise in JavaScript is an object that represents the eventual completion (or failure) with functions  and has three states that are
//Pending, Fullfilled and rejected


const resolvedPromise = new Promise((resolve, reject) => {
    resolve("Promise resolved!");
});

resolvedPromise.then(result => {
    console.log(result);
});



const rejectedPromise = new Promise((resolve, reject) => {
    reject("Promise rejected");
});

rejectedPromise.catch(err => {
    console.log(err);
});



const conditionalPromise = new Promise((resolve, reject) => {
    const success = Math.random() > 0.5;
    if (success) {
        resolve("Promise resolved");
    } else {
        reject("Promise rejected ");
    }
});