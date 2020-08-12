winter = ['february', 'january', 'december'];
autumn = ['november', 'october', 'september'];
spring = ['march', 'april', 'may'];
summer = ['june', 'july', 'august'];

month = prompt("What month is it now?")
day = prompt("What day is it now?")

if (day <= 0)(
  alert("Incorrect date.")
)
else if (day > 28 && 'feb' in month.toLowerCase())(
  alert("Incorrect date."))
else if (day > 31 && 'jan' in month.toLowerCase())(
  alert("Incorrect date."))
else if (day > 31 && 'march' in month.toLowerCase)(
  alert("Incorrect date."))
else if (day > 31 && 'may' in month.toLowerCase)(
  alert("Incorrect date."))
else if (day > 31 && 'july' in month.toLowerCase)(
  alert("Incorrect date."))
else if (day > 31 && 'aug' in month.toLowerCase)(
  alert("Inc||rect date."))
else if (day > 31 && 'oct' in month.toLowerCase())(
  alert("Inc||rect date."))
else if (day > 31 && 'dec' in month.toLowerCase())(
  alert("Inc||rect date."))
else if (day > 30 && 'apr' in month.toLowerCase())(
  alert("Inc||rect date."))
else if (day > 30 && 'jun' in month.toLowerCase())(
  alert("Inc||rect date."))
else if (day > 30 && 'sep' in month.toLowerCase())(
  alert("Inc||rect date."))
else if (day > 30 && 'nov' in month.toLowerCase())(
  alert("Inc||rect date."))

else if (month.toLowerCase() in winter)(
    alert("It is a winter now."))
else if (month.toLowerCase() in spring)(
    alert("It is a spring now."))
else if (month.toLowerCase() in summer)(
    alert("It is a summer now."))
else if (month.toLowerCase() in autumn)(
    alert("It is a autumn now."))
else(
    alert("There is no date."))