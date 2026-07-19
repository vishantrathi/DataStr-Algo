// it is the enviroment created every time we created the execution enviroment
// In javascript our lexical scope (available data + variables where the function was defined) determines our available variables. Not where the function is called (dynamic scope)

console.log('1-----')
// console.log(teddy)



//function expression
var sing2= function(){
    console.log('Uhh lala')
}
console.log(sing2())
//function declaration
function sing(){
    console.log(' ohh lala')
}
