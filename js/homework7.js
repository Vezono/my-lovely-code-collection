//task 1
var sum = 0
for (var i = 0; i < 100; i++){
sum += i;
}

//task 2
var numbers = [2,	5, 9, 15, 0, 4]
for (var i = 0; i < numbers.length; i++){
if (i < 10 && i > 3){
console.log(i);
}
}

//task 3
numbers = [1, 2, 5, 9, 4, 13, 4, 10]
for each (i in numbers){
if (i == 4){
console.log('Есть тут четверка. Выхожу из цикла');
break
}
}
