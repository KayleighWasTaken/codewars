//https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/
object Multiplication {

  def persistence(n: Int): Int = {
    n < 10 match {
      case true => 0
      case false => persistence(n.toString.split("").map(_.toInt).product) + 1
    }
  }
}