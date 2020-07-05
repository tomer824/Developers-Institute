let offset = 0

function myMove() {
    
    setInterval(function () {
        if (offset == 350) {
            goLeft()
        } else {
            offset++
        }

        document.getElementById("animate").style.left = offset + "px"
    }, 50)
}

function goLeft(){
    setInterval(function () {
        if (offset == 0) {
            myMove()
        } else {
            offset--
        }

        document.getElementById("animate").style.left = offset + "px"
    }, 50)
}