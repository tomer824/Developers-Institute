// Use 3 differents for loops to add 5 to each number
// --> console.log the Array
// --> the result is :  [15, 25, 35]

// let arr = [10, 20, 30]

// for(let item of arr){
// 	item += 5
// 	console.log(item)
// }

// for(i = 0; i < arr.length; i++){
// 	arr[i] += 5
// 	console.log(arr[i])
// }

// for(let item in arr){
// 	item += 5
// 	console.log(item)
// }

// let div = document.body.children[0] // access div
// div.firstElementChild

// let lastElement = div.lastElementChild
// lastElement.previousSibling --> to get previous sibling of the element

// 1. Create a function called shopping, that takes 1 parameter --> Array
// 2. Inside the function, you have to go through the array and console.log each fruit that you bought
// 3. Call the function
// ​
// 4. Add 2 new parameters --> currency and amount of money
// 5. Mutiply the amount of money by 3.50 
// 6. Console log the amount you paid and the currency

let arr = ["Apple", "Banana", "Orange", "Watermelon"]

function shopping(arr, currency, money){
	for(let x of arr){
		console.log(x)
	}
	money *= 3.5
	console.log("I spent " + currency + money)
}

shopping(arr, "$", 150)