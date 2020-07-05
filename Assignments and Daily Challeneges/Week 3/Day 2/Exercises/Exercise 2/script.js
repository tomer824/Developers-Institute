// Algorithmic Thinking
// Given an list of numbers.
// I want to know
// 1. What the biggest number is.
// 2. What the total is.
// 3. What the average is.
// Hints
// use a function
// think about what you want that function to return.

let arr = [12, 7, 45, 8, 17]

function biggestNumber(arr){
    let big = arr[0]
    for (num of arr){
        if(big < num){
            big = num
        }
    }
    console.log(big)
}

function total(arr){
    let final = 0
    for(num of arr){
        final += num
    }
    console.log(final)
}

function average(arr){
    let total = 0
    for(item of arr){
        total += item
    }
    total /= arr.length
    console.log(total)
}

function run(){
    biggestNumber(arr)
    total(arr)
    average(arr)
}

run()