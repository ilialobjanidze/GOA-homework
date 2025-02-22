

//array
const numbers = [51, 1349, 123494, 142, 3];
for (const num of numbers) {
    console.log(num);
}

//string
const text = "Hello";
for (const char of text) {
    console.log(char);
}

//set
const uniqueNumbers = new Set([40214, 1230, 512, 412]);
for (const num of uniqueNumbers) {
    console.log(num);
}

// it can also be used with map




//object
const person = { name: "Ilia", age: 15, city: "Tbilisi" };
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}

//arr
const car_type = ["BMW", "Mercedes", "Honda"];
for (const index in car_typ) {
    console.log(`${index}: ${car_type[index]}`);
}



const divide = (a, b) => a / b;
const your_car = car => `Hello, your car is: ${car}!`;
const square = num => num * num;



const user = {
    name: "Dato",
    greet() {
        console.log(`Hello, my name is ${this.name}`);
    }
};

const product = {
    name: "Laptop",
    price: 1350,
    withtax() {
        return this.price * 1.18;
    }
};

const counter = {
    count: 0,
    increment() {
        this.count++;
        console.log(`Count: ${this.count}`);
    }
};


// 7) Object.assign() 3-ჯერ

const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged1 = Object.assign({}, obj1, obj2);
console.log(merged1);




const defaultSettings = { theme: "light", fontSize: 14 };
const userSettings = { theme: "dark" };
const finalSettings = Object.assign({}, defaultSettings, userSettings);
console.log(finalSettings);




const target = { x: 1 };
const source1 = { y: 2 };
const source2 = { z: 3 };
Object.assign(target, src1, src2);
console.log(target);
