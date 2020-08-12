function randomInteger(min, max) {
	let rand = min + Math.random() * (max - min);
  	return Math.round(rand);
}
// Func
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
			score++
       		break
       	};
   		if (answer > number){
       		alert('Меньше!')  
   		};
   		if (answer < number){
	    	alert('Больше!')
	    };
   	}
}

// Gamestart

var score = 0

while(true){
	toplay = prompt('Вы выиграли ' + score + ' раз. Хотите сыграть?')
	if (toplay.toLowerCase() != 'yes'){
		break
	}
	startGame()
}
