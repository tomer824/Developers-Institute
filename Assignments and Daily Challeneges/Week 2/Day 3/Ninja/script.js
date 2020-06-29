//how to remove empty spaces

let user_input = prompt("Please enter a bunch of numbers, separated by commas: ");
let numbers = user_input.split(",");


for(item of numbers){
	item = parseFloat(item)
	if(item % 3 == 0){
		console.log(item + " is divisble by 3")

	}
	else {
		console.log(item + " is not divisble by 3")
	}
}