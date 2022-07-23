//https://www.codewars.com/kata/596343a24489a8b2a00000a2/
object Sol{

  def isItANum(str: String): String = {
    var numbers = str.toList.filter(c => "0123456789" contains c).mkString
    if ((numbers.length == 11) && (numbers.startsWith("0"))) {
      numbers
    } else {
      "Not a phone number"
    }
  }
}