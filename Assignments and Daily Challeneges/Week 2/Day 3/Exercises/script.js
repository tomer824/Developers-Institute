// for(let i = 0 ; i < 16 ; i++){

// 	if(i % 2 == 0){
// 		console.log(i + " is even");
// 	}

// 	else {
// 		console.log(i + " is odd");
// 	}
// }



// 1. Loop through the array of object
// 2. If the username is Sarah : say hello to her friends (display the name of her friends)
// 3. If the username is Dan : change his password to 567
// ​
// --> can use switch


// let users = [
//     {
//         username: "Sarah",
//         password: 123,
//         friends: ["max", "tom"]
//     },
//     {
//         username: "Dan",
//         password: 433
//     }
// ]


// for(let person of users){
// 	if(person.username === "Sarah"){
// 		for(let partner of person.friends){
// 		console.log("Hello Sarah and " partner)
// 		}
// 	}
// 	else if (person.username ==="Dan"){
// 		console.log(" ")
// 	}
// 	else {
// 		console.log("I don't know you")
// 	}
// }


// for(let person of users){
// 	if(person.username ==="Sarah"){
// 		console.log("My friends are " person.friends[0], person.friends[1])
// 	}
// 	else if (person.username ==="Dan"){
// 		console.log("My password is " person.password)
// 	}
// }


// While Loops

// let counter = 1

// while (counter < 10){
// 	console.log("counter is", counter)
// 	counter++
// }


// Exercise 3

let names = ["john", "sarah", 23, "Rudolph", 34];

	for (let i of names){
		if(typeof(i) != "string"){
			continue;
		}
		
		else {
			let first_letter = i.charAt(0);
			let to_upper = first_letter.toUpperCase();
			if (first_letter != to_upper){
				i = to_upper + i.substring(1, i.length);
			}
			console.log(i);
		}
	}

		