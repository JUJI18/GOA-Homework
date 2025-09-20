

let userScore = Number(prompt("Type Score Here:"))

if(userScore <50){
    console.log("it's over, you're out!")

}

else if(userScore >= 50 && userScore <= 70){
    console.log("Medium Score")
}
else if(userScore >= 70 && userScore <= 90){
    console.log("Good Result!")
}
else if(userScore >=90 && userScore <=100){
    console.log("Best Reusult!")
}
else{
    console.log("Error...")
}