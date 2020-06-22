// // Exercise 1
// let x = 15
// let y = 20

// if(x > y){
// 	console.log(x)
// }
// 	else if(x < y) {
// 		console.log(y)
// 	}

// 	else {
// 		console.log("They are even")
// 	}

//// Exericse 2

// let newDog = "Chihuahua"
// let length=newDog.length
// let upper=newDog.toUpperCase(newDog)
// let lower=newDog.toLowerCase(newDog)

// console.log(length, upper, lower)

// Exericse 3

// let g = prompt("Please enter a number")
// let h = parseFloat(g)

// if (h % 2 == 0) {
// 	console.log(g + " is an even number.")
// }
// 	else {
// 		console.log(g + " is not an even number.")
// }


// Exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "heloo@00"]
let onlineUsers = parseFloat(prompt("How many people are online?"))

if (onlineUsers < 1) {
	console.log("no one online")
}
	else if(onlineUsers == 1){
		console.log(`${users[0]} onlineUser`)
	}

	else if(onlineUsers == 2)
		console.log(`${users[0]} and ${users[1]} online`)

	else if(onlineUsers >= 2)
		console.log(`${users[0]} ${users[1]} and ${onlineUsers-2} more online`)	