function printName(){
    console.log("Vishant")
}

function findName(){
    return printName()
}

function sayMyName(){
    return findName()
}

sayMyName()  // js create the execution context 


// JavaScript Execution Context
// Definition
// Execution Context is the environment in which JavaScript code is executed. It contains all the information JavaScript needs to run the code, such as variables, functions, the value of this, and the scope chain.

// Simple Definition: An execution context is a workspace that JavaScript creates before executing your code.

// Types of Execution Context
// 1. Global Execution Context (GEC)
// Created once when the JavaScript program starts.

// It is the default execution context.

// Global variables and functions are stored here.

// In the browser, this refers to the window object.

// In Node.js, this refers to the global object (or module.exports depending on context).

// Example:

// JavaScript

// let name = "John";

// function greet() {
//     console.log("Hello");
// }
// 2. Function Execution Context (FEC)
// Created every time a function is called.

// Each function call gets its own separate execution context.

// It stores:

// Function parameters

// Local variables

// The value of this

// Scope information

// Destroyed after the function finishes execution.

// Example:

// JavaScript

// function add(a, b) {
//     return a + b;
// }

// add(5, 3);
// 3. Eval Execution Context
// Created when code is executed using the eval() function.

// Rarely used because it can make code slower and less secure.

// Generally not recommended.

// Example:

// JavaScript

// eval("console.log('Hello')");
