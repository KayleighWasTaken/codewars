//https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/
object Sol {

  def evenOrOdd(number: Int): String = {
    if ((number & 1) == 0) "Even" else "Odd"
  }
}