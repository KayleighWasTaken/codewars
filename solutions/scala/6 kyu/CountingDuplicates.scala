//https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/
object Dups {

  def duplicateCount(str: String): Int = {
    str.toLowerCase.toSet.count(c => str.toLowerCase.count(_ == c) > 1)
  }
}