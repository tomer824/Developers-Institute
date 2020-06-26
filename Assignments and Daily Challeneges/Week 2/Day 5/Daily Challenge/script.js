let beers = prompt("How many beers do we start with?")
beers = Number(beers)
let count = 1

function beer_drop(beers){
	for(i = beers; i > 0; count++){
		if(i - count >= 0){
		console.log(i + " bottles of beer on the wall")
		console.log(i + " bottles of beer")
		console.log("take " + count + " down, pass it around" )
		i -= count
		}
		else {
		console.log(i + " bottles of beer on the wall")
		console.log(i + " bottles of beer")
		console.log("take " + i + " down and no more bottles of beer")
		break
		}

	}
}


beer_drop(beers)