let addressNumber = "112"
let addressStreet= "Ibn Gvirol"
let country= "Israel"
let global_address = addressStreet + " " + addressNumber + " " + country

console.log("I live at " + global_address)

let birthYear = 1987
let futureYear = 2030
let futureAge = futureYear - birthYear
console.log("I will be " + futureAge + " in " + futureYear)
console.log(`I will be ${futureAge} in ${futureYear}`)

let repeatTest = "Hello\n"
console.log(repeatTest.repeat(5))

let money = 123.888
let roundMoney = money.toFixed(2)
console.log(roundMoney);

let op = Boolean(10>9)
console.log(op)
console.log(Boolean(20>30))


let stuff = ["blue", "red", "yellow", 12, "pink"]
console.log(stuff[1])
console.log("length " + stuff.length)
console.log(stuff[stuff.length - 1])

stuff[0] = "green"
console.log(stuff)

let colors = ["blue", ["pink", "yellow"]]
console.log(colors[1][1])

let lastElement= stuff.pop()
console.log(stuff.pop())
console.log(stuff)

stuff.push("grey")
console.log(stuff)

stuff.splice(2, 1, "black", "green")
console.log(stuff)

// position 3 is not included
let favoriteColors = stuff.slice(1, 3)
console.log("the stuff array ", stuff)

console.log("my favorite color : ", favoriteColors)

let pets=["cat", "dog", "fish", "rabbit", "cow"]
console.log(pets[1])

pets.push("horse")
pets.splice(3, 1)
console.log(pets)