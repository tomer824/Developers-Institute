// 1.

let nav = document.getElementById("navBar");
nav.setAttribute("id", "socialNetworkNavigation");
console.log(nav);

let newElement = document.createElement("li");
let newText = document.createTextNode("logout")
newElement.appendChild(newText)
document.getElementById("list").appendChild(newElement)