// https://www.codewars.com/kata/576bb71bbbcf0951d5000044/
object Kata {
  def countPositivesSumNegatives(integers: Array[Int]): (Int, Int) = {
    val grouped = integers.groupBy(_>0)
    (if (grouped.contains(true)) grouped(true).size else 0, if (grouped.contains(false)) grouped(false).sum else 0)
  }
}