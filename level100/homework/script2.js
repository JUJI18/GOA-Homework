

let startnum = parseInt(prompt("enter start num here:"));
let endnum = parseInt(prompt("enter end num here:"));

let sum = 0;
let count = 0;





for (let i = startnum; i <= endnum; i++) {
    sum += i; 
    count++; 
}






let average = sum / count;








console.log("jami:", sum);
console.log("sashualo:", average);
