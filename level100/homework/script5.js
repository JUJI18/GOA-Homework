

let userNum1 = Number(prompt("enter num1 here"))
let userNum2 = Number(prompt("enter num2 here"))
let userNum3 = Number(prompt("enter num3 here"))



let max;
if(userNum1 >= userNum2 && userNum1 >= userNum3){
    max = userNum1;
}
else if (userNum2 >= userNum1 && userNum2 >= userNum3){
    max= userNum2
}
else{
    max = userNum3;
}


let min;
if(userNum1 <= userNum2 && userNum1 <= userNum3){
    min = userNum1;
}
else if(userNum2 <= userNum1 && userNum2 <= userNum3){
    min= userNum2
}
else {
    min = userNum3
}




console.log("yvelaze didi ricxvi aris", max);
console.log("yvelaze patara ricxvi aris", min);







if(max % 2 === 0){
    console.log("yvelaze didi ricxvi luwia")
    
}

else if(max %2 !== 0){
    console.log("yvelaze didi ricxvi kentia")
}

