

const myName = "Tornike";

let attempts = 0;


let userInput = "";

while (userInput !== myName) {
    userInput = prompt("Enter my name:");

    if (userInput !== myName) {
        attempts++;
    }
}

console.log("You guessed my name and your attempts is: " + attempts);