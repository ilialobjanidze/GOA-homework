//1 
const myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const slice1 = myArray.slice(0, 5);
const slice2 = myArray.slice(3, 8);
const slice3 = myArray.slice(-3);

//2
let today = new Date();
console.log(`day: ${today.getDate()}`);
console.log(`month: ${today.getMonth() + 1}`); 
console.log(`year: ${today.getFullYear()}`);
console.log(`minutes: ${today.getMinutes()}`);
console.log(`seconds: ${today.getSeconds()}`);


//3
function generatePassword(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+';
    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }
    return password;
}

const password = generatePassword(12);