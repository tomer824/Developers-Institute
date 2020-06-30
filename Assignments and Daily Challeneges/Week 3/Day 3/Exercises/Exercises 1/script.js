function hotelCost(numNights){
    return numNights * 150
}

function destination(place){    
        if(place == "Paris"){
            return 300
        }
        else if(place == "New York"){
            return 500
        }
        else{
            return 200
        }
}

function totalTripCost(){
    console.log("$" + (hotelCost(1) + destination("Paris")))
}

totalTripCost()