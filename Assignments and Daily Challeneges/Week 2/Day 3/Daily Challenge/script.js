const arr = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8]
	
let arr2=[]

	while (arr.length > 0)
		let big = arr[0]
		for(i = 0; i < arr.length; i++){
			if (arr[i] > big){
				big = arr[i]
			}
			else {
				continue
			}
			arr2.push(big)
			arr.splice(arr.indexOf(big)
		}


console.log(arr2)
