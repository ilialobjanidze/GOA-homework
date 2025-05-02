//1
let age = 18;
let status = age >= 18 ? "Adult" : "Minor";  

let isLoggedIn = false;
let message = isLoggedIn ? "Welcome back!" : "Please log in.";  

let score = 85;
let grade = score > 90 ? "A" : score > 75 ? "B" : "C";  



//2
let nums = [1, 2, 3, 4];

// map
let doubled = nums.map(n => n * 2); 

// filter
let even = nums.filter(n => n % 2 === 0);  

// map with filter
let squaredEvens = nums.filter(n => n % 2 === 0).map(n => n ** 2);  




//3
let username = null;
let name = username ?? "Guest";  

let value = 0 ?? 5;  

let data = undefined ?? "Default";  




//4
let user = { profile: { name: "Tom" } };
console.log(user.profile?.name);

let noUser = null;
console.log(noUser?.profile?.name); 

let arr = [10, 20];
console.log(arr?.[1]); 


//5
let p = new Promise((res, rej) => setTimeout(() => res("Done"), 1000));
p.then(console.log); 

async function getData() {
  return "Data loaded";
}
getData().then(console.log);  

async function fetchUser() {
  try {
    let response = await fetch('https://api.example.com/user');
    let data = await response.json();
    console.log(data);
  } catch (err) {
    console.error("Error:", err);
  }
}
