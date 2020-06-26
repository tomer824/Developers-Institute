// Hint: The algorithm is called “Bubble Sort”
// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Using the .toString() method, convert the array to a string.
// Using the .join(), convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)


const arr = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8]
	
let arr2=[]
let big = 0
		
		for(i of arr){
			if(arr[i] > big){
				big = arr[i]
			}
			else {
				continue
			}
		arr2.push(big)
		arr.splice(arr.indexOf(big), 1)
		}
	


console.log(arr2)
