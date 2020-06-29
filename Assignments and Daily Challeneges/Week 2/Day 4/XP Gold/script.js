let userNumber;
let computerNumber;
let answer = confirm("Would you like to play a game?")

function playTheGame(){

		if(answer == false){
			alert("No problem, Goodbye")
		}
		else{
			userNumber = Number(prompt("Please enter a number between 1 - 10"));
			if(!userNumber){
				userNumber = alert("Sorry, Not a Number. Please re-enter a number")
				playTheGame()
			}
			else if(userNumber <= 0 || userNumber > 10){
				userNumber = alert("Sorry, its not a good number, Please re-enter a good number")
				playTheGame()
			}
			else {
				computerNumber = (Math.floor(Math.random() * 10) + 1)
				test(userNumber, computerNumber)
			}
		}
}

function test(userNumber, computerNumber){
	if(userNumber == computerNumber){
		alert("You won the game")
	}
	else if(userNumber > computerNumber){
		userNumber = alert("Your number was bigger, please guess again")
		playTheGame()
	}
	else if(userNumber < computerNumber){
		userNumber = alert("Your number was smaller, please guess again")	
		playTheGame()
	}
}

playTheGame()

