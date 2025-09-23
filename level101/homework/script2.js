

let start = Number(prompt("enter number here:"));
let end = Number(prompt("enter second number:"));

let sum = 0;
let i = start;



while(i <  end){
    if(i % 2 ===0){
        sum += i;

    }
    i++;
}


console.log("ლუწი რიცხვების ჯამი " + start + "–დან " + end + "–მდე არის:", sum);