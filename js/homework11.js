color = new Array("https://i.ytimg.com/vi/lkQ0LDx9jHs/maxresdefault.jpg", "https://i.pinimg.com/originals/1c/ba/1e/1cba1e5e40356f6edb0235c8a09a07d5.jpg", "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg");  
//номер цвета, которым будет выполена заливка фона
var num_color = 0; //функция, изменяющая цвет заливки фона страницы 
function change_color() {
document.body.style.backgroundColor = color[num_color]; 
num_color++;
if  (num_color == color.length) {
num_color = 0;} }
document.body.onclick = change_color
