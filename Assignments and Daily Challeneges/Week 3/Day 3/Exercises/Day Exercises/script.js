function sale(sale){
    let banner = document.getElementsByTagName("div")[0]
    banner.style.width = ("140px")
    banner.style.height = ("70px")
    banner.innerHTML = sale
    banner.style.backgroundColor = "blue"
    banner.style.color = "red"

    let seconds = 9
    let time = setInterval(function() {
        banner.innerHTML = "The sale ends in " + seconds + " seconds."  
        seconds--
        if(seconds == -1){
            clearInterval(time)
        }
    }, 1000);
    
}

sale("The sale ends in 10 seconds.")

