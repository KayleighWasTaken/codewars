//https://www.codewars.com/kata/54ba84be607a92aa900000f1/
object Sol {
  def isIsogram(s: String): Boolean = {
    s.toLowerCase.toSet.size == s.size
  }
}