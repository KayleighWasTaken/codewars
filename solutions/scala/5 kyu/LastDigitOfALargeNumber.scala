//https://www.codewars.com/kata/5511b2f550906349a70004e1/
object Sol {
  def lastDigit(n1: BigInt, n2: BigInt): BigInt = {
    n1.modPow(n2, 10)
  }
}