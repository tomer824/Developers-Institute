// 1.

//const GUEST_LIST = {
// 	Randy : "Germany",
// 	Karla : "France",
// 	Wendy : "Japan",
// 	Norman: "England",
// 	Sam : "Argentina" 
// }

// let name = prompt("What is your name");
// name = name.charAt(0).toUpperCase() + name.slice(1);

// 	if (GUEST_LIST[name]) {
// 		console.log("Hi! I'm " + name + ", and I'm from " + 
// 			GUEST_LIST[name])
// 	}
// 	else {
// 		console.log("Hi! I'm a guest")
// 	}
	

// 2.

// let family = {
// 	james : 32,
// 	john : 14,
// 	sarah : 29,
// 	raquel : 7
// }

// for (let elem in family)
// 	console.log(elem)

// for (let elem in family)
// 	console.log(family[elem])



// 3.

// let building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 2000],
//         "Dan":  [4, 1000],
//         "David": [1, 10],
//     },
// }

// console.log(building.number_levels)
// console.log(building.number_of_apt_by_level["1"] + ", " + building.number_of_apt_by_level["3"])
// console.log(building.name_of_tenants[1])
// console.log(building.number_of_rooms_and_rent["Dan"][0])

// let rent_total = (building.number_of_rooms_and_rent["David"][1] + (building.number_of_rooms_and_rent["Sarah"][1]))

// if(rent_total > building.number_of_rooms_and_rent["Dan"][1]){
// 	building.number_of_rooms_and_rent["Dan"][1] = prompt("You need to increase the amount of Dan's rent. Please enter a new amount")
// }


// 4.

// Create two objects, each one should hold a person details. Here are the details: fullName, mass, height.
// Each object should also have a property which value is a function that calculates the Body Mass Index (BMI) of each person
// Create a JS function that compare both the BMI. Display the name of the person that has the biggest BMI.

let person1 = {
	"John": [200, 73],
	}

	let person2 = {
	"Mary": [150, 66],
	}

function calc_bmi(){
	body_mass_index(person1["John"][0], person1["John"][1])
	body_mass_index(person2["Mary"][0], person2["Mary"][1])

}

function body_mass_index(mass, height){
	let bmi = mass / height
	console.log(bmi)
}

calc_bmi()