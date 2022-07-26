//https://www.codewars.com/kata/570409d3d80ec699af001bf9/
object Sol {
  def fusc(n: Int): Int = {
    n match {
      case _ if n < 2 => n
      case _ if (n & 1) == 0 => fusc(n / 2)
      case _ => fusc(n / 2) + fusc(n / 2 + 1)
    }
  }
}