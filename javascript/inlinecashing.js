function finduser(user) {
    return `found ${user.firstname} ${user.lastname}`

}

const userData={
    firstname:'Johnson',
    lastname:'Junior'
};

console.log(finduser(userData))
// 'found Johnson junior'


//hidden class 
function Animal(x,y){
    this.x=x;
    this.y=y;
}

const obj1 = new Animal(1,2)
const obj2 = new Animal(1,3)

obj1.a=300;
obj1.b=3;
obj1.b=370;
obj1.a=34;