name = prompt('Whats your name?')
age = prompt('How old are you?')
tts = '' //Text To Send
if (age > 17){
    tts += 'your are fullaged!'
}
else {
    tts += 'you are not fullaged!'
}
alert(name + ', ' + tts)
