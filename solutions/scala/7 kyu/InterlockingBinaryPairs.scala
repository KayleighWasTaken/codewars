//https://www.codewars.com/kata/628e3ee2e1daf90030239e8a/
object Sol {
  def interlockable(a: Long, b: Long): Boolean = {
    (a & b) == 0
  }
}