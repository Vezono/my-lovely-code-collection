alert('First task.')
for(var i = 0; i < 11; i++){
    if(i & 2 == 0){
        console.log(i)
    }
}
alert('Second task.')
let number = 0
while (number < 100){
number = prompt('Enter number that bigger than 100.')
}
alert('Third task.')
number = prompt('Enter the number.')
let tts = 0
for(var i = 1; i < number; i++){
    if(i & 2 == 0){
        tts+=i
    }
}
alert(tts)
