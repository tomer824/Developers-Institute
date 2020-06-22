// Exercise 1

let me = ["my", "favorite", "color", "is", "blue"];
me = me.join();
console.log(me);


// Exercise 2

let str1 =  "mix";
let str2 = "pod";
let a = str1[0];
let b = str2[0];
str1 = str1.replace(str1[0], b);
str2 = str2.replace(str1[0], a);
console.log(str1);
console.log(str2);



// Exericse 3

let x = parseInt(prompt("Please enter a number"));
let y = parseInt(prompt("Please enter another number"));
let sum = (x + y)
alert("The sum of your numbers is " + sum);