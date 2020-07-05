// 1.

for(let i = 0; i < 4; i++){
    let para = document.getElementsByTagName("p")[i]
    para.classList.add("para_article")
}

let rmv = document.getElementsByClassName("para_article")[3]
rmv.remove()


let head2 = document.getElementsByTagName("h2")[0]
head2.addEventListener("click", function(){
 headFunction(head2)
})

function headFunction(head2){
    head2.remove()
}

let h1 = document.getElementsByTagName("h1")[0];
h1.style.fontSize = Math.floor((Math.random() * 101) + 0) + "px";


let pErase = document.getElementsByTagName("p")[0]
pErase.addEventListener("click", function(){
    pErase.style.display = "none"
})


let pFade = document.getElementsByTagName("p")[1]
pFade.addEventListener("click", fade)
function fade(e){
    pFade.style.visibility = "hidden"
    // pFade.style.fontSize = "20px"
    pFade.style.transition = "all 2s"
}

let table_div = document.getElementsByTagName("div")[0]
let table = document.createElement("table")
table_div.appendChild(table)
let row = document.createElement("tr")
table.appendChild(row)
let td1 = document.createElement("td")
let td2 = document.createElement("td")
row.appendChild(td1)
row.appendChild(td2)
let input1 = document.getElementsByTagName("input")[0]
input1.oninput = function(){
    td1.innerHTML = this.value
}
let input2 = document.getElementsByTagName("input")[1]
input2.oninput = function(){
    td2.innerHTML = this.value
}



// 2.

function getBold_items(){
let bold = document.getElementsByTagName("strong")
return bold
}

function highlight(){
    let bold = getBold_items()
    for(let item of bold){
        item.addEventListener("mouseover", function(){
            item.style.color = "blue"
        })
       
    }
    return
}

highlight()

function return_normal(){
    let bold = getBold_items()
    for(let item of bold){
        item.addEventListener("mouseleave", function(){
            item.style.color = "black"
       })
    }
    return
}
return_normal()

// 3.

