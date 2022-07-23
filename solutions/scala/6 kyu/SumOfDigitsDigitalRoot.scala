//https://www.codewars.com/kata/541c8630095125aba6000c00/
object SumOfDigits {

  def digitalRoot(n: Int): Int = {
    if (n % 9 != 0 | n == 0) {
      n % 9
    } else {
      9
    }
  }
}