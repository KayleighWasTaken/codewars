//https://www.codewars.com/kata/546e2562b03326a88e000020
object Sol {
  def squareDigits(n: Int): Int = {
    n.toString.map(c => c.asDigit * c.asDigit).mkString.toInt
  }
}