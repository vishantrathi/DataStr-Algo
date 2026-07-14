//Jab program aisi memory ko hold karke rakhta hai jo ab use nahi ho rahi, lekin uska reference abhi bhi exist karta hai. Isliye Garbage Collector us memory ko free nahi kar pata.

let user = {
    name: "Johnson"
};

user = null;  //no memory leak

let users = [];


// memory leak
function addUser() {
    users.push({
        name: "John"
    });
}

addUser();
addUser();
addUser();

//global variable
let data = {
    bigArray: new Array(1000000)
};