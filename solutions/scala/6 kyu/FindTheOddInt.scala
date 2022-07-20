//https://www.codewars.com/kata/54da5a58ea159efa38000836/
object FindTheOddInt {

  def findOdd(xs: Seq[Int]): Int = {
    xs.filter(x => xs.count(_ == x) % 2 != 0).head
  }
}