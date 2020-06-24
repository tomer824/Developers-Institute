// Exercise 1

// let age1 = parseInt(prompt("What is your birth year"))
// let age2 = parseInt(prompt("What is your friends birth year"))
// let bigger = 0
// let smaller = 0


//  if(age1 > age2) {
//  	bigger = age1;
//  	smaller = age2;
//  }
 else {
 	let bigger = age2;
 	let smaller = age1;
 }

let difference = bigger - smaller
let half = difference / 2

let result = bigger - half

	console.log(result)


// Exercise 2

let word = prompt("Please enter a word")
let num = word.length


	if(num <= 3) {
		console.log(word)
	}
	else if (num > 3 && word.substr(num-3) != "ing"){
		console.log(word + "ing")
	}
	else if (num > 3 && word.substr(num-3) == "ing"){
		console.log(word + "ly")
	}
