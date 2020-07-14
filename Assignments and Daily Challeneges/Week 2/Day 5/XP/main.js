let num = [];
let first_num;
let	second_num;
let operator = "";
let total = 0;
let equal;

function my_f(button){
	if(button == "+" || button == "-" || button == "*" || button == "/"){
		operator = button;
		first_num = parseInt(num.join(""));
		console.log(first_num + " " + operator)
		num = [];
	}
	else if(button == "=") {
		// second_num = convert num to string and then to number
		second_num = parseInt(num.join(""));
		calc(first_num, operator, second_num)
	}
	else {
		num.push(button);
		console.log(num)
	}
}


function calc(num1, operator, num2){
	switch(operator){
		case "+":
			console.log(first_num + second_num)
			break
			// return first_num + second_num
		case "-":
			console.log(first_num - second_num)
			break
			// return first_num - second_num
		case "*":
			console.log(first_num * second_num)
			break
			// return first_num * second_num
		default:
			console.log(first_num / second_num)
			break
			// return first_num / second_num	
	}
}

my_f()
