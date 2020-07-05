let p = document.getElementsByTagName("p")[0]
p.addEventListener("click", function(){
    p.style.color = "blue"
    p.style.backgroundColor = "red"
    p.style.fontSize = "50px"
    p.elementFromPoint(150, 275)
})