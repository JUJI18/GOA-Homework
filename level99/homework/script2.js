

let userName = prompt("Enter your name:")

let userAge = Number(prompt("enter age here:"))


if(userName == "giorgi" && userAge >= 18){
    console.log("your name is giorgi and you are adult")
}

else if (userName == "nika" && userAge < 18 && userAge > 11){
    console.log("your name is nika and you are younger")
}


else if(userName == "saba" || userName == "irakli" && userAge < 11 && userAge > 5){
    console.log("you have nice name but you are too young")

}

else{
    console.log("you are not born yet D")
}
