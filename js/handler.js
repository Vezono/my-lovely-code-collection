var last_id = 0
function getMessages(){
var xhr = new XMLHttpRequest();
request = 'https://api.telegram.org/bot887117311:AAFm6UsqlzDgNb60EwuwlaEO-U6MCzC6P80/getUpdates'
xhr.open('POST', request, false)
xhr.send()
var answer = JSON.parse(xhr.responseText)['result']
var last = answer[answer.length - 1]

  
if (answer[answer.length - 1]['update_id'] != last_id){
  line.innerText += '\nРазработчик: ' + last['message']['text']
}
last_id = answer[answer.length - 1]['update_id']
}
setInterval(getMessages, 500)
