//https://www.codewars.com/kata/54c27a33fb7da0db0100040e/
object Sol {

  def isSquare(x: Int): Boolean = {
    scala.math.pow(x, 0.5) % 1 == 0
  }
}