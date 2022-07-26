//https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/
object Snail {
  def snail(xs: List[List[Int]]): List[Int] = {
    if (xs.nonEmpty){
      xs.head ++ snail(xs.tail.transpose.reverse)
    } else {
      List[Int]()
    }
  }
}