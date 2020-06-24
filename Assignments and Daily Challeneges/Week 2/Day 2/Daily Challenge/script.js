let str1 = "This dinner is not that bad at all!"
let indexNot1 = str1.indexOf("not");
let indexBad1 = str1.indexOf("bad");


let str2 = "This movie is not so bad at all!"
let indexNot2 = str2.indexOf("not");
let indexBad2 = str2.indexOf("bad");

let str3 = "This dinner is bad at all!"
let indexNot3 = str3.indexOf("not");
let indexBad3 = str3.indexOf("bad");

if (indexNot1 > -1 && indexNot1 < indexBad1) {
	str1 = str1.substring(0, indexNot1) + "good" + str1.substring(indexBad1+3, str1.length);
	console.log(str1);
}

	else { console.log(str1)
}


if (indexNot2 > -1 && indexNot2 < indexBad2) {
	str2=str2.substring(0, indexNot2) + "good" + str2.substring(indexBad2+3, str2.length);
	console.log(str2 + "good")
}

	else {console.log(str2)
}


if (indexNot3 > -1 && indexNot3 < indexBad3) {
	str3=str3.substring(0, indexNot3) + "good" + str3.substring(indexBad3+3, str3.length);
	console.log(str3 + "good")
}

	else {console.log(str3)
}