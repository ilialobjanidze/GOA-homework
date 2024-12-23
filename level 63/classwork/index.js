// 1
const person1 = {
    name: "Anna",
    age: 25,
    city: "Tbilisi"
};

const person2 = {
    name: "Giorgi",
    age: 30,
    city: "Kutaisi"
};

const person3 = {
    name: "Mariam",
    age: 22,
    city: "Batumi"
};


// 2 
function Car(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
}

const car1 = new Car("Toyota", "Corolla", 2015);
const car2 = new Car("BMW", "X5", 2020);
const car3 = new Car("Honda", "Civic", 2018);


// 3
class Person {
    constructor(name, age, city, occupation) {
        this.name = name;
        this.age = age;
        this.city = city;
        this.occupation = occupation;
    }
}

const person1 = new Person("Anna", 25, "Tbilisi", "Teacher");
const person2 = new Person("Giorgi", 30, "Kutaisi", "Engineer");
const person3 = new Person("Mariam", 22, "Batumi", "Student");

console.log(person1, person2, person3);


// 4 

function Animal(name, species, age) {
    this.name = name;
    this.species = species;
    this.age = age;
}

const animal1 = new Animal("Charlie", "Dog", 3);
const animal2 = new Animal("Mittens", "Cat", 2);
const animal3 = new Animal("Coco", "Parrot", 5);

console.log(animal1, animal2, animal3);



// 5
//A constructor function in JavaScript is used to create and initialize objects created from a class or function