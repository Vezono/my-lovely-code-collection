function ixator(mas, count){      //task 1
for (var i = 0; i < count; i++){
mas.push('x'*i+1)
}
}

function arrayFill(mas, elem, count){               //task 2
for (var i = 0; i < count; i++){
mas.push(elem)
}
    


function fillRandom(mas, count){               //task3          
for (var i = 0; i < count; i++){
mas.push(randInt(1, 10))
}
}    
function maxInArray(mas){      //task 4
return Math.max(mas)
}
function minInArray(mas){     // extra task
return Math.min(mas)
}
