var items = ['English', 'Phisycs', 'Music', 'Technologis', 'Biology', 'Urkainian']
function ShowMas(mas){
for(var i = 0; i < mas.length; i++){
    console.log(i + '. ' + mas[i])}
}

ShowMas(items)
items[0] = 'Классный час'
items.push('Math')
items.unshift('Math')


function randInt(min, max) {
  let rand = min + Math.random() * (max - min);
  return Math.round(rand);
}
function FindItem(mas, elem){
for(var i = 0; i < mas.length; i++){
    if (mas[i] == elem){
    return i;
    }
}
}

function arrayFill(mas, elem, count){
for (var i = 0; i < count; i++){
mas.push(elem)
}
    
function ixator(mas, count){
for (var i = 0; i < count; i++){
mas.push('x'*i+1)
}
}

function fillRandom(mas){
for (var i = 0; i < 10; i++){
mas.push(randInt(1, 10))
}
}    
function maxInArray(mas){
return Math.max(mas)
}
function minInArray(mas){
return Math.min(mas)
}
