let worlds = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Neptune", "Saturn", "Uranus", "Pluto"]
let colors = ["orange", "green", "blue", "red", "pink", "yellow", "white", "brown", "grey"]

// Create an array of planets of the solar system
// For each planet, in the array, create a div using createElement. This div should have a class named ‘planet’.
// Each planet should have a different background color. (Hint: add a new class to each planet)
// Finally append each div to the body.
// Bonus: Do the same process for moons. Be careful, each planet has a certain amount of moons; How should you display them ?

let section = document.getElementsByTagName("section")[0]

for(i = 0; i < worlds.length; i++){
    let planets = document.createElement("div")
    planets.classList.add("planet", colors[i])
    planets.style.backgroundColor=colors[i]
    let text = document.createTextNode(worlds[i])
    planets.appendChild(text)
    section.appendChild(planets)
}