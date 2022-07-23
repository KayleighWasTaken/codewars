//https://www.codewars.com/kata/5ce04eadd103f4001edd8986
object Sol {
  def solution(n: Int, b: Int): List[Int] = {
    (1 until (1 << n)).filter(x => (x & b) != 0).toList
  }
}