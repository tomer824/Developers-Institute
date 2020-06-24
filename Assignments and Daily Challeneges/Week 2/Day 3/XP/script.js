// Exercise 1

// let colors = ["red", "blue", "green", "yellow"]
// let x = 1

// 	for(let i = 0; i < colors.length; i++, x++){
// 		console.log(`My # ${x} choice is  ${colors[i]}`)

// 	}



// Exericse 2

// let names = ["Jack", "Phillip", "Sarah", "Amanda","Bernard", "Kyle"]

// let ordered = names.sort();
// let final = []
// let initials;

// 	for (let i = 0; i < ordered.length; i++){
// 		initials = ordered[i];   
// 		initials = initials.charAt(0); 
// 		final.push(initials);  
// 	}
// 	final = final.join('')
	
// 	console.log(final)


// Exericse 3

// let num = prompt("Please enter a number")
// num = parseInt(num)

// 	while(num < 10){
// 		num = prompt("Please enter another number");
// 	}

// Exericse 4

let people = ["Greg", "Mary", "Devon", "James"]
let x = 0
let arr = x
let copy = []

	for(let i = 0; i < people.length; i++){
		console.log(people[i])
	}
		people.shift()
		console.log(people)
		people.splice(2, 1, "Jason")
		console.log(people)
		people.push("Tomer")
		console.log(people)

		for(let x = 0; x < people.length;  x++){
			if(people[x] != "Mary"){
				console.log(people[x])
			}
			else {
				console.log(people[x])
				break
			}
		}

		for(let y = 0; y < people.length; y++)
			if(people[y] != "Mary" && people[y] != "Tomer"){
				let z = people.slice(y, y + 1)
				z = String(z)
				copy.push(z)
			}
			else {
				continue
			}
			console.log(copy)

		// 	(let x = 0; people[x] != "Mary"; x++)
		// 	console.log(people[x])
		// let copy = people.slice[1, 2]
		// 	console.log(copy)
		
		// let index = people.indexof("Mary")
		// console.log(`Mary is at index ${index}`)
		




// Exericise 5 - need explanation!

// let age = [20, 5, 12, 43, 98, 55];
// let sum = 0;

// 	for (let i = 0; i < age.length; i++){
// 		sum += parseInt(age(i));
// 	}
	
// 	console.log(sum)

