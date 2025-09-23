

let num = Number(prompt("Enter number:"));

while (num !== 0) {
    if (num < 0) {
        console.log("negative number");
    } else if (num > 0) {
        console.log("You entered positive number");
    }


    num = Number(prompt("Enter number again:"));
}

console.log("you guessed the number, the loop is over");