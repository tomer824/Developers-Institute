function frame(){
	let	words = prompt("Please enter several words seperated by commas").split(",")
	
	for(i in words){
		words[i] = words[i].trim();
	}
	
	let longest = 0

	for(word of words){
		if(word.length > longest){
			longest = word.length;
		}
	}

let star_line = "*".repeat(longest + 4)

console.log(star_line)

	for(word of words)
		console.log("* " + word + " ".repeat(longest-word.length + 1) + "*")

console.log(star_line)

}

frame()