

let userNum = Number(prompt("type number here:"));


let i = 1;
let even = 0;
let odd = 0;

while(i < userNum){
    if(i % 2 === 0){
        even++;
    }

    else{
        odd++;
    }

    i++;
}


console.log("ლუწის რაოდენობა", even);
console.log("კენტი რიცხვები", odd);