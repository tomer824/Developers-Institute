for(i = 1; i < 6; i++){
    console.log("* ".repeat(i))
}

let rows = 5

    for (let i = 0; i < rows; i++) {
        let output = '';
        for (let j =0; j < rows - i; j++) output += ' ';
        for (let k = 0; k <= i; k++) output += '* ';
        console.log(output);  
    } 

