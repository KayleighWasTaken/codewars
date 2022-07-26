//https://www.codewars.com/kata/5526fc09a1bbd946250002dc/
object Parity {

  def findOutlier(integers: List[Int]): Int = {
    (integers.map(x => x & 1).sum) match {
      case 1 => integers.sortBy(x => x & 1).last
      case _ => integers.sortBy(x => x & 1).head
    }
  }
}