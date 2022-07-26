//https://www.codewars.com/kata/54da539698b8a2ad76000228/
object Solution {
  def isValidWalk(walk: Seq[Char]): Boolean = {
    (walk.size == 10) & (walk.count(_=='n') == walk.count(_=='s')) & (walk.count(_=='e') == walk.count(_=='w'))
  }
}