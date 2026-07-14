// JavaScript Runtime is the environment that executes JavaScript code. It consists of the Call Stack (for synchronous execution), Memory Heap (for storing objects), Web/Node APIs (for asynchronous operations), the Event Loop, and task queues (Microtask Queue and Callback Queue) to manage asynchronous execution.

//JavaScript Runtime =
// Call Stack
// + Memory Heap
// + Web APIs / Node APIs
// + Callback Queue
// + Microtask Queue
// + Event Loop


console.log('1')  // print immediately
setTimeout(()=>{console.log('2'),1000}); // send it to web and no  matter how fast it is it is always send to the web api   api and the js does not wait and execute next line
console.log('3')  // print immediately
// then second line prints 3
// so output likes
//1
//3
//2