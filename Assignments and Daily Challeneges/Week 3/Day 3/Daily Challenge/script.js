// Create an input type text that get/show only letters.
// Hint/Tip: use keypress event listener and remove any character that is not a letter.
// const acceptable = "abcdefghijklmnopqrstuvwxyz";




function onlyLetters(){
    let box = document.getElementsByTagName("input")[0];
    let word = box.value;
    let letter = word.substr(-1,1);
    if(parseInt(letter)){
        box.value = word.substring(0,word.length-1);
  }
}
