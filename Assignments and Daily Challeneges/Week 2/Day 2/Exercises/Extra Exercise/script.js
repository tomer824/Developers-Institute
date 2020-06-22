// 1) get the numberPets
// 2) get teh 2nd type of pet
// 3) what is the favorite food of cat

let users = [
	{
		username : "Sarah",
		password: 123,
		friends: ["max", "tom"],
		pets: {
			numberPets : 2,
			typePets : ["dog", "cat"],
			favoriteFood : {
				dog : "candy",
				cat : "milk"
			}
		}
	}

]

// numberPets - 0 is the first position then call each item with a period
console.log(users[0].pets.numberPets)

//2nd type of pet - only 1 array so position 0
console.log(users[0].pets.typePets[1])

// favorite food of cat - call each object one by one with a period
console.log(users[0].pets.favoriteFood.cat)



