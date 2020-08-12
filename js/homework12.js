pic.style.right = 0
pic.style.bottom = 0
function moveLeft(){
    pic.style.right = parseInt(pic.style.right) + 10 + 'px'
}
function moveRight(){
    pic.style.right = parseInt(pic.style.right) - 10 + 'px'
}
function moveUp(){
    pic.style.bottom = parseInt(pic.style.bottom) + 10 + 'px'
}
function moveDown(){
    pic.style.bottom = parseInt(pic.style.bottom) - 10 + 'px'
}
function Eventer(event){
if (event.keyCode == 68){moveRight()} //D
if (event.keyCode == 65){moveLeft()}  //A
if (event.keyCode == 83){moveDown()} //S
if (event.keyCode == 87){moveUp()} //W
}

document.body.onkeydown = Eventer;
