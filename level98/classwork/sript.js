let userNumber = Number(prompt("enter number"))


if(userNumber > 0 && userNumber % 2 === 0){
    console.log("this number is positive and Even")
}else if (userNumber < 0 && userNumber % 2 !== 0){
    console.log("this number is Odd")
}else{
    console.log("This number is zero!")
}