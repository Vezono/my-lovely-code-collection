var x = 100;
pic.src = "https://openclipart.org/image/300px/svg_to_png/173850/race-car.png"
pic.style.left = x;

 //шаг перемещения строки
var step = 2;
 //правая граница перемещения строки
var right_border = 500;


 //получаем длину строки
var len_text = parseInt(pic.innerHTML.width);

function RunningCar() {
//получаем новые координаты строки для левого края
x =x+step;
 //получаем новые координаты строки для правого края
var r = x + len_text * 10;
 //если строка правым краем касается края тела
if (r >= right_border) {
x = 1; //возвращаем строку в начало страницы
}
pic.style.left = x + "px";
}
 //Вызываем функцию по таймеру
setInterval(RunningCar, 100);
