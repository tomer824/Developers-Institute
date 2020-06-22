// // Exercise 1

// let x = prompt("Enter a word")

// let y = x.replace(/a/ig, "1").replace(/e/gi,"2").replace(/i/gi,"3").replace(/o/gi,"4").replace(/u/gi,"5").replace(/y/gi,"6")

// console.log(y)



// Exercise 2

// let language = prompt("Do you prefer English, French or Hebrew?")
// let langlower = language.toLowerCase()

// switch(langlower) {
// 	case 'french':
// 		console.log("Bonjour")
// 		break;
// 	case 'english':
// 		console.log("Hello")
// 		break;
// 	case 'hebrew':
// 		console.log("Shalom")
// 		break;
// 	default:
// 		console.log(":)")
// }


// Exericse 3

// let grade = prompt("Please enter your grade")
// 	if (grade > 90) {
// 		console.log("A")
// 	}

// 	else if (grade > 80 && grade <= 90){
// 		console.log("B")
// 	}

// 	else if (grade > 70 && grade <= 80) {
// 		console.log("C")
// 	}

// 	else {
// 		console.log("D")
// 	}



// Exercise 4

zipcode = prompt("Please enter your zipcode")
numeral = isNaN(zipcode)

	if(zipcode.length == 5 && numeral == false) {
		console.log("Good")
	}
	else {
		console.log("Error")
}