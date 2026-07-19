//Function Expression
var Canada=()=>{
    console.log('cold')
}


// fn declaration
function india(){
    console.log('warm')
}

//fn invocation
Canada()
india()

function marry(person1,person2)
{
    console.log(arguments)
    return`${person1} is now married to ${person2}`
}

console.log(marry('Tim','Tina'))