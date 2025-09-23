

let num;

while(true){
    num = Number(prompt("type here number):"));
    
    if(num === 0){
        console.log("you entered zero.");
        break;
    }

    console.log("type num:", num);
}