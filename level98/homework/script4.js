let userInput = Number(prompt("Enter any number here:"))



if(userInput > 50 && userInput % 2 === 0){
    console.log("more than 50 and Even")
}

else if(userInput < 50 && userInput > 0 && userInput %2 !== 0 ){
    console.log("This number is less than 50 and more than 0 and is also Odd")
}

else if(userInput < 50 && userInput > 0 && userInput % 2 === 0){
    console.log("This number is less than 50 and more than 0 and is also Even")
}

else{
    console.log("this number is negative")
}