

const myPassword = "12345";

let userPassword = prompt("Enter password:");

while (userPassword !== myPassword) {
    userPassword = prompt("Wrong password! Try again:");
}

console.log("you guessed");