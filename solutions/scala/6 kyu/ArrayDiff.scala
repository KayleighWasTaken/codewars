//https://www.codewars.com/kata/523f5d21c841566fde000009/
object Kata {
  def arrayDiff(a: Seq[Int], b: Seq[Int]): Seq[Int] = {
    a.filter(x => !(b contains x))
  }
}