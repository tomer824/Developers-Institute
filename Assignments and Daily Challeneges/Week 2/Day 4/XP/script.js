// Exercise 1 - ask about bonus console logging

// function checkDriverAge(age) {

// 	if (Number(age) < 18) {
// 	alert("Sorry, you are too yound to drive this car. Powering off");
// 	} 
// 	else if (Number(age) > 18) {
// 	alert("Powering On. Enjoy the ride!");
// 	} 
// 	else if (Number(age) === 18) {
// 	alert("Congratulations on your first year of driving. Enjoy the ride!");
// 	}
// }

// checkDriverAge(prompt("What is your age?"))


// Exercise 2

// let amazonBasket = {
// 	'glasses': 1,
// 	'books': 2,
// 	'floss': 100
// }

// function checkBasket(){
// 	let item = prompt("What item are you looking for").toLowerCase()

// 	if(amazonBasket[item]){

// 		console.log("That is in your basket")
// 	}
// 	else {
// 		console.log("Not in your basket")
// 	}

// checkBasket()



// Exericse 3 - faster way to insert requested info (console.loging)

// let money = [5, 10, 15, 3]
// let purchase_price = 1

// function changeEnough(money_arr, total_due){
// 	let cash = 0;
// 	cash += money_arr[0] * 0.25;
// 	cash += money_arr[1] * 0.10;
// 	cash += money_arr[2] * 0.05;
// 	cash += money_arr[3] * 0.01;

	 
// 	if(cash >= total_due){
// 		console.log("You have enough change to afford the item")
// 	}
// 	else {
// 		console.log("You don't have enough money")
// 	}
// }

// changeEnough(money, purchase_price);



// Exercise 4

// let shoppingList = [
// 	{"name" : "banana", "quantity" : 5},
// 	{"name" : "orange", "quantity" : 13}
// 	{"name" : "apple", "quantity" : 8}
// 	]

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let total = 0


// function in_stock(item){
// 	return stock[item] > 0
// }

// function buy(item){
// 	if(item["quantity"] > stock[item["name"]]){
// 		item["quantity"] = stock[item["name"]]
// 	}
// 	total += (prices[item["name"]] * item["quantity"])
// 	stock[item["name"]] -= item["quantity"]
// }

// function my_bill()
// for(item of shoppingList)
// 	if(in_stock(item["name"])){
// 		buy(item["quantity"])
// 	}

// my_bill()


// Exericse 5

//1.
// function hotel_cost(){
// 	let nights = prompt("How many nights would you like to stay?")
// 	console.log(Number(nights) * 140)
// 	return Number(nights) * 140
// }


// // 2.

// let destination = {
// 	"London" : 183,
// 	"Paris"	: 220,
// }


// function plane_ride_cost(){
// 	let place = prompt("What is your destination")
// 	if(destination[place]){
		
// 		console.log(Number(destination[place]))
// 		return(Number(destination[place]))
// 	}
// 	else {
// 		console.log(300)
// 		return(300)
// 	}
// }

// plane_ride_cost()

// 3.

// function rental_car_cost() {
// 	let days = prompt("How many days would you like to rent the car?")
// 	days = Number(days)
	
// 	if(days <= 10){
// 		console.log(days * 40)
// 		return (days * 40)
// 	}
// 	else {
// 		console.log((days*40)* 0.95)
// 		return ((days * 40) * 0.95)
// 	}
//  }



// 4.

// function total_vacation_cost(hotel_cost, plane_ride_cost, rental_car_cost){
// 	let total = 0;
// 	total += hotel_cost
// 	total += plane_ride_cost
// 	total += rental_car_cost

// console.log(total)
// }

// total_vacation_cost(hotel_cost(), plane_ride_cost(), rental_car_cost())