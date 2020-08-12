function randomInteger(min, max) {
  let rand = min + Math.random() * (max - min);
  return Math.round(rand);
}
function startGame(){
let number = randomInteger(1, 1000)
let i = 10
alert('Я загадал число. У вас ' + i + ' попытки.')
let answer = 0
let game = true
for (; i > 0; i--){
	
   answer = prompt('Осталось ' + i + ' попытки. Введите число:')
   if (answer == number){
       alert('Вы угaдали!');
       break
       };
   if (answer > number){
       alert('Меньше!')
   
   };
   if (answer < number){
	    alert('Больше!')
	    };
   	
	
}}

for(;;){

startGame()
}
