

let userNum = prompt("Enter Number Here:")


if(typeof userNum === "string" && isNaN(Number(userNum))){
    console.log("you entered string number,so you are wrong")
}

else{

    let number = Number(userNum);
   
    
    
    (typeof userNum === Number)
    for(let i = 1; i <= userNum; i++)
        if(i % 2 !== 0){
            console.log(i);
        }
}

