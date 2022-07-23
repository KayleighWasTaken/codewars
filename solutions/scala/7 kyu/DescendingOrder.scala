//https://www.codewars.com/kata/5467e4d82edf8bbf40000155/
object Order {

  def descendingOrder(num: Int): Int = num.toString.sorted(Ordering[Char].reverse).toInt
}