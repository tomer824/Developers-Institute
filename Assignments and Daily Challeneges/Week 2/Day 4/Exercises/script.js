// Practice 1

// function adding(num1, num2){
// 	console.log("The sum is " + (parseInt(num1) + parseInt(num2)))
// }

// pick1=prompt("enter first number")
// pick2=prompt("enter second number")

// adding(pick1, pick2)


// Practice 2

// function odd_or_even(num){
// 	if(parseInt(num) % 2 == 0){
// 		console.log("Your number is even")
// 	}
// 	else {
// 		console.log("Your number is odd")
// 	}
// }

// num = prompt("Please enter a number")

// odd_or_even(num)

// Practice 3

// ask user for their age and return as a number
// make a function that doubles it
// print on screen what twice their age is

function age(){
	return parseInt(prompt("What is your age?"))
}

function double(num){
	return num * 2
}


console.log("Double your age is " + double(age()))