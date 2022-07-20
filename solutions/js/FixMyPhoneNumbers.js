//https://www.codewars.com/kata/596343a24489a8b2a00000a2/
function isItANum(str) {
  let numbers = [...str].filter(x => "0123456789".includes(x)).join("")
  if (numbers.length == 11 && numbers[0] == "0") {
    return numbers
  } else {
    return "Not a phone number"
  }
}