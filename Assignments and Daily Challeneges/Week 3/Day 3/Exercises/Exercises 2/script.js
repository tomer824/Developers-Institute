let button = document.getElementById("btn")
button.onclick = function insert_Row() {
    let add_row = document.createElement("tr")
    for (let i = 0; i < 2; i++) {
        let td = document.createElement("td")
        td.innerHTML = "row 3"
        add_row.appendChild(td)
    }
    let table = document.getElementsByTagName("table")[0]
    table.appendChild(add_row)
}
