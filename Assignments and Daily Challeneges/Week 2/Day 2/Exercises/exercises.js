// Exercise 1

// let age = prompt("What is your age?")

// if(age < 18) {
// 	alert("Sorry, you are too young to drive this car. Powering off")
// }
	
// 	else if (age == 18) {
// 		alert("Congratulations on your first year of driving. Enjoy the ride!")
// 	}

// 	else {
// 		alert("Powering on. Enjoy the ride!")
// 	}


// Exercise 2
// 	let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

let a = 2 + 2;

switch (a) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}