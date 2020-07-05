let num = [];
let first_num;
let	second_num;
let operator = "";
let total = 0;
let equal;

function my_f(button)
	if(button == "+" || button == "-" || button == "*" || button == "/"){
		operator = button;
		first_num = parseInt(num.join());
	}
	else if(button = "=") {
		// second_num = convert num to string and then to number
		calc(first_num, operator, second_num)
	}
	else {
		num = push(button);
	}

function holding(array){
	num 
	// first num = convert array num to string and then to number
	// num = []

}


function calc(num1, operator, num2){
	total = // first_num operand num1 also turned into string and number
	console.log(total)
}


my_f()



// function my_f(button){
// 	if(typeof(button) == 'string' && button != "="){
// 		operator = button;
// 		first_num = parseInt(num1.join(""));
// 		num1 = []
// 		console.log(first_num)
// 	}
// 	else if(button == "=") {
// 		second_num = parseInt(num1.join(""));
// 		console.log(second.num)

// 		switch(operator){
// 			case "+":
// 				console.log(first_num + second_num)
// 				return first_num + second_num;
				
// 			case "-":
// 				console.log(first_num - second_num)
// 				return first_num - second_num;
				
// 			case "/":
// 				console.log(first_num / second_num)
// 				return first_num / second_num;

// 			case "*":
// 				console.log(first_num * second_num)
// 				return first_num * second_num;
// 		}
// 	}
// 	else {
// 	num1.push(button)
// 	}
// }


my_f()