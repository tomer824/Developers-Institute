// Exercise 1

// let colors = ["red", "blue", "green", "yellow", "purple", "orange"]

// 	for(i in colors){
// 		console.log("My #" + (Number(i)+1) + " choice is " + colors[i])

// 	}



// Exericse 2

// let names = ["Jack", "Phillip", "Sarah", "Amanda","Bernard", "Kyle"]

// names.sort();
// let final = '';

// 	for(name of names){
// 		final += name.charAt(0)
// 	}

// console.log(final)

// Exericse 3

// let num = prompt("Please enter a number")
// num = parseInt(num)

// 	while(num < 10){
// 		num = prompt("Please enter another number");
// 	}

// Exericse 4

// let people = ["Greg", "Mary", "Devon", "James"]

// // 1.
// 	for(person of people){
// 		console.log(person)
// 	}

// //  2.
// 	people.shift();
// 	console.log(people)

// // 3.
// 	people.splice(people.indexOf("James"), 1, "Jason")
// 	console.log(people)

// // 4.
// 	people.push("Tomer")
// 	console.log(people)

// // 5.
// 	for(person of people){
// 		console.log(person)
// 		if(person =="Mary"){
// 			break
// 		}
// 	}

// // 6. 
// 	let people_copy  = people.slice(0, people.indexOf("Mary"))
// 	console.log(people_copy) 
	
// 	people_copy += people.slice(people.indexOf("Mary") + 1, people.indexOf("Tomer"))
// 	console.log(people_copy)
	
// 	people_copy += people.splice(people.indexOf("Tomer") + 1)
// 	console.log(people_copy)
// 	console.log(people)

// // 7.
// 	console.log(people.indexOf("Mary"))

// // 8.
// 	console.log(people.indexOf("Foo"))

// // 9.

// 	let last = (people[people.length -1])
// 	console.log(last)



// Exericise 5 - need explanation!

// let age = [20, 5, 12, 43, 98, 55];
// let sum = 0;

// 	for (let i = 0; i < age.length; i++){
// 		sum += parseInt(age(i));
// 	}
	
// 	console.log(sum)

