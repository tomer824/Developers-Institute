let button = document.getElementById("btn")

button.addEventListener("click", changeText)

function changeText() {
    if(button.innerHTML == "Thanks!"){
    button.innerHTML = "Click Me!";
    text.innerHTM = "Well Done"
    }
    else {
        button.innerHTML = "Thanks!"
        text.innerHTML - "Try Again"
    }
}
