//call stack+memory heap
// Call Stack = Manager ki To-Do List (kis function ko kab execute karna hai)
// Call Stack ek LIFO (Last In, First Out) data structure hai.
const no=610 // allocate the memory for no variable
const st='some text' // allocate some memory to the string
const human={ // allocate memory for an object.... and its value
    first:'vishant',
    last:'rathi'
};

// memory heap is simply a free store , it is the large region in  memory where js store data in unordered str
// Memory Heap = Store Room (jahan objects aur data store hote hain)
function calculate(){
    const sumTotal =4+5;
    return sumTotal;
}

console.log(calculate())
// call stack:
