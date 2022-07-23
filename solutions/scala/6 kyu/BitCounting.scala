//https://www.codewars.com/kata/526571aae218b8ee490006f4/
object Kata {

  def countBits(n: Int): Int = n.toBinaryString.count(_ == '1')
}