class Car {
    constructor(brand, model) {
        this.brand = brand;
        this.model = model;
    }

    info() {
        return `${this.brand} ${this.model}`;
    }
}

class Animal {
    constructor(name, species) {
        this.name = name;
        this.species = species;
    }

    speak() {
        return `${this.name} is a ${this.species}.`;
    }
}

class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
    }

    details() {
        return `${this.title} by ${this.author}`;
    }
}






class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        return `${this.name} makes a sound.`;
    }
}

class Dog extends Animal {
    speak() {
        return `${this.name} barks.`;
    }
}

class Cat extends Animal {
    speak() {
        return `${this.name} meows.`;
    }
}

class Cow extends Animal {
    speak() {
        return `${this.name} moos.`;
    }
}



