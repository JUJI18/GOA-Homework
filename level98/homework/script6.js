let userAge = Number(prompt("enter your age"))
let userName = prompt("enter your name")


if(userName === "nika" && userAge > 18){
    console.log("your name is nika and you are adult")
}


else if (userName === "dorblavaso" && userAge < 18){
    console.log("You are dorbla and you are too young")
}

else{
    console.log("you have weird name and age")
}