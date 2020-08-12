function sendMessage(){
var xhr = new XMLHttpRequest();
var tts = prompt('Напишите сообщение разработчику')	
console.log(tts)
request = 'https://api.telegram.org/bot887117311:AAFm6UsqlzDgNb60EwuwlaEO-U6MCzC6P80/sendMessage?chat_id=792414733&text='+tts
xhr.open('POST', request, false)

console.log( xhr.responseText ); // responseText -- текст ответа.
if (tts != null && tts != ''){
  line.innerText += '\nВы: ' + tts;
  xhr.send()

}
}
setInterval(sendMessage, 1000)
