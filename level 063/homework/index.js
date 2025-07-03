// 3. `this` is a keyword in JavaScript that refers to the object currently being worked on.

// 4.
class Computer {
    constructor(brand, processor, ram, storage) {
        this.brand = brand;
        this.processor = processor;
        this.ram = ram;
        this.storage = storage;
    }

    getSpecs() {
        return `${this.brand} with ${this.processor}, ${this.ram}GB RAM, ${this.storage} storage.`;
    }
}

const myComputer = new Computer("Dell", "Intel i7", 16, "512GB SSD");
console.log(myComputer.getSpecs());
class Keyboard {
    constructor(type, layout) {
        this.type = type;
        this.layout = layout;
    }

    description() {
        return `${this.type} keyboard with ${this.layout} layout.`;
    }
}

const myKeyboard = new Keyboard("Mechanical", "QWERTY");
console.log(myKeyboard.description());

class Bus {
    constructor(model, capacity, fuelType) {
        this.model = model;
        this.capacity = capacity;
        this.fuelType = fuelType;
    }

    info() {
        return `Bus model: ${this.model}, Capacity: ${this.capacity} passengers, Fuel: ${this.fuelType}.`;
    }
}

const myBus = new Bus("Mercedes Sprinter", 20, "Diesel");
console.log(myBus.info());
