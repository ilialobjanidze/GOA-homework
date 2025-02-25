class Car {
    constructor(brand, model, year, color) {
      this.brand = brand;
      this.model = model;
      this.year = year;
      this.color = color;
    }
  
    start() {
      console.log(`${this.brand} ${this.model} is starting...`);
    }
  
    drive() {
      console.log(`${this.brand} ${this.model} is driving...`);
    }
  }
  
  const car1 = new Car("Toyota", "Corolla", 2020, "Red");
  const car2 = new Car("Honda", "Civic", 2019, "Blue");
  const car3 = new Car("Ford", "Mustang", 2022, "Black");
  
  console.log(car1);
  car1.start();
  car1.drive();
  
  console.log(car2);
  car2.start();
  car2.drive();
  
  console.log(car3);
  car3.start();
  car3.drive();



  class Person {
    constructor(name, age) {
      this._name = name;
      this._age = age;
    }
  
    getname() {
      return this._name;
    }
  
    getage() {
      return this._age;
    }
  }
  